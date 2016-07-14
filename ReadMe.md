#DarkText

A featherweight, distraction-free text editor for OS X.

###What is DarkText?

DarkText is a bare-bones text editor, permanently configured in dark mode. Many
text editors I used previously, such as TextEdit, or TextWrangler, lacked a true
dark mode option. Additionally, they often felt bloated with needless options,
especially when all most people want out of a text editor is the ability to put
words on a screen. 

DarkText fills this niche by providing only the most basic keyboard commands in
a traditional (some may say cliché) green-on-black format.

###How do I run DarkText?

DarkText is written in Python 3.5.2, mainly using the `tkinter` module included
within the standard library. This means that, if you want to run DarkText from
the source files, you'll need to download the latest version of Python 3 [here]
(https://www.python.org/downloads/).

Alternatively, you can simply download the `DarkTextApp.ZIP` file, unzip it, and
place it in your dock. There is currently no Windows `.EXE` file available, but
an intrepid Windows user *could* build a Windows version from the source files.

Upon attempting to open `DarkText.app`, your system may refuse to open a program
from an unauthorized developer. To work around this, simply right-click on the
application, and select open from the drop-down menu.

###How does DarkText work?
 
DarkText works by creating a border-less windowed application with green-on-black
text. All file save operations output the content of the screen to a text file,
so use DarkText for programming at your own risk. Only one file remains open at
a time, to limit distractions. A help menu is available within the app so you
won't have to leave full screen mode to find out how to do something.

###What features does DarkText have?

DarkText features basic keyboard commands for operations such as saving files,
opening files, copying text, selecting text, and a few more. While in the app,
press `Command-Shift-H` to see the help screen detailing all keyboard commands.

That's it! DarkText is without syntax highlighting, find+replace, or any other
fancy text editing feature. It is designed for spur-of-the-moment drafts, and
nothing else.

Happy typing!
