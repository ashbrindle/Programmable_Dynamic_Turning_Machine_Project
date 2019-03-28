from PyQt4 import QtGui
from PyQt4.QtCore import Qt
import sys
from time import sleep

instructions = []
tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]    # positions of the tape, which will change depending on left or right



class StartWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        super(StartWindow, self).__init__(parent)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        self.setWindowTitle("Tape")  # title of the application
        self.setGeometry(700, 400, 570, 250)
        self.tape = []
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

        self.drawWindow()

    def drawWindow(self):
        self.lblInfinite0 = QtGui.QLabel("...", self)
        self.lblInfinite0.resize(50, 50)
        self.lblInfinite0.move(5, 175)
        self.lblInfinite0.setAlignment(Qt.AlignCenter)
        self.lblInfinite0.setFont(QtGui.QFont('Times', 40))

        self.lblTape0 = QtGui.QLabel("#", self)
        self.lblTape0.resize(50, 50)
        self.lblTape0.setStyleSheet("border:3px solid #000000;")     # css sheet
        self.lblTape0.move(52, 190)
        self.lblTape0.setAlignment(Qt.AlignCenter)
        self.lblTape0.setFont(QtGui.QFont('Times', 30))

        self.lblTape1 = QtGui.QLabel("#", self)
        self.lblTape1.resize(50, 50)
        self.lblTape1.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape1.move(107, 190)
        self.lblTape1.setAlignment(Qt.AlignCenter)
        self.lblTape1.setFont(QtGui.QFont('Times', 30))

        self.lblTape2 = QtGui.QLabel("#", self)
        self.lblTape2.resize(50, 50)
        self.lblTape2.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape2.move(167, 190)
        self.lblTape2.setAlignment(Qt.AlignCenter)
        self.lblTape2.setFont(QtGui.QFont('Times', 30))

        self.lblTape3 = QtGui.QLabel("#", self)
        self.lblTape3.resize(50, 50)
        self.lblTape3.setStyleSheet("border: 7px solid #ff0000;")  # css sheet
        self.lblTape3.move(227, 190)
        self.lblTape3.setAlignment(Qt.AlignCenter)
        self.lblTape3.setFont(QtGui.QFont('Times', 30))

        self.lblTape4 = QtGui.QLabel("#", self)
        self.lblTape4.resize(50, 50)
        self.lblTape4.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape4.move(287, 190)
        self.lblTape4.setAlignment(Qt.AlignCenter)
        self.lblTape4.setFont(QtGui.QFont('Times', 30))

        self.lblTape5 = QtGui.QLabel("#", self)
        self.lblTape5.resize(50, 50)
        self.lblTape5.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape5.move(347, 190)
        self.lblTape5.setAlignment(Qt.AlignCenter)
        self.lblTape5.setFont(QtGui.QFont('Times', 30))

        self.lblTape6 = QtGui.QLabel("#", self)
        self.lblTape6.resize(50, 50)
        self.lblTape6.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape6.move(407, 190)
        self.lblTape6.setAlignment(Qt.AlignCenter)
        self.lblTape6.setFont(QtGui.QFont('Times', 30))

        self.lblTape7 = QtGui.QLabel("#", self)
        self.lblTape7.resize(50, 50)
        self.lblTape7.setStyleSheet("border:3px solid #000000;")  # css sheet
        self.lblTape7.move(467, 190)
        self.lblTape7.setAlignment(Qt.AlignCenter)
        self.lblTape7.setFont(QtGui.QFont('Times', 30))

        self.lblInfinite1 = QtGui.QLabel("...", self)
        self.lblInfinite1.resize(50, 50)
        self.lblInfinite1.move(520, 175)
        self.lblInfinite1.setAlignment(Qt.AlignCenter)
        self.lblInfinite1.setFont(QtGui.QFont('Times', 40))

        self.btnRun = QtGui.QPushButton("Run", self)
        self.btnRun.clicked.connect(self.runMachine)
        self.btnRun.resize(100, 60)
        self.btnRun.setStyleSheet("font: bold; color: white; background-color: green; font-size: 36px; border: 3px solid #000000")
        self.btnRun.move(230, 110)

        self.txtTape = QtGui.QLineEdit(self)
        self.txtTape.resize(280, 40)
        self.txtTape.move(80, 50)

        self.btnTape = QtGui.QPushButton("Submit Tape", self)
        self.btnTape.clicked.connect(self.submitTape)
        self.btnTape.resize(100, 40)
        self.btnTape.move(390, 50)

        self.fillTape()

    def fillTape(self):

        if len(self.tape) >= 5:
            self.lblTape3.setText(str(self.tape[0]))
            self.lblTape4.setText(str(self.tape[1]))
            self.lblTape5.setText(str(self.tape[2]))
            self.lblTape6.setText(str(self.tape[3]))
            self.lblTape7.setText(str(self.tape[4]))
        elif len(self.tape) >= 4:
            self.lblTape3.setText(str(self.tape[0]))
            self.lblTape4.setText(str(self.tape[1]))
            self.lblTape5.setText(str(self.tape[2]))
            self.lblTape6.setText(str(self.tape[3]))
        elif len(self.tape) >= 3:
            self.lblTape3.setText(str(self.tape[0]))
            self.lblTape4.setText(str(self.tape[1]))
            self.lblTape5.setText(str(self.tape[2]))
        elif len(self.tape) >= 2:
            self.lblTape3.setText(str(self.tape[0]))
            self.lblTape4.setText(str(self.tape[1]))
        elif len(self.tape) >= 1:
            self.lblTape3.setText(str(self.tape[0]))

    def moveLeft(self):
        print "LEFT"
        for index in range(len(tape_positions)):
            tape_positions[index] -= 1

        if tape_positions[3] == -1:
            self.tape = ["#"] + self.tape
            for index in range(len(tape_positions)):
                tape_positions[index] += 1

        if tape_positions[3] > -1:
            if tape_positions[0] > -1:
                self.lblTape0.setText(str(self.tape[tape_positions[0]]))
            else:
                self.lblTape0.setText("#")
            if tape_positions[1] > -1:
                self.lblTape1.setText(str(self.tape[tape_positions[1]]))
            else:
                self.lblTape1.setText("#")
            if tape_positions[2] > -1:
                self.lblTape2.setText(str(self.tape[tape_positions[2]]))
            else:
                self.lblTape2.setText("#")
            self.lblTape3.setText(str(self.tape[tape_positions[3]]))
            self.lblTape4.setText(str(self.tape[tape_positions[4]]))
            self.lblTape5.setText(str(self.tape[tape_positions[5]]))
            self.lblTape6.setText(str(self.tape[tape_positions[6]]))
            self.lblTape7.setText(str(self.tape[tape_positions[7]]))

    def moveRight(self):
        print "RIGHT"
        for index in range(len(tape_positions)):
            tape_positions[index] += 1

        self.tape.append("#")

        if tape_positions[0] > -1:
            self.lblTape0.setText(str(self.tape[tape_positions[0]]))
        else:
            self.lblTape0.setText("#")
        if tape_positions[1] > -1:
            self.lblTape1.setText(str(self.tape[tape_positions[1]]))
        else:
            self.lblTape1.setText("#")
        if tape_positions[2] > -1:
            self.lblTape2.setText(str(self.tape[tape_positions[2]]))
        else:
            self.lblTape2.setText("#")
        self.lblTape3.setText(str(self.tape[tape_positions[3]]))
        self.lblTape4.setText(str(self.tape[tape_positions[4]]))
        self.lblTape5.setText(str(self.tape[tape_positions[5]]))
        self.lblTape6.setText(str(self.tape[tape_positions[6]]))
        self.lblTape7.setText(str(self.tape[tape_positions[7]]))

    def submitTape(self):

        inputtape = str(self.txtTape.text())
        self.tape = inputtape.split(",")  # splits each value by comma, allowing for multiple entries

        while len(self.tape) < 8:
            self.tape.append("#")

        app.processEvents()

        if self.txtTape.text() == "":
            return

        self.fillTape()
        self.txtTape.setText("")

    def runMachine(self):

        self.btnTape.setEnabled(False)
        app.processEvents()

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
                    self.moveRight()

                    sleep(2)

                    print "Moving Right"
                    print "--------------------------------------"
                    print ""

                elif current_instruction_set[2] == "L" and current_instruction_set[4] != "H":
                    tape_position -= 1

                    if tape_position == -1:
                        tape_position = 0

                    self.moveLeft()

                    sleep(2)

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
                break
        else:

            print ""
            print "<--- End of Tape --->"
            print "Final Tape: " + str(self.tape)

        self.final_tape()
        self.btnTape.setEnabled(True)
        app.processEvents()

    def final_tape(self):

        '''----------------------------
        TO-DO: Remove the end and start values which are blank from the list
        ----------------------------'''

        finaltapestr = ""

        for index in range (len(self.tape)):
            finaltapestr += "[" + str(self.tape[index]) + "] "

        msgTape = QtGui.QMessageBox()
        msgTape.setWindowTitle("Final Tape")
        msgTape.setText("<b>" + finaltapestr + "</b>")
        msgTape.setStandardButtons(QtGui.QMessageBox.Ok)
        msgTape.exec_()

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