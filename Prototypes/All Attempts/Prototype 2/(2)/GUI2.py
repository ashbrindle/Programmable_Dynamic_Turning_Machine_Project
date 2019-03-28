from Tkinter import *
import tkMessageBox
import sys
from time import sleep

class State:    # manages each state of the machine and executing the instruction associated with the state
    instructions = []       # a list of instructions associated with the current state
    current_context = None  # current context object used to access the Turing Machine

    def __init__(self, context):
        self.current_context = context  # sets the current context of the machine
        self.instructions = []  # sets the instructions to empty
        self.start_of_machine = True    # states that the machine is in its first cycle (just started)

    def executeInstruction(self):
        for index in range(len(self.instructions)): # used to cycle through the instructions until one is found which matches both the current symbol and state
            if self.current_context.tape_position == len(self.current_context.tape):
                break
            if self.instructions[index].symbol == self.current_context.tape[self.current_context.tape_position]:
                app.lblScannedState.config(text = str(self.current_context.state_name)) # these lines will slowly show the instruction to help with readability when running
                sleep(0.5)  # 0.5s sleep
                root.update()   # updates the GUI
                app.lblScannedSymbol.config(text = str(self.instructions[index].symbol))
                sleep(0.5)
                root.update()
                app.lblDirection.config(text = str(self.instructions[index].direction))
                sleep(0.5)
                root.update()
                app.lblNewSymbol.config(text = str(self.instructions[index].new_symbol))
                sleep(0.5)
                root.update()
                app.lblNewState.config(text = str(self.instructions[index].next_state))
                sleep(0.5)
                root.update()
                sleep(1)

                self.current_context.tape[self.current_context.tape_position] = self.instructions[index].new_symbol # changes the symbol on the tape to the one specified from the instruction
                print "New Symbol:", self.instructions[index].new_symbol

                if self.instructions[index].direction == 'R':
                    print "Right"
                    self.current_context.moveRight()    # moves the Turing Machine tape along to the right
                    app.scrollRight()   # moves the GUI tape along to the right
                    
                elif self.instructions[index].direction == 'L':
                    print "Left"
                    self.current_context.moveLeft()    # moves the Turing Machine tape along to the right
                    app.scrollLeft()   # moves the GUI tape along to the right

                root.update()   # updates the GUI
                if self.instructions[index].next_state in self.current_context.available_states:
                    self.current_context.setState(self.instructions[index].next_state)  # sets the state to the next state specified in the instruction
                    self.current_context.state_name = self.instructions[index].next_state   # saves the name to be used in TuringMachine too
                    print "Current State: ", self.current_context.state_name
                    self.current_context.instruction_found = False  # resets instruction found so the next instruction can be found
                else:
                    self.current_context.current_state = None

                print self.current_context.tape
                break
            else:
                self.current_context.instruction_found = False
                self.current_context.current_state = None   # if no symbol matches an instruction, the state gets set to None, therefore ending the machine

    def setInstruction(self, symbol, direction, new_symbol, next_state):
        new_instruction = Instruction() # creates an instruction object
        new_instruction.symbol = symbol # and fills it with the attributes specified for the instruction
        new_instruction.direction = direction
        new_instruction.new_symbol = new_symbol
        new_instruction.next_state = next_state
        self.instructions.append(new_instruction)

class Instruction:  # attributes for each function
    symbol = ''
    direction = 'None'
    new_symbol = ''
    next_state = ''

