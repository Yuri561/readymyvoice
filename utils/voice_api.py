from elevenlabs.client import ElevenLabs
import os
from datetime import datetime
from tkinter import messagebox

client = ElevenLabs(
    api_key='sk_a80e88c6d33e269b27c55e21c709e7cf67c36a8277d67fc6'
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

