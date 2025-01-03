import time
from tkinter import messagebox
from .voice_api import speak_text

# Consolidated help message
help_message = (
    "\nQuick Start Guide:\n"
    "1. Convert: Converts your text to voiceover.\n"
    "2. Voices: Choose a specific voice.\n"
    "3. Play: Hear a preview.\n"
    "4. Download: Save your voiceover as audio.\n"
    "5. Medias: Access saved media.\n"
    "6. New: Start a new project.\n"
    "7. Share: Share your voiceover.\n"
)
ai_message = (
    "Welcome to the Quick Start Guide! Here's how to get started: Convert your text into a voiceover, "
    "pick from a variety of voices, listen to a preview, and download your audio. Access your saved media "
    "anytime, start a new project with ease, and share your voiceovers effortlessly. Ready to bring your words to life? Let’s go."
)

def intro_txt(text, textbox):
    """Displays animated text in a textbox."""
    for character in text:
        textbox.insert("end", character)  # Insert character into the textbox
        textbox.update()  # Update the UI to reflect changes
        time.sleep(0.05)  # Reduced delay for faster text display
    textbox.insert("end", "\n")  # Ensure a newline after the text

def process_command(command, textbox):
    """Processes user input commands with animation."""
    print(f"Received command: {repr(command)}")  # Debugging: Print the command for verification
    command = command.lower().strip()

    # Ensure spacing before adding new command output
    if not textbox.get("1.0", "end-1c").strip():
        textbox.insert("end", "\n")

    if command == "help":
        # Display help information with animation
        intro_txt(help_message, textbox)
        speak_text(ai_message)  # Use speak_text to provide auditory feedback
        intro_txt("This message will self-destruct in 15 seconds...\n", textbox)
        textbox.after(15000, lambda: textbox.delete("1.0", "end"))

    elif command == "home":
        # Display the home message
        home_message = (
            "Welcome to Ready My Voice...\n"
            "Type 'help' for a quick tour of the app\n"
            "Type 'exit' to close the app\n"
            "or start typing to begin...\n"
            "This message will self-destruct in 3 seconds\n"
        )
        intro_txt(home_message, textbox)
        # speak_text(home_message)
        textbox.after(3000, lambda: textbox.delete("1.0", "end"))

    elif command == "exit":
        # Display exit message with animation
        intro_txt("Exiting the application...\n", textbox)
        textbox.after(1000, textbox.quit)

    elif command == "clear":
        # Clear the textbox content
        textbox.delete("1.0", "end")

    else:
        # Display invalid command feedback with a messagebox
        error_message = f"Unknown command: {command}"
        messagebox.showerror(title="Error", message=error_message)
        intro_txt(f"Error: {error_message}\n", textbox)
