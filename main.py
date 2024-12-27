import customtkinter as ctk
from utils.intro_txt import intro_txt, process_command
from utils.voice_api import txt_to_speech
from audio_files.audio_script import play_audio, show_audios
import os
from tkinter import Listbox

# Mapping of displayed names to voice IDs
voice_mapping = {
    "Aria": "9BWtsMINqrJLrRac0k9x",
    "Saarah": "EXAVITQu4vr4xnSDxMaL",
    "Roger": "CwhRBWXzGAHq8TQ4Fs17",
    "Charlie": "IKne3meq5aSn9XLyUdCD",
    "George": "JBFqnCBsd6RMkjVDRZzb"
}


def handle_enter(event=None):
    """Handles Enter key press to process the last command in the textbox."""
    command = input_text.get("end-2l linestart", "end-1c").strip()  # Get the last line
    process_command(command, input_text)  # Process the command


def on_convert_button_click():
    """Handles the Convert button click to process text-to-speech."""
    user_command = input_text.get("1.0", "end-1c").strip()  # Get all text from the textbox
    selected_voice = voices_combobox.get()  # Get the selected voice name
    voice_id = voice_mapping.get(selected_voice, "JBFqnCBsd6RMkjVDRZzb")  # Default voice ID if none selected

    # Convert text to speech and save the audio file
    saved_file_path = txt_to_speech(user_command, input_text, voice_id)

    if saved_file_path:
        play_button.saved_file_path = saved_file_path  # Save the file path for playback


def play_audio_from_button():
    """Plays the audio file saved by the Convert button."""
    saved_file_path = getattr(play_button, 'saved_file_path', None)
    if saved_file_path:
        play_audio(saved_file_path)
    else:
        print("No audio file selected to play.")


def show_media_screen():
    """Switches to the Media screen."""
    clear_frame(main_frame)

    # Media frame
    media_frame = ctk.CTkFrame(main_frame, fg_color="#F0F0F0", corner_radius=10)
    media_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Media title
    media_title = ctk.CTkLabel(
        media_frame, text="Media Files", font=("Helvetica", 24, "bold"), text_color="black"
    )
    media_title.pack(pady=10)

    # Scrollable frame for media files
    scrollable_media_frame = ctk.CTkScrollableFrame(media_frame, width=700, height=400, corner_radius=10)
    scrollable_media_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Retrieve and list audio files
    media_folder = "audio_files"
    media_files = [file for file in os.listdir(media_folder) if file.endswith(".mp3")]
    file_checkboxes = {}

    for file in media_files:
        # Checkbox-like row for each file
        checkbox_var = ctk.BooleanVar()
        checkbox = ctk.CTkCheckBox(
            scrollable_media_frame,
            text=file,
            variable=checkbox_var,
            font=("Helvetica", 14)
        )
        checkbox.pack(anchor="w", padx=10, pady=5)
        file_checkboxes[file] = checkbox_var

    # Action buttons
    def play_selected_media():
        """Plays the first selected media file."""
        for file, var in file_checkboxes.items():
            if var.get():
                play_audio(os.path.join(media_folder, file))
                return
        print("No media file selected to play.")

    def delete_selected_media():
        """Deletes selected media files."""
        import pygame
        pygame.mixer.music.stop()  # Stop any playing audio to release the file lock
        for file, var in list(file_checkboxes.items()):
            if var.get():
                try:
                    os.remove(os.path.join(media_folder, file))
                    file_checkboxes.pop(file).set(0)  # Remove entry
                except PermissionError as e:
                    print(f"Cannot delete {file}: {e}")
        show_media_screen()  # Refresh the media screen

    action_buttons_frame = ctk.CTkFrame(media_frame, height=150, width=50, fg_color='white')
    action_buttons_frame.pack(pady=10)

    play_button = ctk.CTkButton(
        action_buttons_frame,
        text="Play Selected",
        command=play_selected_media,
        fg_color="blue",
        hover_color="darkblue",
        corner_radius=15,
        font=("Helvetica", 18),
        cursor="hand2"
    )
    play_button.pack(side="left", padx=10)

    delete_button = ctk.CTkButton(
        action_buttons_frame,
        text="Delete Selected",
        command=delete_selected_media,
        fg_color="red",
        hover_color="darkred",
        corner_radius=15,
        font=("Helvetica", 18),
        cursor="hand2"
    )
    delete_button.pack(side="left", padx=10)

    # Back button to return to main screen
    back_button = ctk.CTkButton(
        action_buttons_frame,
        text="Home",
        command=show_main_screen,
        fg_color="orange",
        hover_color="darkorange",
        corner_radius=15,
        font=("Helvetica", 18),
        cursor="hand2"
    )
    back_button.pack(side='left', padx=10,pady=10)

