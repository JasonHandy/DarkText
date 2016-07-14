import tkinter as tk
import tkinter.scrolledtext as st
import tkinter.filedialog as dialog
import tkinter.messagebox as message
import os


class DarkText:
    def __init__(self, parent):
        # Create parent variable within class
        self.parent = parent
        self.save_location = ''

        # Create textfield and specify parameters
        self.TextField = st.ScrolledText(self.parent, background='black',
                                         foreground='green',
                                         insertbackground='green',
                                         selectbackground='#818181',
                                         cursor='xterm', wrap='word',
                                         height=60, width=150,
                                         padx=10, pady=10,
                                         undo=True, maxundo=5,
                                         takefocus=True)

        # Set up key bindings
        self.set_key_bindings()

        # Add TextField widget to parent window, make TextField take focus
        self.TextField.pack(fill='both', expand='yes')
        self.TextField.focus_set()

        # Shows help screen at startup without starting window loop
        self.parent.update_idletasks()
        self.show_help()
        self.parent.update_idletasks()

    def set_key_bindings(self, *kwargs):
        self.TextField.bind("<Command-s>", self.save_file)
        self.TextField.bind("<Command-o>", self.open_file)
        self.TextField.bind("<Command-a>", self.select_all)
        self.TextField.bind("<Command-H>", self.show_help)  # CMD+SHIFT+H
        self.TextField.bind("<Command-F>", self.enter_full_screen) # CMD+SHIFT+F
        self.TextField.bind("<Escape>", self.exit_full_screen)

    def save_file(self, *kwargs):
        if self.save_location == '':
            destination = dialog.asksaveasfilename(defaultextension='.txt')
        else:
            destination = self.save_location

        self.parent.update()

        text_string = self.TextField.get(1.0, 'end')  # Selects all text

        try:
            with open(destination, 'w+') as file:  # Truncates file
                file.write(text_string)
                self.save_location = destination
                self.parent.title('DarkText:{!s}'.format(destination))
        except FileNotFoundError:
            self.parent.update()
            message.showinfo("File Not Found!", "The save location could not "
                                                "be found. File unable to be "
                                                "saved!")

    def open_file(self, *kwargs):
        # Set default open location to user's desktop
        user_space = os.path.expanduser('~')
        desktop = os.path.join(user_space, 'Desktop')

        self.parent.update()
        destination = dialog.askopenfilename(initialdir=desktop,
                                             # Add accepted file types here
                                             filetypes=[("Text Files", "TXT"),
                                                        ("Python Files", "PY"),
                                                        ("XML Files", "XML"),
                                                        ("HTML Files", "HTML")])

        # Open file, delete current text, insert new text
        with open(destination, 'r') as file:
            all_text = file.read()
            self.save_location = destination
        self.TextField.delete(1.0, 'end')
        self.TextField.insert('end', all_text)

        self.parent.title('DarkText:{!s}'.format(destination))
        self.parent.update()

    def select_all(self, *kwargs):
        self.TextField.tag_add('sel', 1.0, 'end')

    def show_help(self, *kwargs):
        # Save current text to temporary file
        text_string = self.TextField.get(1.0, 'end')
        with open('tempfile.txt', 'w+') as file:
            file.write(text_string)
        # Show help menu and remove current text
        help_string = """
        Welcome to DarkText. Press RETURN to exit this help menu.
        =========================================================

        Key bindings:

        Command-S:  Save file
        Command-O:  Open file

        Command-A:  Select all text
        Command-C:  Copy selected text
        Command-V:  Paste text from clipboard

        Command-Z:  Undo last action

        Command-Shift-F:    Enter full screen
        Escape:             Exit full screen

        Command-Shift-H:    Show this help screen
        """
        self.TextField.delete(1.0, 'end')
        self.TextField.insert(1.0, help_string)
        self.TextField.bind("<Return>", self.hide_help)
        self.parent.update()

    def hide_help(self, *kwargs):
        # Get text from temporary file and put on screen
        self.TextField.delete(1.0, 'end')
        with open('tempfile.txt', 'r') as file:
            text_string = file.read()
        self.TextField.insert(1.0, text_string)
        self.TextField.unbind("<Return>")
        self.TextField.see('end')

    def enter_full_screen(self, *kwargs):
        root.attributes('-fullscreen', True)

    def exit_full_screen(self, *kwargs):
        root.attributes('-fullscreen', False)

if __name__ == '__main__':
    # Create window and add title
    root = tk.Tk()
    root.title('DarkText: New File')

    # Create DarkText object, and start root mainloop
    DarkText(root)

    # Bring application window to top at creation
    root.attributes("-topmost", True)
    root.attributes("-topmost", False)  # Make sure app isn't always top window
    
    root.mainloop()