class TuringMachine:    # The main Turing Machine which will handle the attributes of the machine, such as the tape and states (The machine will run from here)
    current_state = None    # current state object
    state_name = "" # name of the current state
    available_states = {"HALT": None}   # dict of available state objects
    tape = []   # tape list
    tape_position = 0   # current position on the tape 
    temp_instructions = []  # holds the instructions in a 2D list before they are set
    starting_state = None   # defines the current state
    instruction_found = True    # states if the instruction has been found or not

    def runMachine(self):   # runs the machine and executing the instructions through State
        print "Current Instructions: ", self.temp_instructions

        if self.starting_state == None: # checks if a starting state has been set
            print "Please Define a Starting State or Instruction"
            return  # if not, the machine does not run
        elif len(self.tape) == 0:   # checks the length of the tape
            print "Please Provide a Tape"
            return  # if no tape has been specified the machine will not run

        for instruction in self.temp_instructions:  # cycles through the instruction 2D list and sets the instructions to the states
            if instruction[0] not in self.available_states: # checks if the state has already been defined
                self.available_states[instruction[0]] = State(self) # if it has not, an object will be created
            self.available_states[instruction[0]].setInstruction(instruction[1], instruction[2], instruction[3], instruction[4])    # then the instruction will be added to that state

        self.current_state = self.available_states[self.starting_state] # sets the current state to the specified starting state
        self.state_name = self.starting_state   # and sets the string name

        while self.state_name is not 'HALT': # if an instruction has been found and the machine is not in an HALT state, the machine will continue to run
            if self.current_state == None:
                break
            self.executeInstruction()   # executes the instruction
        app.finalTapePopup()    # once the machine has finished, the popup will appear to show the final tape

    def moveRight(self):    # handles moving right on the tape
        self.tape_position += 1 # moves along once to the right of the tape
        self.tape.append("#")   # a # will be added to the end to stop any out of range errors by the GUI

    def moveLeft(self): # handles moving left on the tape
        self.tape_position -= 1 # moves along once to the left of the tape
        self.tape = ["#"] + self.tape   # the machine will add a # to the start of the tape to stop any out of rang errors by the GUI

    def saveInstruction(self, state, symbol, direction, new_symbol, next_state):    # saves an instruction to the 2D list
        current_instruction = [state, symbol, direction, new_symbol, next_state]    # creates a temp list to save to the 2D list of instructions
        self.temp_instructions.append(current_instruction)  # adds this list to the list of instructions

    def setTape(self, tape):    # saves the specified tape
        self.tape = (tape.split(","))   # using comma seperation, the tape will be split from the symbols inbetween each comma
        while len(self.tape) < 8:   # if the machine does nto meet the required length 
            self.tape.append("#")   # the machine will fill the tape with blank symbols (all blank symbols will be removed at the end of the machine)

    def setState(self, state):  # sets the current state
        self.current_state = self.available_states[state]   # sets the current state to the state passed in

    def executeInstruction(self):   # executes the State instruction
        self.current_state.executeInstruction() # executes the State executeInstruction() depending on the specified state

