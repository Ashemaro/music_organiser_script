import os
import shutil
import re
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def sanitize_folder_name(name):
    # Replace invalid characters with an underscore or remove them
    sanitized_name = re.sub(r'[<>:"/\\|?*]', '_', name)
    return sanitized_name.strip()  # Remove leading/trailing spaces

def get_album_name(file_path):
    try:
        audio = MP3(file_path, ID3=EasyID3)
        return audio.get('album', ['Unknown Album'])[0]
    except Exception as e:
        print(f"Error reading metadata from {file_path}: {e}")
        return 'Unknown Album'

def organize_songs(directory):
    # Dictionary to track files and their albums
    albums = {}

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

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
            print(f"Duplicate found: {filename}")
            os.remove(file_path)  # Delete the duplicate file
        else:
            shutil.move(file_path, new_file_path)
            print(f"Moved {filename} to {album_folder}")

if __name__ == "__main__":
    # Specify the directory containing your songs
    music_directory = r"C:\Users\user\Music"

    # Organize the songs
    organize_songs(music_directory)