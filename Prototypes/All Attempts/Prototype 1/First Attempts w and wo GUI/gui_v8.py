from PyQt4 import QtGui
from PyQt4.QtCore import Qt
import sys
from time import sleep

class TuringMachine():

    def __init__(self):
        self.tape = []
        self.tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6,7]  # positions of the tape, which will change depending on left or right (GUI)
        self.str_instructions = []
        self.instructions = []
        self.tape_position = 0 # tape position (machine)

    def saveInstructions(self, filename):

        templist = []

        templist.append(str(self.txtScannedState.text()))
        templist.append(str(self.txtScannedSymbol.text()))
        templist.append(str(self.txtDirection.text()))
        templist.append(str(self.txtNewSymbol.text()))
        templist.append(str(self.txtNewState.text()))
        self.instructions.append(templist)

        self.str_instructions.append("Scanned State: " + str(self.txtScannedState.text()) + "   " +
                                     "Scanned Symbol: " + str(self.txtScannedSymbol.text()) + "   ")
        self.str_instructions.append("Direction: " + str(self.txtDirection.text()))
        self.str_instructions.append("New Symbol: " + str(self.txtNewSymbol.text()) + "   " +
                                     "New State: " + str(self.txtNewState.text()))

        self.txtScannedState.setText("")
        self.txtScannedSymbol.setText("")
        self.txtDirection.setText("")
        self.txtNewSymbol.setText("")
        self.txtNewState.setText("")

        print "Current Instructions: " + str(self.instructions)

        self.fillInstructions()

    def runMachine(self):

        self.btnRight.setEnabled(False)
        self.btnLeft.setEnabled(False)
        self.btnSubmit.setEnabled(False)
        self.btnExit.setEnabled(False)
        self.txtScannedState.setEnabled(False)
        self.txtScannedSymbol.setEnabled(False)
        self.txtDirection.setEnabled(False)
        self.txtNewSymbol.setEnabled(False)
        self.txtNewState.setEnabled(False)
        self.txtDeleteInstruction.setEnabled(False)
        app.processEvents()

        tape_position = 0
        current_instruction_set = []
        instructionfound = False
        current_state = "A" # start state

        while current_state != "H" and len(self.tape) > 0:

            app.processEvents()
            current_symbol = self.tape[tape_position]
            for index in range(len(self.instructions)):  # goes through the instructions
                if self.instructions[index][0] == current_state and self.instructions[index][1] == current_symbol:  # if both the symbol and state match the instruction
                    current_instruction_set = self.instructions[index]  # make a copy of that instruction to be executed
                    instructionfound = True

            if instructionfound == True:

                self.btnRight.setEnabled(False)
                self.btnLeft.setEnabled(False)
                self.btnSubmit.setEnabled(False)
                self.btnExit.setEnabled(False)
                self.txtScannedState.setEnabled(False)
                self.txtScannedSymbol.setEnabled(False)
                self.txtDirection.setEnabled(False)
                self.txtNewSymbol.setEnabled(False)
                self.txtNewState.setEnabled(False)
                self.txtDeleteInstruction.setEnabled(False)

                print "Current Tape: " + str(self.tape)
                print "Scanned Symbol: " + str(current_symbol)
                print "Scanned State: " + str(current_state)

                self.lblScannedState.setText(str(current_instruction_set[0]))
                sleep(0.5)
                app.processEvents()
                self.lblScannedSymbol.setText(str(current_instruction_set[1]))
                sleep(0.5)
                app.processEvents()
                self.lblDirection.setText(str(current_instruction_set[2]))
                sleep(0.5)
                app.processEvents()
                self.lblNewSymbol.setText(str(current_instruction_set[3]))
                sleep(0.5)
                app.processEvents()
                self.lblNewState.setText(str(current_instruction_set[4]))
                sleep(0.5)
                app.processEvents()


                self.tape[tape_position] = current_instruction_set[3]  # assigns new value to the tape
                print "New Value on Square: " + str(self.tape[tape_position])
                current_state = current_instruction_set[4]  # assigns new state to machine
                print "New State of Machine: " + str(current_state)

                if current_instruction_set[2] == "R" and current_instruction_set[4] != "H":
                    tape_position += 1

                    if tape_position == len(self.tape):
                        self.tape.append('#')

                    self.moveRight()

                    sleep(1)

                    print "Moving Right"
                    print "--------------------------------------"
                    print ""

                    instructionfound = False

                elif current_instruction_set[2] == "L" and current_instruction_set[4] != "H":
                    tape_position -= 1

                    if tape_position == -1:
                        tape_position = 0

                    self.moveLeft()

                    sleep(1)

                    print "Moving Left"
                    print "--------------------------------------"
                    print ""

                    instructionfound = False

                    if tape_position < 0 or tape_position > len(self.tape):
                        self.final_tape()
                        print ""
                        print "<--- End of Tape --->"
                        print "Final Tape: " + str(self.tape)
            else:
                self.final_tape()
                print ""
                print "<--- End of Tape --->"
                print "Final Tape: " + str(self.tape)
                break

        else:
            self.final_tape()
            print ""
            print "<--- End of Tape --->"
            print "Final Tape: " + str(self.tape)

        self.reset_tape()
        self.btnRight.setEnabled(True)
        self.btnLeft.setEnabled(True)
        self.btnSubmit.setEnabled(True)
        self.btnExit.setEnabled(True)
        self.txtScannedState.setEnabled(True)
        self.txtScannedSymbol.setEnabled(True)
        self.txtDirection.setEnabled(True)
        self.txtNewSymbol.setEnabled(True)
        self.txtNewState.setEnabled(True)
        self.txtDeleteInstruction.setEnabled(True)
        app.processEvents()

