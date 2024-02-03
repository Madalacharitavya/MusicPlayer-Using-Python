This is a simple music player application created using the Tkinter library in Python. It allows the user to load a directory containing music files, display them in a playlist, and control the playback of the songs.
1. Importing necessary modules:
   - `from tkinter import *` imports all the classes and functions from the Tkinter module.
   - `from tkinter import filedialog` imports the filedialog module from Tkinter for selecting directories.
   - `import pygame.mixer as mixer` imports the pygame.mixer module for audio playback.
   - `import os` imports the os module for working with files and directories.
2. Initializing the mixer:
   - `mixer.init()` initializes the pygame.mixer module.
3. Functions:
   - `play_song(song_name, songs_list, status)`: This function is called when the user clicks the "Play" button. It sets the selected song as the current song, loads it using `mixer.music.load()`, and plays it using `mixer.music.play()`.
   - `stop_song(status)`: This function is called when the user clicks the "Stop" button. It stops the currently playing song using `mixer.music.stop()`.
   - `load(listbox)`: This function is called when the user clicks the "Load Directory" button. It opens a directory dialog using `filedialog.askdirectory()` and sets the current working directory to the selected directory. It then lists all the files in the directory and adds them to the playlist.
   - `pause_song(status)`: This function is called when the user clicks the "Pause" button. It pauses the currently playing song using `mixer.music.pause()`.
   - `resume_song(status)`: This function is called when the user clicks the "Resume" button. It resumes the paused song using `mixer.music.unpause()`.
4. Creating the GUI:
   - The GUI is created using the Tkinter library.
   - Various frames are created using the `LabelFrame` class to group related elements.
   - `StringVar` variables are used to store and update the current song and song status.
   - A playlist `Listbox` is created to display the songs in the selected directory.
   - Buttons are created for controlling playback and loading the directory.
5. Configuring and placing the GUI elements:
   - The elements are configured with their respective properties, such as text, background color, font, and commands.
   - The elements are placed using the `place` and `pack` methods to define their position in the GUI window.
6. The `mainloop()` function is called to start the GUI event loop and handle user interactions.
When the user interacts with the GUI, the corresponding functions are called to perform the desired actions, such as playing, stopping, pausing, resuming, and loading songs.Overall, this code creates a basic music player interface using Tkinter and utilizes the pygame.mixer module for audio playback.

https://github.com/Madalacharitavya/MusicPlayer-Using-Python/assets/102969979/3cd2fa67-ea86-41e1-9e85-c8fd71856864

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

