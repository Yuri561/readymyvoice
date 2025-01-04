import customtkinter as ctk
from tkinter import filedialog
from utils.download_file import download_file
from utils.intro_txt import intro_txt, process_command
from utils.voice_api import txt_to_speech, speak_text
from audio_files.audio_script import play_audio
import os
import textwrap

# Constants
APP_TITLE = "Ready My Voice"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SIDEBAR_BUTTON_DIMENSIONS = {"width": 120, "height": 50}
FONT_LARGE = ("Helvetica", 20)
FONT_MEDIUM = ("Helvetica", 18)

# Voice mapping
VOICE_MAPPING = {
    "Laura": "FGY2WhTYpPnrIDTdsKH5",
    "Saarah": "EXAVITQu4vr4xnSDxMaL",
    "Roger": "CwhRBWXzGAHq8TQ4Fs17",
    "Charlie": "IKne3meq5aSn9XLyUdCD",
    "George": "JBFqnCBsd6RMkjVDRZzb"
}

# Initialize main window
app = ctk.CTk()
app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
app.resizable(width=False, height=False)
app.title(APP_TITLE)

# Global variables for shared components
main_frame = None
input_text = None
voices_combobox = None
play_button = None


def handle_enter(event=None):
    """Process the last entered command."""
    command = input_text.get("end-2l linestart", "end-1c").strip()
    process_command(command, input_text)


def on_convert_button_click():
    """Handle text-to-speech conversion."""
    user_command = input_text.get("1.0", "end-1c").strip()
    selected_voice = voices_combobox.get()
    voice_id = VOICE_MAPPING.get(selected_voice, None)

    # Convert text to speech
    saved_file_path = txt_to_speech(user_command, input_text, voice_id)

    if saved_file_path:
        play_button.saved_file_path = saved_file_path  # Save path for playback


def play_audio_from_button():
    """Play the saved audio file."""
    saved_file_path = getattr(play_button, 'saved_file_path', None)
    if saved_file_path:
        play_audio(saved_file_path)
    else:
        print("No audio file selected to play.")


def clear_frame(frame):
    """Remove all widgets from a frame."""
    for widget in frame.winfo_children():
        widget.destroy()


def initialize_sidebar(parent_frame):
    """Create and initialize the sidebar with buttons."""
    sidebar_frame = ctk.CTkFrame(parent_frame, fg_color="transparent", corner_radius=10)
    sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew", padx=(0, 10), pady=10)

    # Sidebar Buttons
    button_configs = [
        {"text": "Convert", "command": on_convert_button_click, "color": "#FFC107"},
        {"text": "▶ Play", "command": play_audio_from_button, "color": "#FFC107"},
        {"text": "Medias", "command": show_media_screen, "color": "#FFC107"},
        {"text": "Download", "command": lambda: download_file(play_button.saved_file_path, filedialog, input_text), "color": "#FFC107"},
        {"text": "New", "command": lambda: initialize_main_screen(), "color": "#FFC107"},
        {"text": "Exit", "command": lambda: app.destroy(), "color": "#FFC107"}
    ]

    global voices_combobox, play_button
    for config in button_configs:
        button = ctk.CTkButton(
            sidebar_frame,
            text=config["text"],
            command=config["command"],
            font=FONT_LARGE,
            fg_color=config["color"],
            hover_color=config["color"],
            text_color='black',
            corner_radius=15,
            cursor="hand2",
            **SIDEBAR_BUTTON_DIMENSIONS
        )
        button.pack(pady=10, padx=10)

    # Add Voice Selection Combobox
    voices_combobox = ctk.CTkComboBox(
        sidebar_frame,
        values=list(VOICE_MAPPING.keys()),
        width=SIDEBAR_BUTTON_DIMENSIONS["width"],
        height=SIDEBAR_BUTTON_DIMENSIONS["height"],
        border_color='#DAA520',
        corner_radius=15,
        fg_color="gray",
        button_color="#DAA520",
        button_hover_color="#FFA500",
    )
    voices_combobox.pack(pady=10, padx=10)

    # Play button
    # play_button = ctk.CTkButton(
    #     sidebar_frame,
    #     text="▶ Play",
    #     command=play_audio_from_button,
    #     font=FONT_LARGE,
    #     fg_color="blue",
    #     hover_color="darkblue",
    #     corner_radius=15,
    #     cursor="hand2",
    #     **SIDEBAR_BUTTON_DIMENSIONS
    # )
    # play_button.pack(pady=10, padx=10)
    # play_button.saved_file_path = None


def initialize_main_screen():
    """Set up the main application screen."""
    clear_frame(main_frame)

    # Configure layout
    main_frame.grid_columnconfigure((0, 1), weight=1)
    main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

    # Initialize sidebar
    initialize_sidebar(main_frame)

    # Initialize main text area
    global input_text
    input_text = ctk.CTkTextbox(
        main_frame,
        width=400,
        height=400,
        corner_radius=10,
        font=FONT_MEDIUM
    )
    input_text.grid(row=0, column=1, rowspan=6, sticky="nsew", padx=10, pady=10)
    input_text.bind("<Return>", handle_enter)

    # Intro message
    intro_message = textwrap.dedent("""\
        Welcome to Ready My Voice – your personalized voiceover assistant!
        - Type 'help' for a quick tour.
        - Type 'exit' to close the app.
        - Type 'home' to return to this menu.
        - Type 'clear' to start fresh.
    """)
    app.after(100, lambda: intro_txt(intro_message, input_text))
    app.after(100, lambda: speak_text(intro_message))
    input_text.after(30000, lambda: input_text.delete("1.0", "end"))


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

    # Back button to return to the main screen
    back_button = ctk.CTkButton(
        action_buttons_frame,
        text="Home",
        command=initialize_main_screen,
        fg_color="orange",
        hover_color="darkorange",
        corner_radius=15,
        font=("Helvetica", 18),
        cursor="hand2"
    )
    back_button.pack(side="left", padx=10, pady=10)

# Main frame for dynamic content
main_frame = ctk.CTkFrame(app, fg_color="#0A3D62", corner_radius=10)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Load main screen
initialize_main_screen()

# Run the app
if __name__ == "__main__":
    app.mainloop()