from PyQt4 import QtGui
from PyQt4.QtCore import Qt
import sys
from time import sleep

instructions = []
tape_positions = [0, 1, 2, 3, 4, 5, 6, 7]    # positions of the tape, which will change depending on left or right



class StartWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        super(StartWindow, self).__init__(parent)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        self.setWindowTitle("Tape")  # title of the application
        self.setGeometry(700, 400, 455, 100)
        self.tape = ["1", "1", "1", "#", "#", "#", "#", "#"]
        self.loadInstructions("instructions.txt")

    def loadInstructions(self, filename):
        try:
            file = open(filename, "r")      # opens the file specified in the method parameters
        except IOError:     # catches an error is the file does not exist
            print "Instructions file does not exist"
            return      # early return if network population fails
        for line in file:
            instructions.append(map(str, line.strip().split(',')))       # fills the network 2d list with comma seperated values using the split method

        self.network_populated = True       # the network will then get set to populated
        file.close

        print instructions

        self.drawTape()

    def drawTape(self):
        self.lblTape0 = QtGui.QLabel("#", self)
        self.lblTape0.resize(50, 50)
        self.lblTape0.setStyleSheet("border: 7px solid #ff0000;")     # css sheet
        self.lblTape0.move(10, 40)
        self.lblTape0.setAlignment(Qt.AlignCenter)
        self.lblTape0.setFont(QtGui.QFont('Times', 30))

        self.lblTape1 = QtGui.QLabel("#", self)
        self.lblTape1.resize(50, 50)
        self.lblTape1.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape1.move(65, 40)
        self.lblTape1.setAlignment(Qt.AlignCenter)
        self.lblTape1.setFont(QtGui.QFont('Times', 30))

        self.lblTape2 = QtGui.QLabel("#", self)
        self.lblTape2.resize(50, 50)
        self.lblTape2.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape2.move(120, 40)
        self.lblTape2.setAlignment(Qt.AlignCenter)
        self.lblTape2.setFont(QtGui.QFont('Times', 30))

        self.lblTape3 = QtGui.QLabel("#", self)
        self.lblTape3.resize(50, 50)
        self.lblTape3.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape3.move(175, 40)
        self.lblTape3.setAlignment(Qt.AlignCenter)
        self.lblTape3.setFont(QtGui.QFont('Times', 30))

        self.lblTape4 = QtGui.QLabel("#", self)
        self.lblTape4.resize(50, 50)
        self.lblTape4.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape4.move(230, 40)
        self.lblTape4.setAlignment(Qt.AlignCenter)
        self.lblTape4.setFont(QtGui.QFont('Times', 30))

        self.lblTape5 = QtGui.QLabel("#", self)
        self.lblTape5.resize(50, 50)
        self.lblTape5.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape5.move(285, 40)
        self.lblTape5.setAlignment(Qt.AlignCenter)
        self.lblTape5.setFont(QtGui.QFont('Times', 30))

        self.lblTape6 = QtGui.QLabel("#", self)
        self.lblTape6.resize(50, 50)
        self.lblTape6.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape6.move(340, 40)
        self.lblTape6.setAlignment(Qt.AlignCenter)
        self.lblTape6.setFont(QtGui.QFont('Times', 30))

        self.lblTape7 = QtGui.QLabel("#", self)
        self.lblTape7.resize(50, 50)
        self.lblTape7.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape7.move(395, 40)
        self.lblTape7.setAlignment(Qt.AlignCenter)
        self.lblTape7.setFont(QtGui.QFont('Times', 30))

        self.btnLeft = QtGui.QPushButton("L", self)
        self.btnLeft.clicked.connect(self.moveLeft)
        self.btnLeft.resize(self.btnLeft.sizeHint())  # resizes to what PyQt reccomends, could also use minimumsizehint

        self.btnRight = QtGui.QPushButton("R", self)
        self.btnRight.clicked.connect(self.moveRight)
        self.btnRight.resize(self.btnRight.sizeHint())  # resizes to what PyQt reccomends, could also use minimumsizehint
        self.btnRight.move(380, 0)

        self.btnRun = QtGui.QPushButton("Run", self)
        self.btnRun.clicked.connect(self.runMachine)
        self.btnRun.resize(self.btnRun.sizeHint())
        self.btnRun.move(300, 0)

        self.fillTape()

    def fillTape(self):

        if len(self.tape) >= 8:
            self.lblTape0.setText(str(self.tape[0]))
            self.lblTape1.setText(str(self.tape[1]))
            self.lblTape2.setText(str(self.tape[2]))
            self.lblTape3.setText(str(self.tape[3]))
            self.lblTape4.setText(str(self.tape[4]))
            self.lblTape5.setText(str(self.tape[5]))
            self.lblTape6.setText(str(self.tape[6]))
            self.lblTape7.setText(str(self.tape[7]))
        elif len(self.tape) >= 7:
            self.lblTape0.setText(str(self.tape[0]))
            self.lblTape1.setText(str(self.tape[1]))
            self.lblTape2.setText(str(self.tape[2]))
            self.lblTape3.setText(str(self.tape[3]))
            self.lblTape4.setText(str(self.tape[4]))
            self.lblTape5.setText(str(self.tape[5]))
            self.lblTape6.setText(str(self.tape[6]))
        elif len(self.tape) >= 6:
            self.lblTape0.setText(str(self.tape[0]))
            self.lblTape1.setText(str(self.tape[1]))
            self.lblTape2.setText(str(self.tape[2]))
            self.lblTape3.setText(str(self.tape[3]))
            self.lblTape4.setText(str(self.tape[4]))
            self.lblTape5.setText(str(self.tape[5]))
        elif len(self.tape) >= 5:
            self.lblTape0.setText(str(self.tape[0]))
            self.lblTape1.setText(str(self.tape[1]))
            self.lblTape2.setText(str(self.tape[2]))
            self.lblTape3.setText(str(self.tape[3]))
            self.lblTape4.setText(str(self.tape[4]))
        elif len(self.tape) >= 4:
            self.lblTape0.setText(str(self.tape[0]))
            self.lblTape1.setText(str(self.tape[1]))
            self.lblTape2.setText(str(self.tape[2]))
            self.lblTape3.setText(str(self.tape[3]))
        elif len(self.tape) >= 3:
            self.lblTape0.setText(str(self.tape[0]))
            self.lblTape1.setText(str(self.tape[1]))
            self.lblTape2.setText(str(self.tape[2]))
        elif len(self.tape) >= 2:
            self.lblTape0.setText(str(self.tape[0]))
            self.lblTape1.setText(str(self.tape[1]))
        elif len(self.tape) >= 1:
            self.lblTape0.setText(str(self.tape[0]))

    def moveRight(self):
        print "Right"

        for index in range(len(tape_positions)):
            tape_positions[index] -= 1

        if tape_positions[0] == -1:
            for index in range(len(tape_positions)):
                tape_positions[index] += 1

        if tape_positions[0] != -1:
            self.tape = ['#'] + self.tape
            self.btnLeft.setEnabled(True)
            self.lblTape0.setText(str(self.tape[tape_positions[0]]))
            self.lblTape1.setText(str(self.tape[tape_positions[1]]))
            self.lblTape2.setText(str(self.tape[tape_positions[2]]))
            self.lblTape3.setText(str(self.tape[tape_positions[3]]))
            self.lblTape4.setText(str(self.tape[tape_positions[4]]))
            self.lblTape5.setText(str(self.tape[tape_positions[5]]))
            self.lblTape6.setText(str(self.tape[tape_positions[6]]))
            self.lblTape7.setText(str(self.tape[tape_positions[7]]))

    def moveLeft(self):
        print "Left"

        for index in range(len(tape_positions)):
            tape_positions[index] += 1

        if tape_positions[7] > len(self.tape):
            for index in range(len(tape_positions)):
                tape_positions[index] -= 1

        if tape_positions[7] <= len(self.tape):
            self.btnRight.setEnabled(True)
            self.tape.append("#")
            self.lblTape0.setText(str(self.tape[tape_positions[0]]))
            self.lblTape1.setText(str(self.tape[tape_positions[1]]))
            self.lblTape2.setText(str(self.tape[tape_positions[2]]))
            self.lblTape3.setText(str(self.tape[tape_positions[3]]))
            self.lblTape4.setText(str(self.tape[tape_positions[4]]))
            self.lblTape5.setText(str(self.tape[tape_positions[5]]))
            self.lblTape6.setText(str(self.tape[tape_positions[6]]))
            self.lblTape7.setText(str(self.tape[tape_positions[7]]))

    def runMachine(self):

        tape_position = 0
        current_instruction_set = []
        instructionfound = False
        current_state = "A" # start state

        while current_state != "H":
            app.processEvents()
            current_symbol = self.tape[tape_position]
            for index in range(len(instructions)):  # goes through the instructions
                if instructions[index][0] == current_state and instructions[index][1] == current_symbol:  # if both the symbol and state match the instruction
                    current_instruction_set = instructions[index]  # make a copy of that instruction to be executed
                    instructionfound = True

            if instructionfound == True:
                print "Current Tape: " + str(self.tape)
                print "Scanned Symbol: " + str(current_symbol)
                print "Scanned State: " + str(current_state)

                self.tape[tape_position] = current_instruction_set[3]  # assigns new value to the tape
                print "New Value on Square: " + str(self.tape[tape_position])
                current_state = current_instruction_set[4]  # assigns new state to machine
                print "New State of Machine: " + str(current_state)

                if current_instruction_set[2] == "R" and current_instruction_set[4] != "H":
                    tape_position += 1

                    if tape_position == len(self.tape):
                        self.tape.append('#')

                    self.moveLeft()

                    print "Moving Right"
                    print "--------------------------------------"
                    print ""

                elif current_instruction_set[2] == "L" and current_instruction_set[4] != "H":
                    tape_position -= 1

                    if tape_position == -1:
                        self.tape = ['#'] + self.tape
                        tape_position = 0

                    self.moveRight()

                    print "Moving Left"
                    print "--------------------------------------"
                    print ""

                    if tape_position < 0 or tape_position > len(self.tape):

                        print ""
                        print "<--- End of Tape --->"
                        print "Final Tape: " + str(self.tape)
        else:

            print ""
            print "<--- End of Tape --->"
            print "Final Tape: " + str(self.tape)

class HomeWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        super(HomeWindow, self).__init__()
        self.setGeometry(700, 400, 150, 300)
        self.setWindowTitle("Home")  # title of the application
        self.home()

    def home(self):

        btnQuit = QtGui.QPushButton("Quit", self)
        btnQuit.clicked.connect(self.close_application)  # exits instance of Qcore applicaton
        btnQuit.resize(btnQuit.sizeHint())  # resizes to what PyQt reccomends, could also use minimumsizehint
        btnQuit.move(35, 50)

        btnStart = QtGui.QPushButton("Start Machine", self)
        btnStart.clicked.connect(self.onBtnStartClicked)
        btnStart.resize(btnQuit.sizeHint())
        btnStart.move (35, 20)
        self.dialog = StartWindow(self)

        self.show()

    def close_application(self):
        userinput = QtGui.QMessageBox.question(self, 'Quit', "Are you sure you wish to exit?",
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if userinput == QtGui.QMessageBox.Yes:
            print "EXITING"
            sys.exit()
        else:
            pass

    def onBtnStartClicked(self):
        self.dialog.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)  # argv allows you to pass arguments through the cmd when running
                                        # defined app here
    GUI = HomeWindow()
    sys.exit(app.exec_())