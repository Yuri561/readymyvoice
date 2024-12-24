
import pygame
import time


def play_audio(file_path):
    try:
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load and play the audio file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait for the playback to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    except Exception as e:
        print(f"Error playing audio: {e}")
