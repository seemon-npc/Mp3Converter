import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import threading

# ---------------- WINDOW ----------------
window = tk.Tk()
window.title("MP4 → MP3 Converter")
window.resizable(False, False)
window.configure(bg="#0F172A")  # dark blue-black

# ---------------- THEME COLORS ----------------
BLUE = "#2563EB"
DARK = "#0F172A"
GRAY = "#94A3B8"
WHITE = "white"

# ---------------- STATE ----------------
selected_files = []
output_folder = ""

# ---------------- FUNCTIONS ----------------
def select_files():
    global selected_files
    selected_files = filedialog.askopenfilenames(
        title="Select MP4 Files",
        filetypes=[("MP4 files", "*.mp4")]
    )
    if selected_files:
        files_label.config(text=f"{len(selected_files)} files selected")
        convert_btn.config(state="normal")
        status_label.config(text="")

def select_output_folder():
    global output_folder
    folder = filedialog.askdirectory(title="Select Output Folder")
    if folder:
        output_folder = folder
        output_label.config(text=folder)

def start_conversion():
    if not selected_files:
        messagebox.showerror("Error", "No files selected")
        return
    if not output_folder:
        messagebox.showerror("Error", "Select output folder")
        return

    convert_btn.config(state="disabled")
    threading.Thread(target=convert_batch).start()

def convert_batch():
    progress["value"] = 0
    progress["maximum"] = len(selected_files)

    for index, video_path in enumerate(selected_files, start=1):
        try:
            status_label.config(text=f"Converting {index}/{len(selected_files)}")
            window.update()

            video = VideoFileClip(video_path)
            audio = video.audio

            if audio is None:
                raise Exception("No audio found")

            base_name = os.path.splitext(os.path.basename(video_path))[0]
            output_path = os.path.join(output_folder, base_name + ".mp3")

            audio.write_audiofile(output_path, logger=None)

            audio.close()
            video.close()

            progress["value"] += 1

        except Exception as e:
            messagebox.showerror("Error", f"{os.path.basename(video_path)}\n{e}")

    status_label.config(text="All conversions completed ✅", fg="lightgreen")
    convert_btn.config(state="normal")

# ---------------- UI ----------------
header = tk.Label(
    window,
    text="MP4 → MP3 Converter",
    font=("Arial", 18, "bold"),
    bg="#1E293B",
    fg=WHITE,
    pady=10
)
header.pack(fill="x")

frame = tk.Frame(window, bg=DARK, padx=20, pady=20)
frame.pack()

select_btn = tk.Button(
    frame, text="Select MP4 Files",
    font=("Arial", 12),
    width=25,
    bg=BLUE, fg=WHITE,
    command=select_files
)
select_btn.pack(pady=8)

files_label = tk.Label(
    frame, text="No files selected",
    bg=DARK, fg=GRAY
)
files_label.pack()

output_btn = tk.Button(
    frame, text="Select Output Folder",
    font=("Arial", 12),
    width=25,
    bg=BLUE, fg=WHITE,
    command=select_output_folder
)
output_btn.pack(pady=10)

output_label = tk.Label(
    frame, text="No folder selected",
    bg=DARK, fg=GRAY,
    wraplength=350
)
output_label.pack()

convert_btn = tk.Button(
    frame, text="Convert to MP3",
    font=("Arial", 13, "bold"),
    width=25,
    bg=BLUE, fg=WHITE,
    state="disabled",
    command=start_conversion
)
convert_btn.pack(pady=15)

progress = ttk.Progressbar(
    frame, orient="horizontal",
    length=300, mode="determinate"
)
progress.pack(pady=10)

status_label = tk.Label(
    frame, text="",
    bg=DARK, fg="yellow"
)
status_label.pack()

# ---------------- CENTER WINDOW ----------------
window.update()
w, h = window.winfo_width(), window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (w // 2)
y = (window.winfo_screenheight() // 2) - (h // 2)
window.geometry(f"{w}x{h}+{x}+{y}")

window.mainloop()
