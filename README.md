# Harmoni - Music Organizer

Harmoni is a Python script that organizes your music files into folders based on their album names and deletes duplicate files. It supports multiple audio formats (MP3, FLAC, WAV, etc.) and provides a user-friendly GUI for selecting directories and tracking progress. The script also includes a colorful terminal output and an ASCII art banner for a visually appealing experience.

---

## Features

- **Organizes Music by Album**: Moves music files into folders named after their album.
- **Deletes Duplicates**: Detects and removes duplicate files in the same album folder.
- **Supports Multiple Formats**: Works with MP3, FLAC, WAV, and other formats supported by `mutagen`.
- **Graphical User Interface (GUI)**: Allows users to manually select a directory using a file dialog.
- **Progress Bar**: Shows the progress of file organization in real-time.
- **Status Updates**: Provides real-time updates in the GUI (e.g., "Processed 5/10 files").
- **Colored Terminal Output**: Uses `colorama` for better readability of success, warning, and error messages.
- **ASCII Art Banner**: Displays a stylish "Harmoni" banner when the script starts.

---

## Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **External Libraries**: Install the required libraries using the `requirements.txt` file.

---

## Installation

1. Clone or download the repository.
2. Navigate to the project directory.
3. Install the dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Script**:
   - Save the script as `harmoni_music_organizer.py` and run it:
     ```bash
     python harmoni_music_organizer.py
     ```

2. **Choose Directory**:
   - Click the "Choose Directory" button in the GUI and select the folder containing your music files.

3. **Wait for Completion**:
   - The script will organize the files into folders based on their album names and display progress in the GUI.

---

## Supported Audio Formats

- **MP3**: Uses `mutagen.mp3.MP3` or `mutagen.easyid3.EasyID3`.
- **FLAC**: Uses `mutagen.flac.FLAC`.
- **WAV**: Uses `mutagen.wave.WAVE`.
- **Other Formats**: Uses `mutagen.File` as a fallback for other formats supported by `mutagen`.

---

## Example

### Before Running the Script:
```
C:\Users\user\Music\
    Song1.mp3
    Song2.flac
    Song3.wav
```

### After Running the Script:
```
C:\Users\user\Music\
    Album1\
        Song1.mp3
        Song2.flac
    Album2\
        Song3.wav
```

---

## Screenshots

### ASCII Art Banner:
```
  _    _                   _ 
 | |  | |                 (_)
 | |__| | __ _ _ __  _ __  _ 
 |  __  |/ _` | '_ \| '_ \| |
 | |  | | (_| | | | | | | | |
 |_|  |_|\__,_|_| |_|_| |_|_|
```

### GUI:
- A simple window with a "Choose Directory" button, a progress bar, and a status label.

---

## Troubleshooting

1. **Error: `No directory selected!`**:
   - Ensure you select a valid directory using the file dialog.

2. **Error: `Unsupported file format`**:
   - The script skips unsupported file formats. Ensure your files are in a supported format (MP3, FLAC, WAV, etc.).

3. **Error: `mutagen` or `colorama` not installed**:
   - Install the required libraries using `pip install -r requirements.txt`.

4. **Error: `NotADirectoryError`**:
   - Ensure the album names do not contain invalid characters. The script sanitizes these, but if the issue persists, check for other edge cases (e.g., extremely long folder names).

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it as needed.

---

## Author

[Kudakwashe Marongedza](https://github.com/ashemaro)  
**Harmoni - Music Organizer**

---

## Contributing

Contributions are welcome! If you'd like to improve the script, feel free to open an issue or submit a pull request.

---