def download_file(filepath, filedialog, textbox):
    import shutil
    import os

    try:
        # Check if file exists
        if not os.path.exists(filepath):
            textbox.insert("end", "Error: File does not exist.\n")
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            initialfile="default_name.mp3",
            filetypes=[("MP3 files", "*.mp3")]
        )
        # Handle user cancelation
        if not filename:
            textbox.insert("end", "Download canceled by user.\n")
            return

        # Copy file to selected destination
        shutil.copy(filepath, filename)

        # Notify success
        textbox.insert("end", f"File downloaded successfully to: {filename}\n")

    except Exception as e:
        # Correctly reference textbox for error messages
        textbox.insert("end", f"An error occurred: {str(e)}\n")