class CustomTapeWindow(QtGui.QMainWindow, TuringMachine):

    def __init__(self, parent = None):
        super(CustomTapeWindow, self).__init__(parent)
        TuringMachine.__init__(self)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        self.setGeometry(700, 400, 1070, 295)
        self.setFixedSize(1070, 295)
        self.setWindowTitle("Write a Custom Tape")
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.setStyleSheet("background-color: #dedddd;")

        self.scroll_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]  # positions of the tape, which will change depending on left or right

        self.drawWindow()

    def drawWindow(self):

        self.lblInstructionTitle = QtGui.QLabel("Running Instructions:", self)
        self.lblInstructionTitle.move(820, 2)
        self.lblInstructionTitle.resize(self.lblInstructionTitle.sizeHint())
        self.lblInstructionBorder = QtGui.QLabel(self)
        self.lblInstructionBorder.setWordWrap(True)
        self.lblInstructionBorder.setText(" Scanned State: \n\n"
                               " Scanned Symbol: \n\n"
                               " Direction: \n\n"
                               " New Symbol: \n\n"
                               " New State: \n\n")
        self.lblInstructionBorder.setStyleSheet(
            "font-size: 20px; "
            "border: 2px solid #000000;"
            "border-style: dashed hidden hidden dashed;"
            "background-color: #ededed;")
        self.lblInstructionBorder.setFont(QtGui.QFont('Times', 40))
        self.lblInstructionBorder.resize(250, 300)
        self.lblInstructionBorder.move(820, 20)

        self.lblScannedState = QtGui.QLabel("N/A", self)
        self.lblScannedState.resize(50, 50)
        self.lblScannedState.move(1000, 30)
        self.lblScannedState.setAlignment(Qt.AlignCenter)
        self.lblScannedState.setStyleSheet("background-color: #ededed;")
        self.lblScannedState.setFont(QtGui.QFont('Times', 20))

        self.lblScannedSymbol = QtGui.QLabel("N/A", self)
        self.lblScannedSymbol.resize(50, 50)
        self.lblScannedSymbol.move(1000, 75)
        self.lblScannedSymbol.setAlignment(Qt.AlignCenter)
        self.lblScannedSymbol.setStyleSheet("background-color: #ededed;")
        self.lblScannedSymbol.setFont(QtGui.QFont('Times', 20))

        self.lblDirection = QtGui.QLabel("N/A", self)
        self.lblDirection.resize(50, 50)
        self.lblDirection.move(1000, 120)
        self.lblDirection.setAlignment(Qt.AlignCenter)
        self.lblDirection.setStyleSheet("background-color: #ededed;")
        self.lblDirection.setFont(QtGui.QFont('Times', 20))

        self.lblNewSymbol = QtGui.QLabel("N/A", self)
        self.lblNewSymbol.resize(50, 50)
        self.lblNewSymbol.move(1000, 165)
        self.lblNewSymbol.setAlignment(Qt.AlignCenter)
        self.lblNewSymbol.setStyleSheet("background-color: #ededed;")
        self.lblNewSymbol.setFont(QtGui.QFont('Times', 20))

        self.lblNewState = QtGui.QLabel("N/A", self)
        self.lblNewState.resize(50, 50)
        self.lblNewState.move(1000, 210)
        self.lblNewState.setAlignment(Qt.AlignCenter)
        self.lblNewState.setStyleSheet("background-color: #ededed;")
        self.lblNewState.setFont(QtGui.QFont('Times', 20))

        self.lblInfinite0 = QtGui.QLabel("...", self)
        self.lblInfinite0.resize(50, 50)
        self.lblInfinite0.move(253, 215)
        self.lblInfinite0.setAlignment(Qt.AlignCenter)
        self.lblInfinite0.setFont(QtGui.QFont('Times', 40))

        self.lblTape0 = QtGui.QLabel("#", self)
        self.lblTape0.resize(50, 50)
        self.lblTape0.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")     # css sheet
        self.lblTape0.move(302, 230)
        self.lblTape0.setAlignment(Qt.AlignCenter)
        self.lblTape0.setFont(QtGui.QFont('Times', 20))

        self.lblTape1 = QtGui.QLabel("#", self)
        self.lblTape1.resize(50, 50)
        self.lblTape1.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape1.move(357, 230)
        self.lblTape1.setAlignment(Qt.AlignCenter)
        self.lblTape1.setFont(QtGui.QFont('Times', 20))

        self.lblTape2 = QtGui.QLabel("#", self)
        self.lblTape2.resize(50, 50)
        self.lblTape2.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape2.move(417, 230)
        self.lblTape2.setAlignment(Qt.AlignCenter)
        self.lblTape2.setFont(QtGui.QFont('Times', 20))

        self.lblTape3 = QtGui.QLabel("#", self)
        self.lblTape3.resize(50, 50)
        self.lblTape3.setStyleSheet(
            "border: 7px solid #ff0000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape3.move(477, 230)
        self.lblTape3.setAlignment(Qt.AlignCenter)
        self.lblTape3.setFont(QtGui.QFont('Times', 20))

        self.lblTape4 = QtGui.QLabel("#", self)
        self.lblTape4.resize(50, 50)
        self.lblTape4.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape4.move(537, 230)
        self.lblTape4.setAlignment(Qt.AlignCenter)
        self.lblTape4.setFont(QtGui.QFont('Times', 20))

        self.lblTape5 = QtGui.QLabel("#", self)
        self.lblTape5.resize(50, 50)
        self.lblTape5.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape5.move(597, 230)
        self.lblTape5.setAlignment(Qt.AlignCenter)
        self.lblTape5.setFont(QtGui.QFont('Times', 20))

        self.lblTape6 = QtGui.QLabel("#", self)
        self.lblTape6.resize(50, 50)
        self.lblTape6.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape6.move(657, 230)
        self.lblTape6.setAlignment(Qt.AlignCenter)
        self.lblTape6.setFont(QtGui.QFont('Times', 20))

        self.lblTape7 = QtGui.QLabel("#", self)
        self.lblTape7.resize(50, 50)
        self.lblTape7.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape7.move(717, 230)
        self.lblTape7.setAlignment(Qt.AlignCenter)
        self.lblTape7.setFont(QtGui.QFont('Times', 20))

        self.lblInfinite1 = QtGui.QLabel("...", self)
        self.lblInfinite1.resize(50, 50)
        self.lblInfinite1.move(770, 215)
        self.lblInfinite1.setAlignment(Qt.AlignCenter)
        self.lblInfinite1.setFont(QtGui.QFont('Times', 40))

        self.btnRun = QtGui.QPushButton("Run", self)
        self.btnRun.clicked.connect(self.start)
        self.btnRun.resize(330, 20)
        self.btnRun.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: green; ")
        self.btnRun.move(370, 200)

        self.txtTape = QtGui.QLineEdit(self)
        self.txtTape.setStyleSheet(
            "border: 1px solid #000000;"
            "background-color: #ffffff;")
        self.txtTape.resize(440, 20)
        self.txtTape.move(260, 170)

        self.lblTape = QtGui.QLabel("Insert Tape: ", self)
        self.lblTape.move(260, 145)
        self.lblTape.setStyleSheet("background-color: rgba(0,0,0,0%);") #transparent

        self.btnSubmit = QtGui.QPushButton("Submit", self)
        self.btnSubmit.clicked.connect(self.submit)
        self.btnSubmit.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: green; ")
        self.btnSubmit.resize(100, 20)
        self.btnSubmit.move(710, 170)

        self.btnExit = QtGui.QPushButton("Return To Menu", self)
        self.btnExit.clicked.connect(self.close)
        self.btnExit.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: #901414; ")
        self.btnExit.resize(150, 20)
        self.btnExit.move(873, 263)

        self.btnRight = QtGui.QPushButton("--->", self)
        self.btnRight.clicked.connect(self.moveRight)
        self.btnRight.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: #bf6b18; ")
        self.btnRight.resize(100, 20)
        self.btnRight.move(710,200)

        self.btnLeft = QtGui.QPushButton("<---", self)
        self.btnLeft.clicked.connect(self.moveLeft)
        self.btnLeft.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: #bf6b18; ")
        self.btnLeft.resize(100,20)
        self.btnLeft.move(260,200)

        self.lblAddInstructions = QtGui.QLabel("Add an Instruction:", self)
        self.lblAddInstructions.move(5, 2)
        self.lblAddInstructions.resize(self.lblAddInstructions.sizeHint())

        self.lblAddInstructionBorder = QtGui.QLabel(self)
        self.lblAddInstructionBorder.setWordWrap(True)
        self.lblAddInstructionBorder.setText(" Scanned State: \n\n"
                                          " Scanned Symbol: \n\n"
                                          " Direction: \n\n"
                                          " New Symbol: \n\n"
                                          " New State: \n\n")
        self.lblAddInstructionBorder.setStyleSheet(
            "font-size: 20px; "
            "border: 2px solid #000000;"
            "border-style: dashed dashed hidden hidden;"
            "background-color: #ededed;")
        self.lblAddInstructionBorder.setFont(QtGui.QFont('Times', 40))
        self.lblAddInstructionBorder.resize(250, 300)
        self.lblAddInstructionBorder.move(0, 20)

        self.txtScannedState = QtGui.QLineEdit(self)
        self.txtScannedState.resize(50, 40)
        self.txtScannedState.move(180, 30)
        self.txtScannedState.setAlignment(Qt.AlignCenter)
        self.txtScannedState.setStyleSheet("background-color: #ededed;")
        self.txtScannedState.setFont(QtGui.QFont('Times', 20))

        self.txtScannedSymbol = QtGui.QLineEdit(self)
        self.txtScannedSymbol.resize(50, 40)
        self.txtScannedSymbol.move(180, 75)
        self.txtScannedSymbol.setAlignment(Qt.AlignCenter)
        self.txtScannedSymbol.setStyleSheet("background-color: #ededed;")
        self.txtScannedSymbol.setFont(QtGui.QFont('Times', 20))

        self.txtDirection = QtGui.QLineEdit(self)
        self.txtDirection.resize(50, 40)
        self.txtDirection.move(180, 120)
        self.txtDirection.setAlignment(Qt.AlignCenter)
        self.txtDirection.setStyleSheet("background-color: #ededed;")
        self.txtDirection.setFont(QtGui.QFont('Times', 20))

        self.txtNewSymbol = QtGui.QLineEdit(self)
        self.txtNewSymbol.resize(50, 40)
        self.txtNewSymbol.move(180, 165)
        self.txtNewSymbol.setAlignment(Qt.AlignCenter)
        self.txtNewSymbol.setStyleSheet("background-color: #ededed;")
        self.txtNewSymbol.setFont(QtGui.QFont('Times', 20))

        self.txtNewState = QtGui.QLineEdit(self)
        self.txtNewState.resize(50, 40)
        self.txtNewState.move(180, 210)
        self.txtNewState.setAlignment(Qt.AlignCenter)
        self.txtNewState.setStyleSheet("background-color: #ededed;")
        self.txtNewState.setFont(QtGui.QFont('Times', 20))

        self.btnSubmitInstruction = QtGui.QPushButton("Submit Instruction", self)
        self.btnSubmitInstruction.clicked.connect(self.saveInstructions)
        self.btnSubmitInstruction.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: green; ")
        self.btnSubmitInstruction.resize(150, 20)
        self.btnSubmitInstruction.move(50, 263)

        self.lblViewInstructions = QtGui.QLabel("Saved Instructions:", self)
        self.lblViewInstructions.move(260, 2)
        self.lblViewInstructions.resize(self.lblViewInstructions.sizeHint())

        self.txtViewInstructions = QtGui.QPlainTextEdit(self)
        self.txtViewInstructions.resize(440, 130)
        self.txtViewInstructions.move(260, 20)
        self.txtViewInstructions.setStyleSheet("background-color: #ededed;")
        self.txtViewInstructions.setFont(QtGui.QFont('Times', 14))
        self.txtViewInstructions.setReadOnly(True)
        self.txtViewInstructions.setPlainText("No Instructions Loaded, \n"
                                              "Add Instructions on the Right Side of the Window")

        self.btnClearInstructions = QtGui.QPushButton("Clear Instructions", self)
        self.btnClearInstructions.clicked.connect(self.clearInstructions)
        self.btnClearInstructions.resize(100, 20)
        self.btnClearInstructions.move(710, 20)
        self.btnClearInstructions.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: #901414;")
        self.btnClearInstructions.setFont(QtGui.QFont('SansSerif', 7.5))

        self.lblDeleteInstruction = QtGui.QLabel("Delete Instructions:", self)
        self.lblDeleteInstruction.move(710, -5)
        self.lblDeleteInstruction.setStyleSheet("background-color: rgba(0,0,0,0%);")  # transparent


        self.txtDeleteInstruction = QtGui.QLineEdit(self)
        self.txtDeleteInstruction.move(730, 50)
        self.txtDeleteInstruction.resize(60, 50)
        self.txtDeleteInstruction.setStyleSheet("background-color: #ededed;")
        self.txtDeleteInstruction.setFont(QtGui.QFont('Times', 14))
        self.txtDeleteInstruction.setAlignment(Qt.AlignCenter)

        self.btnDeleteInstruction = QtGui.QPushButton("Delete Instruction", self)
        self.btnDeleteInstruction.clicked.connect(self.deleteInstruction)
        self.btnDeleteInstruction.resize(100, 20)
        self.btnDeleteInstruction.move(710, 110)
        self.btnDeleteInstruction.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: #901414;")
        self.btnDeleteInstruction.setFont(QtGui.QFont('SansSerif', 7.5))

        self.txtStartingPosition = QtGui.QLineEdit(self)
        self.txtStartingPosition.move(710, 140)
        self.txtStartingPosition.resize(100, 20)

        self.fillTape()

    def fillTape(self):

        self.lblTape0.setText("#")
        self.lblTape1.setText("#")
        self.lblTape2.setText("#")
        self.lblTape3.setText("#")
        self.lblTape4.setText("#")
        self.lblTape5.setText("#")
        self.lblTape6.setText("#")
        self.lblTape7.setText("#")

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

        app.processEvents()

    def fillInstructions(self):

        self.txtViewInstructions.setPlainText("")
        index = 0
        instruction_number = 0

        while index != len(self.str_instructions):
            self.txtViewInstructions.appendPlainText("INSTRUCTION: " + str(instruction_number) + ":")

            self.txtViewInstructions.appendPlainText(str(self.str_instructions[index]))
            self.txtViewInstructions.appendPlainText(str(self.str_instructions[index + 1]))
            self.txtViewInstructions.appendPlainText(str(self.str_instructions[index + 2]))
            self.txtViewInstructions.appendPlainText("---------------------------------------------------------")
            index += 3
            instruction_number += 1

        app.processEvents()

    def deleteInstruction(self):
        if self.txtDeleteInstruction.text() != "":
            instruction = int(self.txtDeleteInstruction.text())
            index = instruction * 3

            if index + 2 <= len(self.str_instructions) and len(self.instructions) > 0:

                print "Deleting Instruction: (" + str(instruction) + ") " + str(self.instructions[instruction])

                self.instructions.pop(instruction)
                self.txtViewInstructions.setPlainText("")

                self.str_instructions.pop(index)
                self.str_instructions.pop(index)
                self.str_instructions.pop(index)

                self.fillInstructions()

                if self.txtViewInstructions.toPlainText() == "":
                    self.txtViewInstructions.setPlainText("No Instructions Loaded, \n"
                                              "Add Instructions on the Right Side of the Window")
            self.txtDeleteInstruction.setText("")

    def clearInstructions(self):
        self.instructions = []
        app.processEvents()
        self.txtViewInstructions.setPlainText("No Instructions Loaded, \n"
                                              "Add Instructions on the Right Side of the Window")

    def moveLeft(self):
        print "LEFT"
        for index in range(len(self.tape_positions)):
            self.tape_positions[index] -= 1

        if self.tape_positions[3] == -1:
            self.tape = ["#"] + self.tape
            for index in range(len(self.tape_positions)):
                self.tape_positions[index] += 1

        if self.tape_positions[3] > -1:
            if self.tape_positions[0] > -1:
                self.lblTape0.setText(str(self.tape[self.tape_positions[0]]))
            else:
                self.lblTape0.setText("#")
            if self.tape_positions[1] > -1:
                self.lblTape1.setText(str(self.tape[self.tape_positions[1]]))
            else:
                self.lblTape1.setText("#")
            if self.tape_positions[2] > -1:
                self.lblTape2.setText(str(self.tape[self.tape_positions[2]]))
            else:
                self.lblTape2.setText("#")
            self.lblTape3.setText(str(self.tape[self.tape_positions[3]]))
            self.lblTape4.setText(str(self.tape[self.tape_positions[4]]))
            self.lblTape5.setText(str(self.tape[self.tape_positions[5]]))
            self.lblTape6.setText(str(self.tape[self.tape_positions[6]]))
            self.lblTape7.setText(str(self.tape[self.tape_positions[7]]))

        if self.tape_position > 0:
            self.tape_position -= 1

    def moveRight(self):
        print "RIGHT"
        for index in range(len(self.tape_positions)):
            self.tape_positions[index] += 1

        self.tape.append("#")

        if self.tape_positions[0] > -1:
            self.lblTape0.setText(str(self.tape[self.tape_positions[0]]))
        else:
            self.lblTape0.setText("#")
        if self.tape_positions[1] > -1:
            self.lblTape1.setText(str(self.tape[self.tape_positions[1]]))
        else:
            self.lblTape1.setText("#")
        if self.tape_positions[2] > -1:
            self.lblTape2.setText(str(self.tape[self.tape_positions[2]]))
        else:
            self.lblTape2.setText("#")
        self.lblTape3.setText(str(self.tape[self.tape_positions[3]]))
        self.lblTape4.setText(str(self.tape[self.tape_positions[4]]))
        self.lblTape5.setText(str(self.tape[self.tape_positions[5]]))
        self.lblTape6.setText(str(self.tape[self.tape_positions[6]]))
        self.lblTape7.setText(str(self.tape[self.tape_positions[7]]))

        self.tape_position += 1


    def submit(self):

        self.scroll_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]  # resets scroll positions

        if self.txtTape.text() == "":
            self.txtTape.setText("#")

        inputtape = str(self.txtTape.text())

        self.tape = inputtape.split(",")  # splits each value by comma, allowing for multiple entries

        while len(self.tape) < 8:
            self.tape.append("#")

        #self.tape_position = int(self.txtStartingPosition.text())

        self.fillTape()

        # for count in range(self.tape_position):
        #     self.moveRight()

        app.processEvents()

        self.txtTape.setText("")

    def reset_tape(self):
        self.lblTape0.setText("#")
        self.lblTape1.setText("#")
        self.lblTape2.setText("#")
        self.lblTape3.setText("#")
        self.lblTape4.setText("#")
        self.lblTape5.setText("#")
        self.lblTape6.setText("#")
        self.lblTape7.setText("#")
        self.tape = []
        self.tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6,7]  # positions of the tape, which will change depending on left or right

        self.lblScannedState.setText("N/A")
        self.lblScannedSymbol.setText("N/A")
        self.lblDirection.setText("N/A")
        self.lblNewSymbol.setText("N/A")
        self.lblNewState.setText("N/A")

    def final_tape(self):

        finaltapestr = ""

        while self.tape[0] == "#":
            self.tape.pop(0)
            if self.tape[0] != "#":
                break

        while self.tape[-1] == "#":
            self.tape.pop(-1)
            if self.tape[-1] != "#":
                break

        for index in range (len(self.tape)):
            finaltapestr += "[" + str(self.tape[index]) + "] "

        msgTape = QtGui.QMessageBox()
        msgTape.setWindowTitle("Final Tape")
        msgTape.setText("<b>" + finaltapestr + "</b>")
        msgTape.setStandardButtons(QtGui.QMessageBox.Ok)
        msgTape.exec_()

    # def scrollRight(self):
    #
    #     for index in range(len(self.scroll_positions)):
    #         self.scroll_positions[index] += 1
    #
    #     if self.scroll_positions[8] <= len(self.tape):
    #         if self.scroll_positions[0] > -1:
    #             self.lblTape0.setText(str(self.tape[self.scroll_positions[0]]))
    #         else:
    #             self.lblTape0.setText("#")
    #         if self.scroll_positions[1] > -1:
    #             self.lblTape1.setText(str(self.tape[self.scroll_positions[1]]))
    #         else:
    #             self.lblTape1.setText("#")
    #         if self.scroll_positions[2] > -1:
    #             self.lblTape2.setText(str(self.tape[self.scroll_positions[2]]))
    #         else:
    #             self.lblTape2.setText("#")
    #         self.lblTape3.setText(str(self.tape[self.scroll_positions[3]]))
    #         self.lblTape4.setText(str(self.tape[self.scroll_positions[4]]))
    #         self.lblTape5.setText(str(self.tape[self.scroll_positions[5]]))
    #         self.lblTape6.setText(str(self.tape[self.scroll_positions[6]]))
    #         self.lblTape7.setText(str(self.tape[self.scroll_positions[7]]))
    #
    #     else:
    #         for index in range(len(self.scroll_positions)):
    #             self.scroll_positions[index] -= 1
    #
    #
    #     app.processEvents()
    #
    # def scrollLeft(self):
    #
    #     for index in range(len(self.scroll_positions)):
    #         self.scroll_positions[index] -= 1
    #
    #     if self.scroll_positions[2] >= -1:
    #         if self.scroll_positions[0] > -1:
    #             self.lblTape0.setText(str(self.tape[self.scroll_positions[0]]))
    #         else:
    #             self.lblTape0.setText("#")
    #         if self.scroll_positions[1] > -1:
    #             self.lblTape1.setText(str(self.tape[self.scroll_positions[1]]))
    #         else:
    #             self.lblTape1.setText("#")
    #         if self.scroll_positions[2] > -1:
    #             self.lblTape2.setText(str(self.tape[self.scroll_positions[2]]))
    #         else:
    #             self.lblTape2.setText("#")
    #         self.lblTape3.setText(str(self.tape[self.scroll_positions[3]]))
    #         self.lblTape4.setText(str(self.tape[self.scroll_positions[4]]))
    #         self.lblTape5.setText(str(self.tape[self.scroll_positions[5]]))
    #         self.lblTape6.setText(str(self.tape[self.scroll_positions[6]]))
    #         self.lblTape7.setText(str(self.tape[self.scroll_positions[7]]))
    #
    #     else:
    #         for index in range(len(self.scroll_positions)):
    #             self.scroll_positions[index] += 1
    #
    #     app.processEvents()

    def start(self):
        self.fillTape()
        self.runMachine()