def show_main_screen():
    """Switches back to the main screen."""
    clear_frame(main_frame)
    initialize_main_content()


def clear_frame(frame):
    """Clears all widgets from a frame."""
    for widget in frame.winfo_children():
        widget.destroy()


def initialize_main_content():
    """Initializes the main screen content."""
    # Grid configuration for main_frame
    main_frame.grid_columnconfigure((0, 1), weight=1)
    main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

    # Sidebar for buttons
    sidebar_frame = ctk.CTkFrame(main_frame, fg_color="#D3D3D3", corner_radius=10)
    sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew", padx=(0, 10), pady=10)

    # Buttons in sidebar
    convert_button = ctk.CTkButton(
        sidebar_frame,
        text="Convert",
        command=on_convert_button_click,
        font=("Helvetica", 20),
        width=120,
        height=50,
        fg_color="green",
        hover_color="darkgreen",
        corner_radius=15,
        cursor="hand2"
    )
    convert_button.pack(pady=10, padx=10)

    # ComboBox for voice selection
    global voices_combobox  # Ensure voices_combobox is accessible globally
    voices_combobox = ctk.CTkComboBox(
        sidebar_frame,
        values=list(voice_mapping.keys()),  # Use the names from the voice_mapping
        width=120,
        height=50,
        border_color='#DAA520',
        corner_radius=15,
        fg_color="gray",
        button_color="#DAA520",
        button_hover_color="#FFA500",
    )
    voices_combobox.pack(pady=10, padx=10)

    # Play button
    global play_button  # Ensure play_button is accessible globally
    play_button = ctk.CTkButton(
        sidebar_frame,
        text="▶ Play",
        width=120,
        height=50,
        command=play_audio_from_button,
        fg_color="blue",
        hover_color="darkblue",
        corner_radius=15,
        font=("Helvetica", 20),
        cursor="hand2"
    )
    play_button.pack(pady=10, padx=10)
    play_button.saved_file_path = None  # Initialize with no file path

    # Media button to switch to Media screen
    media_button = ctk.CTkButton(
        sidebar_frame,
        text="Medias",
        width=120,
        height=50,
        command=show_media_screen,
        fg_color="red",
        hover_color="darkred",
        corner_radius=15,
        font=("Helvetica", 20),
        cursor="hand2"
    )
    media_button.pack(pady=10, padx=10)
# download btn
    download_button = ctk.CTkButton(sidebar_frame, text="Download",
                                    width=120, height=50,
                                    fg_color="orange", hover_color="darkorange",
                                    corner_radius=15, font=("Helvetica", 20),
                                    cursor="hand2")
    download_button.pack(pady=10, padx=10)
    #new btn
    new_project_button = ctk.CTkButton(sidebar_frame, text="New",
                                       width=120, height=50,
                                       fg_color="purple", hover_color="darkpurple",
                                       corner_radius=15, font=("Helvetica", 20),
                                       cursor="hand2")
    new_project_button.pack(pady=10, padx=10)
    #share btn
    share_button = ctk.CTkButton(sidebar_frame, text="Share",
                                 width=120, height=50,
                                 fg_color="#00CED1", hover_color="#20B2AA",
                                 corner_radius=15, font=("Helvetica", 20),
                                 cursor="hand2")
    share_button.pack(pady=10, padx=10)
    # Main Textbox
    global input_text  # Ensure input_text is accessible globally
    input_text = ctk.CTkTextbox(main_frame, width=400, height=400,
                                corner_radius=10, font=("Helvetica", 18))
    input_text.grid(row=0, column=1, rowspan=6, sticky="nsew", padx=10, pady=10)
    input_text.bind("<Return>", handle_enter)

    # Display intro text
    intro_message = """Welcome to Ready My Voice...
    Type 'help' for a quick tour of the app
    Type 'exit' to close the app\n or start typing to begin...\n"""
    app.after(100, lambda: intro_txt(intro_message, input_text))
    input_text.after(15000, lambda: input_text.delete("1.0", "end"))  # Clear after 15 seconds


# Initialize the main window
app = ctk.CTk()
app.geometry("800x600")
app.resizable(width=False, height=False)
app.title("Ready My Voice")

# Main frame for dynamic content
main_frame = ctk.CTkFrame(app, fg_color="#F0F0F0", corner_radius=10)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Load the main screen
initialize_main_content()

# Run the app
if __name__ == '__main__':
    app.mainloop()
