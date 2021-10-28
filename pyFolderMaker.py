'''

Folder maker application
Input top folders in top box seperates by commas
Input folders to place into top folders in bottom box
Assign destination of folders
Press start

'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

import pyFolderMakerGUIQt

class FolderMakerQt(QDialog, pyFolderMakerGUIQt.Ui_folderMaker):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # assign actions to all buttons
        self.destinationButton.clicked.connect(self.destination_button)
        self.startButton.clicked.connect(self.start_button)

    def destination_button(self):
        global new_folder
        new_folder = QFileDialog.getExistingDirectory(self, "Select Destination for Folders")

    def start_button(self):
        top_folders = self.topFolders.toPlainText()
        top_folders_list = top_folders.split(",")
        bottom_folders = self.bottomFolders.toPlainText()
        bottom_folders_list = bottom_folders.split(",")

        for top_folder in top_folders_list:
            newTopFolder = new_folder + "/" + top_folder
            os.mkdir(newTopFolder)
            for bottom_folder in bottom_folders_list:
                newBotFolder = newTopFolder + "/" + bottom_folder
                os.mkdir(newBotFolder)
                

        print(top_folders_list, bottom_folders_list)
        #for each item in list from top folders box make a folder
        #for each item in list from bottom folders box make a child folder


app = QApplication(sys.argv)
folderMakerQt = FolderMakerQt()
folderMakerQt.show()
app.exec_()