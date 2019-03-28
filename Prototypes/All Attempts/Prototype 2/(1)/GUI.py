#import TuringMachine
from PyQt4 import QtGui, QtCore
import sys
from time import sleep

GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]

class State:
    instructions = []
    current_context = None

    def __init__(self, context):
        self.current_context = context
        self.instructions = []

    def executeInstruction(self):
        for index in range(len(self.instructions)):
            if self.current_context.tape_position == len(self.current_context.tape):
                break
            if self.instructions[index].symbol == self.current_context.tape[self.current_context.tape_position]:
                self.current_context.tape[self.current_context.tape_position] = self.instructions[index].new_symbol
                print "New Symbol:", self.instructions[index].new_symbol

                if self.instructions[index].direction == 'R':
                    print "Right"
                    self.current_context.moveRight()
                    
                elif self.instructions[index].direction == 'L':
                    print "Left"
                    self.current_context.moveLeft()

                self.current_context.setState(self.instructions[index].next_state)
                self.current_context.state_name = self.instructions[index].next_state
                self.current_context.tape_direction = self.instructions[index].direction

                print "Current State: ", self.current_context.state_name
                break

    def setInstruction(self, symbol, direction, new_symbol, next_state):
        new_instruction = Instruction()
        new_instruction.symbol = symbol
        new_instruction.direction = direction
        new_instruction.new_symbol = new_symbol
        new_instruction.next_state = next_state
        self.instructions.append(new_instruction)

class Instruction:
    symbol = ''
    direction = 'None'
    new_symbol = ''
    next_state = ''

class TuringMachine():
    current_state = None
    state_name = ""
    tape_direction = ""
    available_states = {"HALT": None}
    tape = []
    tape_position = 0
    temp_instructions = []
    starting_state = None

    def runMachine(self):
        print self.temp_instructions
        for instruction in self.temp_instructions:
            if instruction[0] not in self.available_states:
                self.available_states[instruction[0]] = State(self)
            self.available_states[instruction[0]].setInstruction(instruction[1], instruction[2], instruction[3], instruction[4])

        self.current_state = self.available_states[self.starting_state]
        self.state_name = self.starting_state
        print "Starting State: ", self.state_name

        while self.state_name is not "HALT":
            
            self.executeInstruction()

    def moveRight(self):    # handles moving right on the tape
        self.tape_position += 1
        self.tape.append("#")   # if the position is at the end, add a blank symbol

    def moveLeft(self): # handles moving left on the tape
        self.tape_position -= 1
        self.tape = ["#"] + self.tape   # if the position is at the start, add a blank symbol

    def changeSymbol(self, symbol):
        self.tape[self.tape_position] == str(symbol)    # changes the current squares symbol on the tape

    def saveInstruction(self, state, symbol, direction, new_symbol, next_state):
        current_instruction = [state, symbol, direction, new_symbol, next_state]
        self.temp_instructions.append(current_instruction)

    def setTape(self, tape):
        self.tape = (tape.split(","))
        while len(self.tape) < 8:
            self.tape.append("#")

    def setState(self, state):
        self.current_state = self.available_states[state]

    def executeInstruction(self):
        self.current_state.executeInstruction()

class CustomTapeWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        super(CustomTapeWindow, self).__init__(parent)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        self.setGeometry(700, 400, 1070, 295)
        self.setFixedSize(1070, 295)
        self.setWindowTitle("Write a Custom Tape")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)
        self.setStyleSheet("background-color: #dedddd;")
        self.machine = TuringMachine()
        self.str_instructions = []

        #self.scroll_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]  # positions of the tape, which will change depending on left or right

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
        self.lblScannedState.setAlignment(QtCore.Qt.AlignCenter)
        self.lblScannedState.setStyleSheet("background-color: #ededed;")
        self.lblScannedState.setFont(QtGui.QFont('Times', 20))

        self.lblScannedSymbol = QtGui.QLabel("N/A", self)
        self.lblScannedSymbol.resize(50, 50)
        self.lblScannedSymbol.move(1000, 75)
        self.lblScannedSymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.lblScannedSymbol.setStyleSheet("background-color: #ededed;")
        self.lblScannedSymbol.setFont(QtGui.QFont('Times', 20))

        self.lblDirection = QtGui.QLabel("N/A", self)
        self.lblDirection.resize(50, 50)
        self.lblDirection.move(1000, 120)
        self.lblDirection.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDirection.setStyleSheet("background-color: #ededed;")
        self.lblDirection.setFont(QtGui.QFont('Times', 20))

        self.lblNewSymbol = QtGui.QLabel("N/A", self)
        self.lblNewSymbol.resize(50, 50)
        self.lblNewSymbol.move(1000, 165)
        self.lblNewSymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNewSymbol.setStyleSheet("background-color: #ededed;")
        self.lblNewSymbol.setFont(QtGui.QFont('Times', 20))

        self.lblNewState = QtGui.QLabel("N/A", self)
        self.lblNewState.resize(50, 50)
        self.lblNewState.move(1000, 210)
        self.lblNewState.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNewState.setStyleSheet("background-color: #ededed;")
        self.lblNewState.setFont(QtGui.QFont('Times', 20))

        self.lblInfinite0 = QtGui.QLabel("...", self)
        self.lblInfinite0.resize(50, 50)
        self.lblInfinite0.move(253, 215)
        self.lblInfinite0.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfinite0.setFont(QtGui.QFont('Times', 40))

        self.lblTape0 = QtGui.QLabel("#", self)
        self.lblTape0.resize(50, 50)
        self.lblTape0.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")     # css sheet
        self.lblTape0.move(302, 230)
        self.lblTape0.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTape0.setFont(QtGui.QFont('Times', 20))

        self.lblTape1 = QtGui.QLabel("#", self)
        self.lblTape1.resize(50, 50)
        self.lblTape1.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape1.move(357, 230)
        self.lblTape1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTape1.setFont(QtGui.QFont('Times', 20))

        self.lblTape2 = QtGui.QLabel("#", self)
        self.lblTape2.resize(50, 50)
        self.lblTape2.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape2.move(417, 230)
        self.lblTape2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTape2.setFont(QtGui.QFont('Times', 20))

        self.lblTape3 = QtGui.QLabel("#", self)
        self.lblTape3.resize(50, 50)
        self.lblTape3.setStyleSheet(
            "border: 7px solid #ff0000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape3.move(477, 230)
        self.lblTape3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTape3.setFont(QtGui.QFont('Times', 20))

        self.lblTape4 = QtGui.QLabel("#", self)
        self.lblTape4.resize(50, 50)
        self.lblTape4.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape4.move(537, 230)
        self.lblTape4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTape4.setFont(QtGui.QFont('Times', 20))

        self.lblTape5 = QtGui.QLabel("#", self)
        self.lblTape5.resize(50, 50)
        self.lblTape5.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape5.move(597, 230)
        self.lblTape5.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTape5.setFont(QtGui.QFont('Times', 20))

        self.lblTape6 = QtGui.QLabel("#", self)
        self.lblTape6.resize(50, 50)
        self.lblTape6.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape6.move(657, 230)
        self.lblTape6.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTape6.setFont(QtGui.QFont('Times', 20))

        self.lblTape7 = QtGui.QLabel("#", self)
        self.lblTape7.resize(50, 50)
        self.lblTape7.setStyleSheet(
            "border:3px solid #000000;"
            "background-color: #ffffff;")  # css sheet
        self.lblTape7.move(717, 230)
        self.lblTape7.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTape7.setFont(QtGui.QFont('Times', 20))

        self.lblInfinite1 = QtGui.QLabel("...", self)
        self.lblInfinite1.resize(50, 50)
        self.lblInfinite1.move(770, 215)
        self.lblInfinite1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfinite1.setFont(QtGui.QFont('Times', 40))

        self.btnRun = QtGui.QPushButton("Run", self)
        self.btnRun.clicked.connect(self.runMachine)
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
        self.btnRight.clicked.connect(self.scrollRight)
        self.btnRight.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: #bf6b18; ")
        self.btnRight.resize(100, 20)
        self.btnRight.move(710,200)

        self.btnLeft = QtGui.QPushButton("<---", self)
        self.btnLeft.clicked.connect(self.scrollLeft)
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
        self.txtScannedState.setAlignment(QtCore.Qt.AlignCenter)
        self.txtScannedState.setStyleSheet("background-color: #ededed;")
        self.txtScannedState.setFont(QtGui.QFont('Times', 20))

        self.txtScannedSymbol = QtGui.QLineEdit(self)
        self.txtScannedSymbol.resize(50, 40)
        self.txtScannedSymbol.move(180, 75)
        self.txtScannedSymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.txtScannedSymbol.setStyleSheet("background-color: #ededed;")
        self.txtScannedSymbol.setFont(QtGui.QFont('Times', 20))

        self.txtDirection = QtGui.QLineEdit(self)
        self.txtDirection.resize(50, 40)
        self.txtDirection.move(180, 120)
        self.txtDirection.setAlignment(QtCore.Qt.AlignCenter)
        self.txtDirection.setStyleSheet("background-color: #ededed;")
        self.txtDirection.setFont(QtGui.QFont('Times', 20))

        self.cbDirection = QtGui.QComboBox(self)
        self.cbDirection.addItems(["None", "R", "L"])
        self.cbDirection.move(130, 120)
        self.cbDirection.resize(100, 40)
        self.cbDirection.setStyleSheet("background-color: #ededed;")
        self.cbDirection.setFont(QtGui.QFont('Times', 15))


        self.txtNewSymbol = QtGui.QLineEdit(self)
        self.txtNewSymbol.resize(50, 40)
        self.txtNewSymbol.move(180, 165)
        self.txtNewSymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.txtNewSymbol.setStyleSheet("background-color: #ededed;")
        self.txtNewSymbol.setFont(QtGui.QFont('Times', 20))

        self.txtNewState = QtGui.QLineEdit(self)
        self.txtNewState.resize(50, 40)
        self.txtNewState.move(180, 210)
        self.txtNewState.setAlignment(QtCore.Qt.AlignCenter)
        self.txtNewState.setStyleSheet("background-color: #ededed;")
        self.txtNewState.setFont(QtGui.QFont('Times', 20))

        self.btnSubmitInstruction = QtGui.QPushButton("Submit Instruction", self)
        self.btnSubmitInstruction.clicked.connect(self.setInstruction)
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

        self.txtViewInstructions = QtGui.QTextEdit(self)
        self.txtViewInstructions.resize(440, 130)
        self.txtViewInstructions.move(260, 20)
        self.txtViewInstructions.setStyleSheet("background-color: #ededed;")
        self.txtViewInstructions.setFont(QtGui.QFont('Times', 14))
        self.txtViewInstructions.setReadOnly(True)
        self.txtViewInstructions.append("No Instructions Loaded")
        self.txtViewInstructions.append("Add Instructions on the Right Side of the Window")

        self.lblDeleteAllInstructions = QtGui.QLabel("Delete Instructions:", self)
        self.lblDeleteAllInstructions.move(710, -5)
        self.lblDeleteAllInstructions.setStyleSheet("background-color: rgba(0,0,0,0%);")  # transparent

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

        self.lblDeleteInstruction = QtGui.QLabel("Delete Instruction:", self)
        self.lblDeleteInstruction.move(710, 35)
        self.lblDeleteInstruction.setStyleSheet("background-color: rgba(0,0,0,0%);")  # transparent

        self.txtDeleteInstruction = QtGui.QLineEdit(self)
        self.txtDeleteInstruction.move(710, 60)
        self.txtDeleteInstruction.resize(100, 60)
        self.txtDeleteInstruction.setStyleSheet("background-color: #ededed;")
        self.txtDeleteInstruction.setFont(QtGui.QFont('Times', 16))
        self.txtDeleteInstruction.setAlignment(QtCore.Qt.AlignCenter)

        self.btnDeleteInstruction = QtGui.QPushButton("Delete Instruction", self)
        self.btnDeleteInstruction.clicked.connect(self.deleteInstruction)
        self.btnDeleteInstruction.resize(100, 20)
        self.btnDeleteInstruction.move(710, 130)
        self.btnDeleteInstruction.setStyleSheet(
            "border: 1px solid #000000;"
            "font: bold; "
            "color: white;"
            "background-color: #901414;")
        self.btnDeleteInstruction.setFont(QtGui.QFont('SansSerif', 7.5))

        self.fillTape()

    def runMachine(self):
        self.machine.saveInstruction("A", "0", "R", "1", "B")
        self.machine.saveInstruction("A", "#", "R", "#", "HALT")
        self.machine.saveInstruction("B", "1", "R", "0", "A")
        self.machine.saveInstruction("B", "#", "R", "#", "HALT")
        self.machine.starting_state = "A"
        print "Starting Tape", self.machine.tape
        self.machine.runMachine()

    def scrollLeft(self, tape):
        print "LEFT"

        if self.machine.tape_position > 0:
            self.machine.tape_position -= 1

        for index in range(len(GUI_tape_positions)):
            GUI_tape_positions[index] -= 1

        if GUI_tape_positions[3] == -1:
            for index in range(len(GUI_tape_positions)):
                GUI_tape_positions[index] += 1

        if GUI_tape_positions[3] > -1:
            if GUI_tape_positions[0] > -1:
                self.lblTape0.setText(str(tape[GUI_tape_positions[0]]))
            else:
                self.lblTape0.setText("#")
            if GUI_tape_positions[1] > -1:
                self.lblTape1.setText(str(tape[GUI_tape_positions[1]]))
            else:
                self.lblTape1.setText("#")
            if GUI_tape_positions[2] > -1:
                self.lblTape2.setText(str(tape[GUI_tape_positions[2]]))
            else:
                self.lblTape2.setText("#")
            self.lblTape3.setText(str(tape[GUI_tape_positions[3]]))
            self.lblTape4.setText(str(tape[GUI_tape_positions[4]]))
            self.lblTape5.setText(str(tape[GUI_tape_positions[5]]))
            self.lblTape6.setText(str(tape[GUI_tape_positions[6]]))
            self.lblTape7.setText(str(tape[GUI_tape_positions[7]]))

            app.sendPostedEvents()
    
    def scrollRight(self, tape):
        print "RIGHT"

        self.machine.tape_position += 1

        for index in range(len(GUI_tape_positions)):
            GUI_tape_positions[index] += 1

        #self.machine.tape.append("#")

        if GUI_tape_positions[0] > -1:
            self.lblTape0.setText(str(tape[GUI_tape_positions[0]]))
        else:
            self.lblTape0.setText("#")
        if GUI_tape_positions[1] > -1:
            self.lblTape1.setText(str(tape[GUI_tape_positions[1]]))
        else:
            self.lblTape1.setText("#")
        if GUI_tape_positions[2] > -1:
            self.lblTape2.setText(str(tape[GUI_tape_positions[2]]))
        else:
            self.lblTape2.setText("#")
        self.lblTape3.setText(str(tape[GUI_tape_positions[3]]))
        self.lblTape4.setText(str(tape[GUI_tape_positions[4]]))
        self.lblTape5.setText(str(tape[GUI_tape_positions[5]]))
        self.lblTape6.setText(str(tape[GUI_tape_positions[6]]))
        self.lblTape7.setText(str(tape[GUI_tape_positions[7]]))

        app.sendPostedEvents()

    def fillTape(self):

        self.lblTape0.setText("#")
        self.lblTape1.setText("#")
        self.lblTape2.setText("#")
        self.lblTape3.setText("#")
        self.lblTape4.setText("#")
        self.lblTape5.setText("#")
        self.lblTape6.setText("#")
        self.lblTape7.setText("#")

        if len(self.machine.tape) >= 5:
            self.lblTape3.setText(str(self.machine.tape[0]))
            self.lblTape4.setText(str(self.machine.tape[1]))
            self.lblTape5.setText(str(self.machine.tape[2]))
            self.lblTape6.setText(str(self.machine.tape[3]))
            self.lblTape7.setText(str(self.machine.tape[4]))
        elif len(self.machine.tape) >= 4:
            self.lblTape3.setText(str(self.machine.tape[0]))
            self.lblTape4.setText(str(self.machine.tape[1]))
            self.lblTape5.setText(str(self.machine.tape[2]))
            self.lblTape6.setText(str(self.machine.tape[3]))
        elif len(self.machine.tape) >= 3:
            self.lblTape3.setText(str(self.machine.tape[0]))
            self.lblTape4.setText(str(self.machine.tape[1]))
            self.lblTape5.setText(str(self.machine.tape[2]))
        elif len(self.machine.tape) >= 2:
            self.lblTape3.setText(str(self.machine.tape[0]))
            self.lblTape4.setText(str(self.machine.tape[1]))
        elif len(self.machine.tape) >= 1:
            self.lblTape3.setText(str(self.machine.tape[0]))

        app.sendPostedEvents()

    def deleteInstruction(self):
        if self.txtDeleteInstruction.text() != "":
            instruction = int(self.txtDeleteInstruction.text())
            index = instruction * 3

            if index + 2 <= len(self.str_instructions) and len(self.machine.temp_instructions) > 0:

                print "Deleting Instruction: (" + str(instruction) + ") " + str(self.machine.temp_instructions[instruction])

                self.machine.temp_instructions.pop(instruction)

                self.txtViewInstructions.setPlainText("")

                self.str_instructions.pop(index)
                self.str_instructions.pop(index)
                self.str_instructions.pop(index)

                if self.txtViewInstructions.toPlainText() == "":
                    self.txtViewInstructions.setPlainText("No Instructions Loaded, \n"
                                              "Add Instructions on the Right Side of the Window")
            self.txtDeleteInstruction.setText("")

            app.processEvents()

    def clearInstructions(self):
        self.machine.temp_instructions = []
        app.processEvents()
        self.txtViewInstructions.setPlainText("No Instructions Loaded, \n"
                                              "Add Instructions on the Right Side of the Window")

    def submit(self):

        if self.txtTape.text() == "":
            self.txtTape.setText("#")

        inputtape = str(self.txtTape.text())

        self.machine.setTape(inputtape)

        self.fillTape()

        app.processEvents()
        
        self.txtTape.setText("")
        print "Current Tape: ", self.machine.tape

    def reset_tape(self):
        self.lblTape0.setText("#")
        self.lblTape1.setText("#")
        self.lblTape2.setText("#")
        self.lblTape3.setText("#")
        self.lblTape4.setText("#")
        self.lblTape5.setText("#")
        self.lblTape6.setText("#")
        self.lblTape7.setText("#")
        self.machine.tape_position = 0
        self.machine.tape = []
        #GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]  # positions of the tape, which will change depending on left or right

        self.lblScannedState.setText("N/A")
        self.lblScannedSymbol.setText("N/A")
        self.lblDirection.setText("N/A")
        self.lblNewSymbol.setText("N/A")
        self.lblNewState.setText("N/A")

        QtGui.QApplication.processEvents()

    def final_tape(self):

        finaltapestr = ""

        while self.machine.tape[0] == "#":
            self.machine.tape.pop(0)
            if self.machine.tape[0] != "#":
                break

        while self.machine.tape[-1] == "#":
            self.machine.tape.pop(-1)
            if self.machine.tape[-1] != "#":
                break

        for index in range (len(self.machine.tape)):
            finaltapestr += "[" + str(self.machine.tape[index]) + "] "

        msgTape = QtGui.QMessageBox()
        msgTape.setWindowTitle("Final Tape")
        msgTape.setText("<b>" + finaltapestr + "</b>")
        msgTape.setStandardButtons(QtGui.QMessageBox.Ok)
        msgTape.exec_()

    def setInstruction(self):
        templist = []
        self.machine.saveInstruction(
            str(self.txtScannedState.text()),
            str(self.txtScannedSymbol.text()),
            str(self.cbDirection.currentText()),
            str(self.txtNewSymbol.text()),
            str(self.txtNewState.text()))

        self.str_instructions.append("Scanned State: " + str(self.txtScannedState.text()) + "   " +
                                     "Scanned Symbol: " + str(self.txtScannedSymbol.text()) + "   ")
        self.str_instructions.append("Direction: " + str(self.cbDirection.currentText()))
        self.str_instructions.append("New Symbol: " + str(self.txtNewSymbol.text()) + "   " +
                                     "New State: " + str(self.txtNewState.text()))

        self.txtScannedState.setText("")
        self.txtScannedSymbol.setText("")
        self.txtDirection.setText("")
        self.txtNewSymbol.setText("")
        self.txtNewState.setText("")

        self.txtViewInstructions.setPlainText("")
        index = 0
        instruction_number = 0

        while index != len(self.str_instructions):
            self.txtViewInstructions.append("INSTRUCTION: " + str(instruction_number) + ":")

            self.txtViewInstructions.append(str(self.str_instructions[index]))
            self.txtViewInstructions.append(str(self.str_instructions[index + 1]))
            self.txtViewInstructions.append(str(self.str_instructions[index + 2]))
            self.txtViewInstructions.append("---------------------------------------------------------")
            index += 3
            instruction_number += 1

        app.processEvents()

        print "Current Instructions: " + str(self.machine.temp_instructions)

class ExamplesWindow(QtGui.QMainWindow):
    pass

class HomeWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        super(HomeWindow, self).__init__()
        self.setGeometry(700, 400, 350, 185)
        self.setFixedSize(350, 185)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)
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
    app = QtGui.QApplication(sys.argv)
                                        # defined app here
    GUI = HomeWindow()
    sys.exit(app.exec_())