class ExamplesWindow(QtGui.QMainWindow, TuringMachine):
    pass

class HomeWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        super(HomeWindow, self).__init__()
        self.setGeometry(700, 400, 350, 185)
        self.setFixedSize(350, 185)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.draw_Window()

    def draw_Window(self):

        self.btnStartCustomTape = QtGui.QPushButton("Start Machine With Custom Tape", self)
        self.btnStartCustomTape.clicked.connect(self.showCustomTape)
        self.btnStartCustomTape.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: green; "
            "font-size: 17px")
        self.btnStartCustomTape.resize(300, 40)
        self.btnStartCustomTape.move(25, 25)

        self.btnStartExampleTapes = QtGui.QPushButton("Example Machines", self)
        self.btnStartExampleTapes.clicked.connect(self.showExamples)

        self.btnStartExampleTapes.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: green; "
            "font-size: 17px")
        self.btnStartExampleTapes.resize(300, 40)
        self.btnStartExampleTapes.move(25, 75)

        self.btnQuit = QtGui.QPushButton("Quit", self)
        self.btnQuit.clicked.connect(self.close_application)
        self.btnQuit.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: #901414; "
            "font-size: 20px")
        self.btnQuit.resize(300, 40)
        self.btnQuit.move(25, 125)

        self.customtape_dialog = CustomTapeWindow(self)
        self.examples_dialog = ExamplesWindow(self)
        self.show()

    def close_application(self):
        userinput = QtGui.QMessageBox.question(self, 'Quit', "Are you sure you wish to exit?",
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if userinput == QtGui.QMessageBox.Yes:
            print "EXITING"
            sys.exit()
        else:
            pass

    def showCustomTape(self):
        self.customtape_dialog.show()

    def showExamples(self):
        self.examples_dialog.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)  # argv allows you to pass arguments through the cmd when running
                                        # defined app here
    GUI = HomeWindow()
    sys.exit(app.exec_())