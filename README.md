# Music Organizer Script

This Python script organizes your music files into folders based on their album names and deletes duplicate files. It uses the `mutagen` library to read metadata from audio files and ensures that folder names are valid for Windows by sanitizing invalid characters.

---

## Features

- **Organizes Music by Album**: Moves music files into folders named after their album.
- **Deletes Duplicates**: Detects and removes duplicate files in the same album folder.
- **Sanitizes Folder Names**: Replaces invalid characters in album names to ensure compatibility with Windows file systems.

---

## Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Mutagen Library**: Install the `mutagen` library to read metadata from audio files.

   ```bash
   pip install mutagen
   ```

---

## Usage

1. **Place the Script in Your Music Directory**:
   - Save the script (`music_organizer.py`) in the directory containing your music files.

2. **Update the Music Directory Path**:
   - Open the script in a text editor and update the `music_directory` variable with the path to your music folder.

   ```python
   music_directory = r"C:\Users\user\Music"
   ```

3. **Run the Script**:
   - Open a terminal or command prompt, navigate to the directory where the script is located, and run the script.

   ```bash
   python music_organizer.py
   ```

4. **Check the Output**:
   - The script will create folders named after the albums and move the corresponding music files into them.
   - Duplicate files will be deleted.

---

## Example

### Before Running the Script:
```
C:\Users\user\Music\
    Song1.mp3
    Song2.mp3
    Song3.mp3
```

### After Running the Script:
```
C:\Users\user\Music\
    Album1\
        Song1.mp3
        Song2.mp3
    Album2\
        Song3.mp3
```

---

## Notes

- **Supported File Formats**: The script is designed to work with MP3 files that have ID3 tags. If you have other formats (e.g., FLAC, WAV), you may need to modify the script to handle their metadata.
- **Backup Your Files**: Always back up your music files before running the script to avoid accidental data loss.
- **Invalid Characters**: The script replaces invalid characters (`<>:"/\\|?*`) in album names with underscores (`_`).

---

## Troubleshooting

1. **Error: `NotADirectoryError`**:
   - Ensure the album names do not contain invalid characters. The script sanitizes these, but if the issue persists, check for other edge cases (e.g., extremely long folder names).

2. **Error: `FileNotFoundError`**:
   - Double-check the `music_directory` path to ensure it points to the correct folder.

3. **Error: `mutagen` Not Installed**:
   - Install the `mutagen` library using `pip install mutagen`.

---

## License

This script is provided under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it as needed.

---

## Author

[Kudakwashe Marongedza](https://github.com/ashemaro)

---