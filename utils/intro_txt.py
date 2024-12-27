import time
from tkinter import messagebox


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




def intro_txt(text, textbox):
    """Displays animated text in a textbox."""
    for character in text:
        textbox.insert("end", character)  # Insert character into the textbox
        textbox.update()  # Update the UI to reflect changes
        time.sleep(0.08)  # Delay between each character
    textbox.insert("end", "\n")  # Ensure a newline after the text

def process_command(command, textbox):
    """Processes user input commands with animation."""
    print(f"Received command: {repr(command)}")  # Debugging: Print the command for verification
    command = command.lower().strip()

    # Ensure spacing before adding new command output
    if textbox.get("end-2c", "end-1c") != "\n":
        textbox.insert("end", "\n")

    if command == "help":
        # Display help information with animation
        intro_txt(help_message, textbox)
        intro_txt("This message will self-destruct in 15 seconds...\n", textbox)
        textbox.after(15000, lambda: textbox.delete("1.0", "end"))

    elif command == "home":
        # Display the help message again as home
        intro_txt( """Welcome to Ready My Voice...
Type 'help' for a quick tour of the app
Type 'exit' to close the app\n or start typing to begin...\n
This message will self-destruct in 3 seconds""", textbox)

    elif command == "exit":
        # Display exit message with animation
        intro_txt("Exiting the application...\n", textbox)
        textbox.after(1000, lambda: textbox.quit())

    elif command == "clear":
        # Clear the textbox content
        textbox.delete("1.0", "end")

    else:
        # Display invalid command feedback with a messagebox
        messagebox.showerror(title="Error", message=f"Unknown command: {command}")
