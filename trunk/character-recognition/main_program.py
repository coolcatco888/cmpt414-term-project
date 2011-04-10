# Main entry point into program

__author__="cley"
__date__ ="$9-Apr-2011 5:07:40 PM$"

import gtk

class  MainProgramGTK:

    def __init__(self):
        filename = "main_menu.glade"
        builder = gtk.Builder()
        builder.add_from_file(filename)
        signals = { "on_window_destroy" : gtk.main_quit }
        builder.connect_signals(signals)

if __name__ == "__main__":
    app = MainProgramGTK()
    gtk.main()
