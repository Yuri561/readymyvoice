import time

def intro_txt(text, textbox):
    """Displays animated text in a textbox."""
    for character in text:
        textbox.insert("end", character)  # Insert character into the textbox
        textbox.update()  # Update the UI to reflect changes
        time.sleep(0.08)  # Delay between each character
    textbox.insert("end", "\n")  # Add a newline after the text

#-------------code done by defJu--------------------#
def process_command(command, textbox):
    """Processes user input commands with animation."""
    command = command.lower().strip()
    textbox.insert("end", "\n")  # Insert an extra newline for spacing
    textbox.update()
    if command == "help":
        # Display help information with animation
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
        intro_txt(help_message, textbox)
    elif command == "exit":
        # Display exit message with animation
        intro_txt("Exiting the application...\n", textbox)
        textbox.after(1000, textbox.quit)
    else:
        # Display invalid command feedback with animation
        intro_txt(f"Unknown command: {command}\n", textbox)
