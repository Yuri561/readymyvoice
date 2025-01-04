import pygame
import time
import os
from utils.intro_txt import intro_txt
from functools import partial


def play_audio(file_path):
    """Plays an audio file using pygame."""
    try:
        # Initialize pygame mixer
        pygame.mixer.init()
        # Load and play the audio file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing: {file_path}")

        # Wait for the playback to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    except pygame.error as e:
        print(f"Error playing audio: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def show_audios(path, textbox):

    if not os.path.exists(path):
        intro_txt("Error: The folder does not exist.\n", textbox)
        return

    # Retrieve list of .mp3 files in the directory
    try:
        mp3_files = [file for file in os.listdir(path) if file.endswith(".mp3")]
    except Exception as e:
        intro_txt(f"Error accessing folder: {e}\n", textbox)
        return

    if not mp3_files:
        textbox.insert("end", "No MP3 files found in the folder.\n")
        return

    # Display the MP3 files
    textbox.insert("end", "MP3 Files:\n")
    for file in mp3_files:
        # Create the full path for playback
        file_path = os.path.join(path, file)

        # Add the file as clickable text
        textbox.insert("end", file + "\n", file)  # Assign a unique tag per file
        textbox.tag_config(file, foreground="blue", underline=1)  # Style the text

        # Use functools.partial to bind the file path to the click event
        textbox.tag_bind(
            file,
            "<Button-1>",
            partial(on_file_click, file_path)
        )


def on_file_click(file_path, event=None):
    """
    Handles the click event for an MP3 file.

    Parameters:
        file_path (str): Path to the MP3 file.
        event: Optional tkinter event (not used).
    """
    print(f"Clicked on: {file_path}")
    play_audio(file_path)
