# Main entry point into program

__author__="cley"
__date__ ="$9-Apr-2011 5:07:40 PM$"

import gtk
import PythonMagick
import pickle
from ocr import OCR

TEXT_LOAD = "Load"
TEXT_SAVE = "Save"

class  MainProgramGTK:

    builder = 0
    testing_image = 0
    network = 0
    training_data = 0

    def __init__(self):

        # Load GUI from glade xml
        filename = "main_menu.glade"
        builder = gtk.Builder()
        builder.add_from_file(filename)

        # Bind functions to GUI
        signals = {
            "on_window_destroy" : gtk.main_quit,
            "on_about_show" : self.about_show,
            "on_load_save_dialog_show" : self.load_save_dialog_show
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

    def load_save_dialog_show(self, widget):
        label = widget.get_label()

        button = self.builder.get_object("loadSaveButton")
        button.set_label(label)
        
        self.window = self.builder.get_object("filechooserdialog")
        dialog = self.window
        self.window.set_title(label + "...")
        
        if label[:4] == "Load":
            dialog.set_action(gtk.FILE_CHOOSER_ACTION_OPEN)
        else:
            dialog.set_action(gtk.FILE_CHOOSER_ACTION_SAVE)

        response = self.window.run()

        

        if response == gtk.RESPONSE_OK:
            file_name = dialog.get_filename()
            if label[:4] == "Load":
                if label[5:] == "Image":
                    self.testing_image = PythonMagick.Image(file_name)
                    self.__display_image(file_name, "testingImage")
                    
                elif label[5:] == "Network":
                    filehandler = open(file_name, 'r')
                    self.network = pickle.load(filehandler)

                elif label[5:] == "Training Data":
                    filehandler = open(file_name, 'r')
                    self.training_data = self.__create_training_image_list(filehandler.read())
                    
            elif label[4:] == "Save":
                
                if label[5:] == "Network":
                    self.__save_training_data(file_name)

                elif label[5:] == "Training Data":
                    self.__save_training_data(file_name)
            self.window.hide()
                    
        elif response == gtk.RESPONSE_DELETE_EVENT or response == gtk.RESPONSE_CANCEL:
            self.window.hide()

    def test_image(self):

        return

    def __create_training_image_list(self, str):
        list = []
        
        for line in str.split():
            list.append(line)

        return list

    def __save_training_data(self, file_name):
        return

    def __save_network(self, file_name):
        return

    def __display_image(self, image_file, object_name):
        image = PythonMagick.Image(image_file)
        image.scale("100x100")
        image.write("test_image.png")

        testing_image_display = self.builder.get_object(object_name)
        testing_image_display.set_from_file("test_image.png")

if __name__ == "__main__":
    app = MainProgramGTK()
    gtk.main()
