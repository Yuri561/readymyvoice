import customtkinter as ctk
from utils.intro_txt import intro_txt, process_command
from utils.voice_api import txt_to_speech
from audio_files.audio_script import play_audio

# Mapping of displayed names to voice IDs
#------- Done by defju() ---------#
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
        # Save the file path as an attribute of the Play button
        play_button.saved_file_path = saved_file_path

def play_audio_from_button():
    # Retrieve the file path from the button's attribute
    saved_file_path = getattr(play_button, 'saved_file_path', None)
    if saved_file_path:
        play_audio(saved_file_path)
    else:
        print("No audio file selected to play.")

# Initialize the main window
app = ctk.CTk()
app.geometry("800x600")
app.resizable(width=False, height=False)
app.title("Ready My Voice")

# Title section
title_frame = ctk.CTkFrame(app, height=100, fg_color='orange', corner_radius=10)
title_frame.pack(fill='x', padx=10, pady=5)

title_label = ctk.CTkLabel(title_frame, text='Ready My Voice',
                           font=("Arial", 30, "bold"), text_color="white")
title_label.pack(side="left", padx=20)

# Main layout
main_frame = ctk.CTkFrame(app, fg_color='#F0F0F0', corner_radius=10)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

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

# Create Play button with default saved_file_path
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
play_button.saved_file_path = None

download_button = ctk.CTkButton(sidebar_frame, text="Download",
                                width=120, height=50,
                                fg_color="orange", hover_color="darkorange",
                                corner_radius=15, font=("Helvetica", 20),
                                cursor="hand2")
download_button.pack(pady=10, padx=10)

media_button = ctk.CTkButton(sidebar_frame, text="Medias",
                             width=120, height=50,
                             fg_color="red", hover_color="darkred",
                             corner_radius=15, font=("Helvetica", 20),
                             cursor="hand2")
media_button.pack(pady=10, padx=10)

new_project_button = ctk.CTkButton(sidebar_frame, text="New",
                                   width=120, height=50,
                                   fg_color="purple", hover_color="darkpurple",
                                   corner_radius=15, font=("Helvetica", 20),
                                   cursor="hand2")
new_project_button.pack(pady=10, padx=10)

share_button = ctk.CTkButton(sidebar_frame, text="Share",
                             width=120, height=50,
                             fg_color="#00CED1", hover_color="#20B2AA",
                             corner_radius=15, font=("Helvetica", 20),
                             cursor="hand2")
share_button.pack(pady=10, padx=10)

# Text box for displaying output and user input
input_text = ctk.CTkTextbox(main_frame, width=400, height=400,
                            corner_radius=10, font=("Helvetica", 18))
input_text.grid(row=0, column=1, rowspan=6, sticky="nsew", padx=10, pady=10)
input_text.bind("<Return>", handle_enter)

intro_message = """Welcome to Ready My Voice...
Type 'help' for a quick tour of the app
Type 'exit' to close the app\n or start typing to begin...\n
This message will self-destruct in 3 seconds"""

# Display intro text and schedule clearing
app.after(100, lambda: intro_txt(intro_message, input_text))
input_text.after(15000, lambda: input_text.delete("1.0", "end"))  # Clear after 15 seconds

# Run the app
if __name__ == '__main__':
    app.mainloop()
