import os
import shutil
import re
from tkinter import Tk, Button, Label, filedialog, ttk
from mutagen import File
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.wave import WAVE
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Function to display ASCII art banner
def display_banner():
    print(Fore.CYAN + r"""
  _    _                   _ 
 | |  | |                 (_)
 | |__| | __ _ _ __  _ __  _ 
 |  __  |/ _` | '_ \| '_ \| |
 | |  | | (_| | | | | | | | |
 |_|  |_|\__,_|_| |_|_| |_|_|
    """ + Style.RESET_ALL)

# Function to sanitize folder names
def sanitize_folder_name(name):
    sanitized_name = re.sub(r'[<>:"/\\|?*]', '_', name)
    return sanitized_name.strip()

# Function to get album name from audio file
def get_album_name(file_path):
    try:
        audio = File(file_path, easy=True)
        if audio is None:
            print(Fore.YELLOW + f"Unsupported file format: {file_path}" + Style.RESET_ALL)
            return 'Unknown Album'
        if isinstance(audio, MP3) or isinstance(audio, EasyID3):
            return audio.get('album', ['Unknown Album'])[0]
        elif isinstance(audio, FLAC):
            return audio.get('album', ['Unknown Album'])[0]
        elif isinstance(audio, WAVE):
            return audio.get('album', ['Unknown Album'])[0]
        else:
            return audio.tags.get('album', ['Unknown Album'])[0]
    except Exception as e:
        print(Fore.RED + f"Error reading metadata from {file_path}: {e}" + Style.RESET_ALL)
        return 'Unknown Album'

# Function to organize songs
def organize_songs(directory, progress_bar, status_label):
    if not directory:
        status_label.config(text="No directory selected!", fg="red")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    total_files = len(files)
    progress_bar["maximum"] = total_files

    for i, filename in enumerate(files):
        file_path = os.path.join(directory, filename)

        # Get the album name
        album_name = get_album_name(file_path)

        # Sanitize the album name
        sanitized_album_name = sanitize_folder_name(album_name)

        # Create a folder for the album if it doesn't exist
        album_folder = os.path.join(directory, sanitized_album_name)
        if not os.path.exists(album_folder):
            os.makedirs(album_folder)

        # Move the file to the album folder
        new_file_path = os.path.join(album_folder, filename)

        # Check for duplicates
        if os.path.exists(new_file_path):
            print(Fore.YELLOW + f"Duplicate found: {filename}" + Style.RESET_ALL)
            os.remove(file_path)  # Delete the duplicate file
        else:
            shutil.move(file_path, new_file_path)
            print(Fore.GREEN + f"Moved {filename} to {album_folder}" + Style.RESET_ALL)

        # Update progress bar and status label
        progress_bar["value"] = i + 1
        status_label.config(text=f"Processed {i + 1}/{total_files} files", fg="blue")
        progress_bar.update()

    status_label.config(text="Organization complete!", fg="green")

# Function to open directory dialog
def choose_directory(progress_bar, status_label):
    directory = filedialog.askdirectory()
    if directory:
        organize_songs(directory, progress_bar, status_label)

# Create the main GUI window
def create_gui():
    root = Tk()
    root.title("Harmoni - Music Organizer")
    root.geometry("400x200")

    # Label for instructions
    Label(root, text="Select a directory to organize music files:").pack(pady=10)

    # Button to choose directory
    choose_button = Button(root, text="Choose Directory", command=lambda: choose_directory(progress_bar, status_label))
    choose_button.pack(pady=10)

    # Progress bar
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=10)

    # Status label
    status_label = Label(root, text="", fg="blue")
    status_label.pack(pady=10)

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    display_banner()
    create_gui()