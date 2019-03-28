import sys
from PyQt4 import QtGui, QtCore # GUI, Button Events,

class Window(QtGui.QMainWindow):    # runs every time we create a window object

    def __init__(self): # this is a constructor
        super(Window, self).__init__()
        self.setGeometry(700, 400, 500, 300)    # sets the position and size of the window
        self.setWindowTitle("PyQt") # title of the application
        self.home()

    def home(self):
        btnQuit = QtGui.QPushButton("Quit", self)
        btnQuit.clicked.connect(self.close_application)    # exits instance of Qcore applicaton
        btnQuit.resize(btnQuit.sizeHint())  # resizes to what PyQt reccomends, could also use minimumsizehint
        btnQuit.move(200,150)

        cbWindowSize = QtGui.QCheckBox('Enlarge', self)
        cbWindowSize.stateChanged.connect(self.enlarge_window)
        cbWindowSize.move(200, 100)

        self.pbDownload = QtGui.QProgressBar(self)
        self.pbDownload.setGeometry(150, 250, 250, 20)
        self.btnDownload = QtGui.QPushButton("Download more RAM", self)
        self.btnDownload.resize(self.btnDownload.sizeHint())
        self.btnDownload.move(200, 200)
        self.btnDownload.clicked.connect(self.download_file)

        self.styleChoice = QtGui.QLabel("Win10", self)
        cbStyle = QtGui.QComboBox(self)
        cbStyle.addItem("motif")
        cbStyle.addItem("Windows")
        cbStyle.addItem("cde")
        cbStyle.addItem("Plastique")
        cbStyle.addItem("Cleanlooks")
        cbStyle.move(25, 250)
        self.styleChoice.move(25, 200)
        cbStyle.activated[str].connect(self.style_choice)


        self.show()

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download_file(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.pbDownload.setValue(self.completed)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(700, 400, 1000, 600)
        else:
            self.setGeometry(700, 400, 500, 300)

    def close_application(self):
        userinput = QtGui.QMessageBox.question(self, 'Quit', "Are you sure you wish to exit?",
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if userinput == QtGui.QMessageBox.Yes:
            print "EXITING"
            sys.exit()
        else:
            pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)  # argv allows you to pass arguments through the cmd when running
                                        # defined app here
    GUI = Window()
    sys.exit(app.exec_())