class CustomTapeWindow:
    def __init__(self, window):
        self.tape_font = ("times", 20)
        self.instruction_font = ("times", 20)
        self.addInstruction_font = ("times", 15)
        self.currentInstruction_font = ("times", 10)
        self.arrow_font = ("calibri", 10, "bold")
        self.run_font = ("bold")
        self.submitTape_font = ("calibri", 10, "bold")
        self.title_font = ("calibri", 12, "italic")
        self.machine = TuringMachine()
        self.str_instructions = []
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
        self.drawWindow()

    def drawWindow(self):

        self.lblTapeTitle = Label(
            root,
            text = "Insert Tape: (Comma Seperated)",
            font = self.title_font)
        self.lblTapeTitle.pack()
        self.lblTapeTitle.place(x = 302, y = 158)

        self.lblTape0 = Label(
            root, 
            text= "#",
            bg = "LightSteelBlue1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape0.pack()
        self.lblTape0.place(x = 302, y = 237)

        self.lblTape1 = Label(
            root, 
            text="#",
            bg = "LightSteelBlue1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape1.pack()
        self.lblTape1.place(x = 382, y = 237)

        self.lblTape2 = Label(
            root, 
            text="#",
            bg = "LightSteelBlue1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape2.pack()
        self.lblTape2.place(x = 462, y = 237)

        self.lblTape3 = Label(
            root, 
            text="#",
            bg = "DarkOliveGreen3",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape3.pack()
        self.lblTape3.place(x = 542, y = 237)

        self.lblTape4 = Label(
            root, 
            text="#",
            bg = "LightSteelBlue1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape4.pack()
        self.lblTape4.place(x = 622, y = 237)

        self.lblTape5 = Label(
            root, 
            text="#",
            bg = "LightSteelBlue1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape5.pack()
        self.lblTape5.place(x = 702, y = 237)

        self.lblTape6 = Label(
            root, 
            text="#",
            bg = "LightSteelBlue1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape6.pack()
        self.lblTape6.place(x = 782, y = 237)

        self.lblTape7 = Label(
            root, 
            text="#",
            bg = "LightSteelBlue1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape7.pack()
        self.lblTape7.place(x = 862, y = 237)

        self.lblAddInstructionTitle = Label(
            root,
            text = "Add a Instruction:",
            font = self.title_font)
        self.lblAddInstructionTitle.pack()
        self.lblAddInstructionTitle.place(x = 10, y = -1)

        self.lblInstructionsTitle = Label(
            root,
            text = "Running Instruction:",
            font = self.title_font)
        self.lblInstructionsTitle.pack()
        self.lblInstructionsTitle.place(x = 958, y = -1)

        self.lblInstructionsBorder = Label(
            root, 
            text= "Scanned State: \n\n"
                                    "Scanned Symbol: \n\n"
                                    "Direction: \n\n"
                                    "New Symbol: \n\n"
                                    "New State:",
            bg = "white",
            fg = "black",
            font = self.instruction_font,
            height = 9,
            width = 18,
            borderwidth = 2,
            relief = "solid",
            justify = LEFT,
            anchor = "w")
        self.lblInstructionsBorder.pack()
        self.lblInstructionsBorder.place(x = 958, y = 20)

        self.lblScannedState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.currentInstruction_font,
            height = 2,
            width = 7)
        self.lblScannedState.pack()
        self.lblScannedState.place(x = 1148, y = 28)

        self.lblScannedSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.currentInstruction_font,
            height = 2,
            width = 7)
        self.lblScannedSymbol.pack()
        self.lblScannedSymbol.place(x = 1148, y = 85)

        self.lblDirection = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.currentInstruction_font,
            height = 2,
            width = 7)
        self.lblDirection.pack()
        self.lblDirection.place(x = 1148, y = 146)

        self.lblNewSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.currentInstruction_font,
            height = 2,
            width = 7)
        self.lblNewSymbol.pack()
        self.lblNewSymbol.place(x = 1148, y = 207)

        self.lblNewState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.currentInstruction_font,
            height = 2,
            width = 7)
        self.lblNewState.pack()
        self.lblNewState.place(x = 1148, y = 264)

        self.lblAddInstructionsBorder = Label(
            root, 
            text= "Scanned State: \n\n"
                                    "Scanned Symbol: \n\n"
                                    "Direction: \n\n"
                                    "New Symbol: \n\n"
                                    "New State:",
            bg = "white",
            fg = "black",
            font = self.instruction_font,
            height = 9,
            width = 18,
            borderwidth = 2,
            relief = "solid",
            justify = LEFT,
            anchor = "w")
        self.lblAddInstructionsBorder.pack()
        self.lblAddInstructionsBorder.place(x = 0, y = 20)

        self.txtScannedState = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtScannedState.pack()
        self.txtScannedState.place(x = 195, y = 28)

        self.txtScannedSymbol = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtScannedSymbol.pack()
        self.txtScannedSymbol.place(x = 195, y = 85)

        self.txtDirection = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtDirection.pack()
        self.txtDirection.place(x = 195, y = 146)

        self.txtNewSymbol = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtNewSymbol.pack()
        self.txtNewSymbol.place(x = 195, y = 207)

        self.txtNewState = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtNewState.pack()
        self.txtNewState.place(x = 195, y = 270)

        self.btnSaveInstruction = Button(
            root,
            text = "Save Instruction",
            command = self.saveInstruction,
            bg = "green4",
            fg = "white",
            font = self.arrow_font,
            height = 1,
            width = 20,
            borderwidth = 1,
            relief = "solid")
        self.btnSaveInstruction.pack()
        self.btnSaveInstruction.place(x = 65, y = 310)

        self.btnRight = Button(
            root,
            text = "--------->",
            command = self.scrollRight,
            bg = "DarkGoldenrod3",
            fg = "white",
            font = self.arrow_font,
            height = 1,
            width = 10,
            borderwidth = 1,
            relief = "solid")
        self.btnRight.pack()
        self.btnRight.place(x = 854, y = 207)

        self.btnLeft = Button(
            root,
            text = "<---------",
            command = self.scrollLeft,
            bg = "DarkGoldenrod3",
            fg = "white",
            font = self.arrow_font,
            height = 1,
            width = 10,
            borderwidth = 1,
            relief = "solid")
        self.btnLeft.pack()
        self.btnLeft.place(x = 302, y = 207)

        self.txtStartingStateTitle = Label(
            root,
            text = "Starting State:",
            font = self.title_font)
        self.txtStartingStateTitle.pack()
        self.txtStartingStateTitle.place(x = 550, y = 145)

        self.txtStartingState = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtStartingState.pack()
        self.txtStartingState.place(x = 650, y = 145)

        self.btnStartingState = Button(
            root,
            text = "Submit State",
            command = self.setStartingState,
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 12,
            borderwidth = 1,
            relief = "solid")
        self.btnStartingState.pack()
        self.btnStartingState.place(x = 732, y = 146)

        self.btnRun = Button(
            root,
            text = "Run",
            command = self.runMachine,
            bg = "green4",
            fg = "white",
            height = 1,
            width = 64,
            borderwidth = 1,
            relief = "solid")
        self.btnRun.pack()
        self.btnRun.place(x = 389, y = 207)

        self.txtTape = Text(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 74,
            borderwidth = 1,
            relief = "solid")
        self.txtTape.pack()
        self.txtTape.place(x = 302, y = 180)

        self.btnTape = Button(
            root,
            text = "Submit Tape",
            command = self.submitTape,
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 13,
            borderwidth = 1,
            relief = "solid")
        self.btnTape.pack()
        self.btnTape.place(x = 834, y = 177)

        self.lblAddInstructionTitle = Label(
            root,
            text = "Current Instruction(s):",
            font = self.title_font)
        self.lblAddInstructionTitle.pack()
        self.lblAddInstructionTitle.place(x = 302, y = -1)

        self.instructionsFrame = Frame(
            root,
            borderwidth = 1,
            relief = "solid")
        self.instructionsFrame.pack()
        self.instructionsFrame.place(x = 302, y = 20)

        self.scrlInstructions = Scrollbar(self.instructionsFrame)
        self.scrlInstructions.pack(side = "right", fill = "y")

        self.lstShowInstructions = Listbox(
            self.instructionsFrame,
            bg = "white",
            yscrollcommand = self.scrlInstructions.set,
            fg = "black",
            height = 7,
            width = 83)
        self.lstShowInstructions.pack(side = "left", fill = "y")
        self.scrlInstructions.config(command = self.lstShowInstructions.yview)
        self.lstShowInstructions.insert(0, "No Instructions Loaded, \n"
                                              "Add Instructions on the Right Side of the Window")

        self.lblDeleteTitle = Label(
            root,
            text = "Delete:",
            font = self.title_font)
        self.lblDeleteTitle.pack()
        self.lblDeleteTitle.place(x = 836, y = 0)
        self.lblDeleteTitle2 = Label(
            root,
            text = "(Enter Number)",
            font = self.title_font)
        self.lblDeleteTitle2.pack()
        self.lblDeleteTitle2.place(x = 836, y = 20)

        self.txtDeleteInstruction = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            width = 13,
            borderwidth = 1,
            relief = "solid")
        self.txtDeleteInstruction.pack()
        self.txtDeleteInstruction.place(x = 836, y = 50)

        self.btnDeleteInstruction = Button(
            root,
            text = "Delete \n Instruction",
            command = self.deleteInstruction,
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            height = 2,
            width = 13,
            borderwidth = 1,
            relief = "solid")
        self.btnDeleteInstruction.pack()
        self.btnDeleteInstruction.place(x = 834, y = 75)

        self.btnDeleteAllInstructions = Button(
            root,
            text = "Clear All \n Instructions",
            command = self.clearInstructions,
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            height = 2,
            width = 13,
            borderwidth = 1,
            relief = "solid")
        self.btnDeleteAllInstructions.pack()
        self.btnDeleteAllInstructions.place(x = 834, y = 120)

        self.txtTape.focus()

    def runMachine(self):
        if self.machine.starting_state == None and len(self.machine.temp_instructions) > 0:
            self.machine.starting_state = self.machine.temp_instructions[0][0]
        print "Starting State: ", self.machine.starting_state
        print "Starting Tape: ", self.machine.tape
        self.machine.runMachine()

    def scrollLeft(self):
        if len(self.machine.tape) > 0:
            print "LEFT"
            if self.machine.tape_position > 0:
                self.machine.tape_position -= 1

            for index in range(len(self.GUI_tape_positions)):
                self.GUI_tape_positions[index] -= 1

            if self.GUI_tape_positions[3] == -1:
                for index in range(len(self.GUI_tape_positions)):
                    self.GUI_tape_positions[index] += 1

            if self.GUI_tape_positions[3] > -1:
                if self.GUI_tape_positions[0] > -1:
                    self.lblTape0.config(text = str(self.machine.tape[self.GUI_tape_positions[0]]))
                else:
                    self.lblTape0.config(text = "#")
                if self.GUI_tape_positions[1] > -1:
                    self.lblTape1.config(text = str(self.machine.tape[self.GUI_tape_positions[1]]))
                else:
                    self.lblTape1.config(text = "#")
                if self.GUI_tape_positions[2] > -1:
                    self.lblTape2.config(text = str(self.machine.tape[self.GUI_tape_positions[2]]))
                else:
                    self.lblTape2.config(text = "#")
                if self.GUI_tape_positions[3] < len(self.machine.tape):
                    self.lblTape3.config(text = str(self.machine.tape[self.GUI_tape_positions[3]]))
                else:
                    self.lblTape3.config(text = "#")
                if self.GUI_tape_positions[4] < len(self.machine.tape):
                    self.lblTape4.config(text = str(self.machine.tape[self.GUI_tape_positions[4]]))
                else:
                    self.lblTape4.config(text = "#")
                if self.GUI_tape_positions[5] < len(self.machine.tape):
                    self.lblTape5.config(text = str(self.machine.tape[self.GUI_tape_positions[5]]))
                else:
                    self.lblTape5.config(text = "#")
                if self.GUI_tape_positions[6] < len(self.machine.tape):
                    self.lblTape6.config(text = str(self.machine.tape[self.GUI_tape_positions[6]]))
                else:
                    self.lblTape6.config(text = "#")
                if self.GUI_tape_positions[7] < len(self.machine.tape):
                    self.lblTape7.config(text = str(self.machine.tape[self.GUI_tape_positions[7]]))
                else:
                    self.lblTape7.config(text = "#")

    def scrollRight(self):
        if len(self.machine.tape) > 0:
            print "RIGHT"

            for index in range(len(self.GUI_tape_positions)):
                self.GUI_tape_positions[index] += 1

            if self.GUI_tape_positions[0] < len(self.machine.tape):
                self.lblTape0.config(text = str(self.machine.tape[self.GUI_tape_positions[0]]))
            else:
                self.lblTape0.config(text = "#")
            if self.GUI_tape_positions[1] < len(self.machine.tape):
                self.lblTape1.config(text = str(self.machine.tape[self.GUI_tape_positions[1]]))
            else:
                self.lblTape1.config(text = "#")
            if self.GUI_tape_positions[2] < len(self.machine.tape):
                self.lblTape2.config(text = str(self.machine.tape[self.GUI_tape_positions[2]]))
            else:
                self.lblTape2.config(text = "#")
            if self.GUI_tape_positions[3] < len(self.machine.tape):
                self.lblTape3.config(text = str(self.machine.tape[self.GUI_tape_positions[3]]))
            else:
                self.lblTape3.config(text = "#")
            if self.GUI_tape_positions[4] < len(self.machine.tape):
                self.lblTape4.config(text = str(self.machine.tape[self.GUI_tape_positions[4]]))
            else:
                self.lblTape4.config(text = "#")
            if self.GUI_tape_positions[5] < len(self.machine.tape):
                self.lblTape5.config(text = str(self.machine.tape[self.GUI_tape_positions[5]]))
            else:
                self.lblTape5.config(text = "#")
            if self.GUI_tape_positions[6] < len(self.machine.tape):
                self.lblTape6.config(text = str(self.machine.tape[self.GUI_tape_positions[6]]))
            else:
                self.lblTape6.config(text = "#")
            if self.GUI_tape_positions[7] < len(self.machine.tape):
                self.lblTape7.config(text = str(self.machine.tape[self.GUI_tape_positions[7]]))
            else:
                self.lblTape7.config(text = "#")

            if self.GUI_tape_positions[3] > len(self.machine.tape):
                for index in range(len(self.GUI_tape_positions)):
                    self.GUI_tape_positions[index] -= 1

    def submitTape(self):
        if self.txtTape.get("1.0", END) == "":
            self.txtTape.insert(END, "#")

        input_tape = str(self.txtTape.get("1.0", END))
        input_tape = input_tape[:-1]

        self.machine.setTape(input_tape)

        self.fillTape()

        self.txtTape.delete('1.0', END)
        print "Current Tape: ", self.machine.tape    

    def resetMachine(self):
        self.lblTape0.config(text = "#")
        self.lblTape1.config(text = "#")
        self.lblTape2.config(text = "#")
        self.lblTape3.config(text = "#")
        self.lblTape4.config(text = "#")
        self.lblTape5.config(text = "#")
        self.lblTape6.config(text = "#")
        self.lblTape7.config(text = "#")
        self.machine.tape_position = 0
        self.machine.tape = []
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]  # positions of the tape, which will change depending on left or right
        self.machine.available_states = {}
        self.machine.temp_instructions = []
        self.machine.state_name = ""
        self.machine.starting_state = None
        self.machine.current_state = None

        self.lblScannedState.config(text = "N/A")
        self.lblScannedSymbol.config(text = "N/A")
        self.lblDirection.config(text = "N/A")
        self.lblNewSymbol.config(text = "N/A")
        self.lblNewState.config(text = "N/A")

        self.clearInstructions()
        
        root.update()

    def fillTape(self):
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
        self.lblTape0.config(text = "#")
        self.lblTape1.config(text = "#")
        self.lblTape2.config(text = "#")
        self.lblTape3.config(text = "#")
        self.lblTape4.config(text = "#")
        self.lblTape5.config(text = "#")
        self.lblTape6.config(text = "#")
        self.lblTape7.config(text = "#")

        if len(self.machine.tape) >= 5:
            self.lblTape3.config(text = str(self.machine.tape[0]))
            self.lblTape4.config(text = str(self.machine.tape[1]))
            self.lblTape5.config(text = str(self.machine.tape[2]))
            self.lblTape6.config(text = str(self.machine.tape[3]))
            self.lblTape7.config(text = str(self.machine.tape[4]))
        elif len(self.machine.tape) >= 4:
            self.lblTape3.config(text = str(self.machine.tape[0]))
            self.lblTape4.config(text = str(self.machine.tape[1]))
            self.lblTape5.config(text = str(self.machine.tape[2]))
            self.lblTape6.config(text = str(self.machine.tape[3]))
        elif len(self.machine.tape) >= 3:
            self.lblTape3.config(text = str(self.machine.tape[0]))
            self.lblTape4.config(text = str(self.machine.tape[1]))
            self.lblTape5.config(text = str(self.machine.tape[2]))
        elif len(self.machine.tape) >= 2:
            self.lblTape3.config(text = str(self.machine.tape[0]))
            self.lblTape4.config(text = str(self.machine.tape[1]))
        elif len(self.machine.tape) >= 1:
            self.lblTape3.config(text = str(self.machine.tape[0]))

    def finaliseTape(self):
        finaltapestr = ""

        while self.machine.tape == "#":
            self.machine.tape.pop(0)
            if self.machine.tape[0] != "#":
                break
        if len(self.machine.tape) > 1:
            while self.machine.tape[-1] == "#":
                self.machine.tape.pop(-1)
                if self.machine.tape[-1] != "#":
                    break

        for index in range (len(self.machine.tape)):
            finaltapestr += "[" + str(self.machine.tape[index]) + "] "
        return finaltapestr

    def saveInstruction(self):
        temp_list = []
        self.machine.saveInstruction(
            str(self.txtScannedState.get()),
            str(self.txtScannedSymbol.get()),
            str(self.txtDirection.get()),
            str(self.txtNewSymbol.get()),
            str(self.txtNewState.get()))

        self.str_instructions.append("Scanned State: " + str(self.txtScannedState.get()))
        self.str_instructions.append("Scanned Synbol: " + str(self.txtScannedSymbol.get()))
        self.str_instructions.append("Direction: " + str(self.txtDirection.get()))
        self.str_instructions.append("New Symbol: " + str(self.txtNewSymbol.get()))
        self.str_instructions.append("New State: " + str(self.txtNewState.get()))

        self.txtScannedState.delete("0", END)
        self.txtScannedSymbol.delete("0", END)
        self.txtDirection.delete("0", END)
        self.txtNewSymbol.delete("0", END)
        self.txtNewState.delete("0", END)

        self.fillInstructions()
        self.txtScannedState.focus()

    def fillInstructions(self):
        if self.lstShowInstructions.size() != 0:

            self.lstShowInstructions.delete(0, END)
            index = 0
            instruction_number = 0

            while index != len(self.str_instructions):
                self.lstShowInstructions.insert(END, "\n INSTRUCTION: " + str(instruction_number) + ": \n")
                self.lstShowInstructions.insert(END, str(self.str_instructions[index]))
                self.lstShowInstructions.insert(END, str(self.str_instructions[index + 1]))
                self.lstShowInstructions.insert(END, str(self.str_instructions[index + 2]))
                self.lstShowInstructions.insert(END, str(self.str_instructions[index + 3]))
                self.lstShowInstructions.insert(END, str(self.str_instructions[index + 4]))
                self.lstShowInstructions.insert(END, "---------------------------------------------------------")
                index += 5
                instruction_number += 1

    def deleteInstruction(self):

        instruction = self.txtDeleteInstruction.get()
        if len(instruction) != 0:

            if isinstance(instruction, int) == False:
                print "Please Enter an Integer"
                self.txtDeleteInstruction.delete("0", END)
                return

            index = instruction * 5

            if index + 4 <= len(self.str_instructions) and len(self.machine.temp_instructions) > 0:
                print "Deleteing Instruction: (" + str(instruction) + ") " + str (self.machine.temp_instructions[instruction])
                self.machine.temp_instructions.pop(instruction)
                self.lstShowInstructions.delete(0, END)
                print "Current Instructions:", self.machine.temp_instructions

                self.str_instructions.pop(index)
                self.str_instructions.pop(index)
                self.str_instructions.pop(index)
                self.str_instructions.pop(index)
                self.str_instructions.pop(index)
                
                if len(self.str_instructions) >= 5:
                    self.lstShowInstructions.delete(0, END)
                    strindex = 0
                    instruction_number = 0
                    while strindex != len(self.str_instructions):
                        self.lstShowInstructions.insert(END, "\n INSTRUCTION: " + str(instruction_number) + ": \n")
                        self.lstShowInstructions.insert(END, str(self.str_instructions[strindex]))
                        self.lstShowInstructions.insert(END, str(self.str_instructions[strindex + 1]))
                        self.lstShowInstructions.insert(END, str(self.str_instructions[strindex + 2]))
                        self.lstShowInstructions.insert(END, str(self.str_instructions[strindex + 3]))
                        self.lstShowInstructions.insert(END, str(self.str_instructions[strindex + 4]))
                        self.lstShowInstructions.insert(END, "---------------------------------------------------------")
                        strindex += 5
                        instruction_number += 1

                if self.lstShowInstructions.size() == 0:
                    self.lstShowInstructions.insert(
                        0, "No Instructions Loaded, \n Add Instructions on the Left Side of the Window")
            self.txtDeleteInstruction.delete("0", END)

    def clearInstructions(self):
        self.lstShowInstructions.delete(0, END)
        self.machine.available_states = {}
        self.machine.temp_instructions = []
        root.update()
        self.lstShowInstructions.insert(0, "No Instructions Loaded, \n"
                                              "Add Instructions on the Right Side of the Window")
        print self.machine.temp_instructions

    def setStartingState(self):
        if str(self.txtStartingState.get()) != "":
            self.machine.starting_state = str(self.txtStartingState.get())
            print "starting State set to: ", self.machine.starting_state

    def finalTapePopup(self):

        finaltape_str = self.finaliseTape()

        popup_finaltape = Toplevel()
        popup_finaltape.title("Final Tape")
        popup_finaltape.geometry("300x150+750+250")
        if self.machine.instruction_found == False:
            lblInstructionFound = Label(popup_finaltape, text = "Machine Halt \n Because No Instruction Present \n for the Current Context of the Turing Machine")
            lblInstructionFound.pack()
        elif self.machine.instruction_found == True:
            lblInstructionFound = Label(popup_finaltape, text = "Machine Halt \n Because of Transition to HALT State")
            lblInstructionFound.pack()

        lblFinalTape = Label(popup_finaltape, text = finaltape_str)
        lblFinalTape.pack()

        btnDismiss = Button(popup_finaltape, text="Dismiss Window", command = popup_finaltape.destroy)
        btnDismiss.pack()

        btnDismiss.focus()

        self.resetMachine()

if __name__ == "__main__":
    root = Tk()
    app = CustomTapeWindow(root)
    root.geometry("1235x345+250+250")
    root.mainloop()