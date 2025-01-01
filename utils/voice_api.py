import io
import threading
from elevenlabs.client import ElevenLabs
import os
from datetime import datetime
from tkinter import messagebox
import pygame

client = ElevenLabs(
    api_key='sk_14896d0859b0623878a8832e727864beebbd6e47cb7e7739'
)

def txt_to_speech(command, textbox, voice_id="JBFqnCBsd6RMkjVDRZzb"):
    try:
        # Call ElevenLabs API
        response = client.text_to_speech.convert(
            voice_id=voice_id,
            output_format="mp3_44100_128",
            text=command,
            model_id="eleven_multilingual_v2",
        )
        # Save the audio
        folder = 'audio_files'
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'output_{timestamp}.mp3'
        file_path = os.path.join(folder,filename)

        with open(file_path, "wb") as f:
            #iterate over the response
            for chunk in response:
                f.write(chunk)

        # Update the textbox with a success message
        textbox.insert("end", "\n")
        messagebox.showinfo(title="Success", message=f"Conversion successful! File saved to {file_path}")
        textbox.insert("end", "\n")  # Add a newline after the text

        return file_path
    except Exception as e:
        # Update the textbox with an error message
        messagebox.showerror(title="Error", message=f"an error has occurred please try again {e}")
        textbox.insert("end", "\n")  # Add a newline after the text

def speak_text(text, voice_id="pFZP5JQG7iQjIQuC4Bku"):
    def play_audio():
        try:
            # Call ElevenLabs API
            response = client.text_to_speech.convert(
                voice_id=voice_id,
                output_format="mp3_44100_128",
                text=text,
                model_id="eleven_multilingual_v2",
            )

            # Initialize Pygame mixer
            pygame.mixer.init()
            # Create a BytesIO object for direct playback
            audio_data = io.BytesIO()
            for chunk in response:
                audio_data.write(chunk)

            # Load and play the audio
            audio_data.seek(0)  # Reset pointer to the start of the stream
            pygame.mixer.music.load(audio_data, "mp3")
            pygame.mixer.music.play()

            # Wait for playback to finish
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)
        except Exception as e:
            print(f"Error speaking text: {e}")

    # Run the audio playback in a separate thread
    threading.Thread(target=play_audio, daemon=True).start()
