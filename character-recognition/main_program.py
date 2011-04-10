# Main entry point into program

__author__="cley"
__date__ ="$9-Apr-2011 5:07:40 PM$"

import gtk

TEXT_LOAD = "Load"
TEXT_SAVE = "Save"

class  MainProgramGTK:

    builder = 0

    def __init__(self):

        # Load GUI from glade xml
        filename = "main_menu.glade"
        builder = gtk.Builder()
        builder.add_from_file(filename)

        # Bind functions to GUI
        signals = {
            "on_window_destroy" : gtk.main_quit,
            "on_about_show" : self.about_show,
            "on_load_network" : self.load_network
        }
        builder.connect_signals(signals)
        self.builder = builder

        self.window = self.builder.get_object("mainWindow")
        self.window.set_title("OCR Neural Network")


    def about_show(self, widget):
        self.window = self.builder.get_object("aboutdialog")
	response = self.window.run()

        if response == gtk.RESPONSE_DELETE_EVENT or response == gtk.RESPONSE_CANCEL:
            self.window.hide()

    def load_network(self, widget):
        self.window = self.builder.get_object("filechooserdialog")
        self.window.set_title("Choose Neural Network...")
        response = self.window.run()

        if response == gtk.RESPONSE_DELETE_EVENT or response == gtk.RESPONSE_CANCEL:
            self.window.hide()


if __name__ == "__main__":
    app = MainProgramGTK()
    gtk.main()
