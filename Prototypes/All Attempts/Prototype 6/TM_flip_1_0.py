from State import State, StateContext
from time import sleep
import sys
from Tkinter import *
import tkMessageBox


class TuringMachineGUI():
    def __init__(self, window):
        self.tape_font = ("times", 20)
        self.position_font = ("times", 15, "italic")
        self.instruction_font = ("times", 15)
        self.addInstruction_font = ("times", 10)
        self.dropdown_font = ("times", 10)
        self.currentInstruction_font = ("times", 10)
        self.arrow_font = ("calibri", 10, "bold")
        self.run_font = ("bold")
        self.submitTape_font = ("calibri", 10, "bold")
        self.run_font = ("calibri", 15, "bold")
        self.title_font = ("times", 15)
        self.title2_font = ("times", 11)

        self.tape = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        self.tape_position = 0
        self.starting_state = "A"

        self.list_instructions = [
                    "State   Symbol   Dir   New Symbol   New State", 
                    "A        1             R      0                     B", 
                    "A        END       R      END               HALT", 
                    "-----------------------------------------------------",
                    "B        0             R      1                     A", 
                    "B        END       R      END               HALT"]

        self.tape_options = [
            "Empty Tape",
            "[0, 1, 0, 1, 0, 1, 0, END]"]

        self.tapes = {
            "Empty Tape": ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            "[0, 1, 0, 1, 0, 1, 0, END]": ["0","1", "0", "1", "0", "1", "0", "END"]
        }
        self.starting_states = {
            "Empty Tape": "A",
            "[0, 1, 0, 1, 0, 1, 0, END]": "A"}

        self.tape_positions = {
            "Empty Tape": 0,
            "[0, 1, 0, 1, 0, 1, 0, END]": 0}

        self.str_instructions = []
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
        self.drawWindow()

    def drawWindow(self):

        self.lblPositions = Label(
            root,
            text= "-3             -2             -1             0              1              2              3              4",
            fg = "gray26",
            font = self.position_font)
        self.lblPositions.pack()
        self.lblPositions.place(x = 80, y = 5)

        self.lblTape0 = Label(
            root,
            text= "#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape0.pack()
        self.lblTape0.place(x = 62, y = 30)

        self.lblTape1 = Label(
            root,
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape1.pack()
        self.lblTape1.place(x = 142, y = 30)

        self.lblTape2 = Label(
            root,
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape2.pack()
        self.lblTape2.place(x = 222, y = 30)

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
        self.lblTape3.place(x = 302, y = 30)

        self.lblTape4 = Label(
            root,
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape4.pack()
        self.lblTape4.place(x = 382, y = 30)

        self.lblTape5 = Label(
            root,
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape5.pack()
        self.lblTape5.place(x = 462, y = 30)

        self.lblTape6 = Label(
            root,
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape6.pack()
        self.lblTape6.place(x = 542, y = 30)

        self.lblTape7 = Label(
            root,
            text="#",
            bg = "DarkSeaGreen1",
            fg = "black",
            font = self.tape_font,
            height = 2,
            width = 4,
            borderwidth = 2,
            relief = "solid")
        self.lblTape7.pack()
        self.lblTape7.place(x = 622, y = 30)

        self.lblSelectTapeTitle = Label(
            root,
            text = "Select Machine Tape:",
            font = self.title_font)
        self.lblSelectTapeTitle.pack()
        self.lblSelectTapeTitle.place(x = 468, y = 115)

        self.selected_tape = StringVar()
        self.selected_tape.set(self.tape_options[0])
        self.optTape = OptionMenu(
            root,
            self.selected_tape,
            *self.tape_options,
            command = self.selections)
        self.optTape.pack()
        self.optTape.config(
            bg = "white",
            fg = "black",
            font = self.dropdown_font,
            width = 36,
            borderwidth = 1,
            relief = "solid",
            justify = LEFT)
        self.optTape["menu"].config(
            bg = "white",
            fg = "black",
            font = self.dropdown_font,
            borderwidth = 1,
            relief = "solid")
        self.optTape.place(x = 468, y = 143)

        self.lblInstructionsTitle = Label(
            root,
            text = "Running Instruction:",
            font = self.title_font)
        self.lblInstructionsTitle.pack()
        self.lblInstructionsTitle.place(x = 468, y = 293)

        self.lblInstructionsBorder = Label(
            root,
            text= "Scanned State: \n"
                                    "Scanned Symbol: \n"
                                    "Direction: \n"
                                    "New Symbol: \n"
                                    "New State:",
            bg = "white",
            fg = "black",
            font = self.instruction_font,
            height = 5,
            width = 23,
            borderwidth = 2,
            relief = "solid",
            justify = LEFT,
            anchor = "w")
        self.lblInstructionsBorder.pack()
        self.lblInstructionsBorder.place(x = 468, y = 210)

        self.lblScannedState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblScannedState.pack()
        self.lblScannedState.place(x = 665, y = 214)

        self.lblScannedSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblScannedSymbol.pack()
        self.lblScannedSymbol.place(x = 665, y = 236)

        self.lblDirection = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblDirection.pack()
        self.lblDirection.place(x = 665, y = 256)

        self.lblNewSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblNewSymbol.pack()
        self.lblNewSymbol.place(x = 665, y = 276)

        self.lblNewState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblNewState.pack()
        self.lblNewState.place(x = 665, y = 298)

        self.lblAllInstructionsTitle = Label(
            root,
            text = "All Instructions:",
            font = self.title_font)
        self.lblAllInstructionsTitle.pack()
        self.lblAllInstructionsTitle.place(x = 30, y = 115)

        self.instructionsFrame = Frame(
            root,
            borderwidth = 2,
            relief = "solid")
        self.instructionsFrame.pack()
        self.instructionsFrame.place(x = 30, y = 140)

        self.scrlInstructions = Scrollbar(self.instructionsFrame)
        self.scrlInstructions.pack(side = "right", fill = "y")

        self.lstShowInstructions = Listbox(
            self.instructionsFrame,
            bg = "white",
            yscrollcommand = self.scrlInstructions.set,
            fg = "black",
            height = 13,
            width = 40,
            font = self.instruction_font)
        self.lstShowInstructions.pack(side = "left", fill = "y")
        self.scrlInstructions.config(command = self.lstShowInstructions.yview)

        for x in range(len(self.list_instructions)):
            self.lstShowInstructions.insert(x, self.list_instructions[x])

        self.btnHelp = Button(
            root,
            text = "Help",
            bg = "DarkGoldenRod3",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 36,
            borderwidth = 1,
            relief = "solid")
        self.btnHelp.pack()
        self.btnHelp.place(x = 468, y = 375)

        self.btnRun = Button(
            root,
            text = "Run Machine",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 36,
            borderwidth = 1,
            relief = "solid",
            command = self.runMachine)
        self.btnRun.pack()
        self.btnRun.place(x = 468, y = 340)

        self.btnExit = Button(
            root,
            text = "Exit Application",
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            command = root.destroy,
            height = 1,
            width = 36,
            borderwidth = 1,
            relief = "solid")
        self.btnExit.pack()
        self.btnExit.place(x = 468, y = 410)

        self.imgStates = Canvas(root)
        self.imgStates.config(width = 6000, height = 500)
        self.photoState = PhotoImage(file = "TM_flip_1_0_State_Diagram_small.gif")
        self.imgStates.create_image(0,0, image = self.photoState, anchor="nw")
        self.imgStates.place(x = 750, y = 20)

    def selections(self, item):
        self.tape = self.tapes[item]
        self.starting_state = self.starting_states[item]
        self.tape_position = self.tape_positions[item]
        self.fillTape()
        if self.tape_position >= 0:
            for pos in range(self.tape_position):
                self.scrollRight(self.tape)
        root.update()

    def scrollLeft(self, current_tape):
        if len(current_tape) > 0:

            # for index in range(len(self.GUI_tape_positions)):
            #     self.GUI_tape_positions[index] -= 1

            if self.GUI_tape_positions[3] == -1:
                for index in range(len(self.GUI_tape_positions)):
                    self.GUI_tape_positions[index] += 1

            if self.GUI_tape_positions[3] > -1:
                if self.GUI_tape_positions[0] > -1:
                    self.lblTape0.config(text = str(current_tape[self.GUI_tape_positions[0]]))
                else:
                    self.lblTape0.config(text = "#")
                if self.GUI_tape_positions[1] > -1:
                    self.lblTape1.config(text = str(current_tape[self.GUI_tape_positions[1]]))
                else:
                    self.lblTape1.config(text = "#")
                if self.GUI_tape_positions[2] > -1:
                    self.lblTape2.config(text = str(current_tape[self.GUI_tape_positions[2]]))
                else:
                    self.lblTape2.config(text = "#")
                if self.GUI_tape_positions[3] < len(current_tape):
                    self.lblTape3.config(text = str(current_tape[self.GUI_tape_positions[3]]))
                else:
                    self.lblTape3.config(text = "#")
                if self.GUI_tape_positions[4] < len(current_tape):
                    self.lblTape4.config(text = str(current_tape[self.GUI_tape_positions[4]]))
                else:
                    self.lblTape4.config(text = "#")
                if self.GUI_tape_positions[5] < len(current_tape):
                    self.lblTape5.config(text = str(current_tape[self.GUI_tape_positions[5]]))
                else:
                    self.lblTape5.config(text = "#")
                if self.GUI_tape_positions[6] < len(current_tape):
                    self.lblTape6.config(text = str(current_tape[self.GUI_tape_positions[6]]))
                else:
                    self.lblTape6.config(text = "#")
                if self.GUI_tape_positions[7] < len(current_tape):
                    self.lblTape7.config(text = str(current_tape[self.GUI_tape_positions[7]]))
                else:
                    self.lblTape7.config(text = "#")

    def scrollRight(self, current_tape):
        if len(current_tape) > 0:

            for index in range(len(self.GUI_tape_positions)):
                self.GUI_tape_positions[index] += 1

            if self.GUI_tape_positions[0] < len(current_tape) and self.GUI_tape_positions[0] >= 0:
                self.lblTape0.config(text = str(current_tape[self.GUI_tape_positions[0]]))
            else:
                self.lblTape0.config(text = "#")
            if self.GUI_tape_positions[1] < len(current_tape) and self.GUI_tape_positions[1] >= 0:
                self.lblTape1.config(text = str(current_tape[self.GUI_tape_positions[1]]))
            else:
                self.lblTape1.config(text = "#")
            if self.GUI_tape_positions[2] < len(current_tape) and self.GUI_tape_positions[2] >= 0:
                self.lblTape2.config(text = str(current_tape[self.GUI_tape_positions[2]]))
            else:
                self.lblTape2.config(text = "#")
            if self.GUI_tape_positions[3] < len(current_tape):
                self.lblTape3.config(text = str(current_tape[self.GUI_tape_positions[3]]))
            else:
                self.lblTape3.config(text = "#")
            if self.GUI_tape_positions[4] < len(current_tape):
                self.lblTape4.config(text = str(current_tape[self.GUI_tape_positions[4]]))
            else:
                self.lblTape4.config(text = "#")
            if self.GUI_tape_positions[5] < len(current_tape):
                self.lblTape5.config(text = str(current_tape[self.GUI_tape_positions[5]]))
            else:
                self.lblTape5.config(text = "#")
            if self.GUI_tape_positions[6] < len(current_tape):
                self.lblTape6.config(text = str(current_tape[self.GUI_tape_positions[6]]))
            else:
                self.lblTape6.config(text = "#")
            if self.GUI_tape_positions[7] < len(current_tape):
                self.lblTape7.config(text = str(current_tape[self.GUI_tape_positions[7]]))
            else:
                self.lblTape7.config(text = "#")

            if self.GUI_tape_positions[3] > len(current_tape):
                for index in range(len(self.GUI_tape_positions)):
                    self.GUI_tape_positions[index] -= 1

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

        if len(self.tape) >= 5:
            self.lblTape3.config(text = str(self.tape[0]))
            self.lblTape4.config(text = str(self.tape[1]))
            self.lblTape5.config(text = str(self.tape[2]))
            self.lblTape6.config(text = str(self.tape[3]))
            self.lblTape7.config(text = str(self.tape[4]))
        elif len(self.tape) >= 4:
            self.lblTape3.config(text = str(self.tape[0]))
            self.lblTape4.config(text = str(self.tape[1]))
            self.lblTape5.config(text = str(self.tape[2]))
            self.lblTape6.config(text = str(self.tape[3]))
        elif len(self.tape) >= 3:
            self.lblTape3.config(text = str(self.tape[0]))
            self.lblTape4.config(text = str(self.tape[1]))
            self.lblTape5.config(text = str(self.tape[2]))
        elif len(self.tape) >= 2:
            self.lblTape3.config(text = str(self.tape[0]))
            self.lblTape4.config(text = str(self.tape[1]))
        elif len(self.tape) >= 1:
            self.lblTape3.config(text = str(self.tape[0]))

    def finaliseTape(self):
        finaltapestr = ""

        while self.TM.tape[0] == "#":
            self.TM.tape.pop(0)
            if self.TM.tape[0] != "#":
                break
        if len(self.TM.tape) > 1:
            while self.TM.tape[-1] == "#":
                self.TM.tape.pop(-1)
                if self.TM.tape[-1] != "#":
                    break

        for index in range (len(self.TM.tape)):
            finaltapestr += "[" + str(self.TM.tape[index]) + "] "
        return finaltapestr

    def runMachine(self):
        self.TM = TuringMachine(self.starting_state, self.tape, self.tape_position)
        root.update()
        self.TM.runMachine()

    def resetMachine(self):
        self.lblTape0.config(text = "#")
        self.lblTape1.config(text = "#")
        self.lblTape2.config(text = "#")
        self.lblTape3.config(text = "#")
        self.lblTape4.config(text = "#")
        self.lblTape5.config(text = "#")
        self.lblTape6.config(text = "#")
        self.lblTape7.config(text = "#")
        self.TM.tape_position = 0
        self.TM.tape = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
        self.GUI_tape_positions = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]  # positions of the tape, which will change depending on left or right

        self.lblScannedState.config(text = "N/A")
        self.lblScannedSymbol.config(text = "N/A")
        self.lblDirection.config(text = "N/A")
        self.lblNewSymbol.config(text = "N/A")
        self.lblNewState.config(text = "N/A")
        root.update()

    def finalTapePopup(self):

        finaltape_str = self.finaliseTape()

        popup_finaltape = Toplevel()
        popup_finaltape.title("Final Tape")
        popup_finaltape.geometry("300x150+750+250")
        lblInstructionFound = Label(popup_finaltape, text = "Final Tape")
        lblInstructionFound.pack()

        lblFinalTape = Label(popup_finaltape, text = finaltape_str)
        lblFinalTape.pack()

        btnDismiss = Button(popup_finaltape, text="Dismiss Window", command = popup_finaltape.destroy)
        btnDismiss.pack()

        btnDismiss.focus()

        self.resetMachine()


class Transition:
    def found0(self):
        print "Error, [0] instruction not found in current state"
        return False

    def found1(self):
        print "Error, [1] instruction not found in current state"
        return False

    def foundEND(self):
        print "Error, [#] or Blank Symbol instruction not found in current state"
        return False


class TuringStateA(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found0(self):
        print "(A) Current State"
        app.lblScannedState.config(text = "A")
        root.update()
        sleep(0.2)

        print "(0) Symbol on Tape"
        app.lblScannedSymbol.config(text = "0")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)

        self.current_context.tape[self.current_context.tape_position] = "1"
        print "(1) New Symbol on Tape"
        app.lblNewSymbol.config(text = "1")
        root.update()
        sleep(0.2)

        self.current_context.setState("B")
        print "(B) New State"
        app.lblNewState.config(text = "B")
        root.update()

        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringStateB(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def found1(self):
        print "(B) Current State"
        app.lblScannedState.config(text = "B")
        root.update()
        sleep(0.2)

        print "(1) Symbol on Tape"
        app.lblScannedSymbol.config(text = "1")
        root.update()
        sleep(0.2)

        print "(R) Direction"
        app.lblDirection.config(text = "Right")
        root.update()
        sleep(0.2)

        self.current_context.tape[self.current_context.tape_position] = "0"
        print "(0) New Symbol on Tape"
        app.lblNewSymbol.config(text = "0")
        root.update()
        sleep(0.2)

        self.current_context.setState("A")
        print "(A) New State"
        app.lblNewState.config(text = "A")
        root.update()
        
        self.current_context.moveRight()
        app.scrollRight(self.current_context.tape)
        root.update()
        print "Tape: ", self.current_context.tape
        print "\n - - - - - - - - - - - - - -  \n"
        sleep(1)
        return True

    def foundEND(self):
        print "End of Machine"
        print "\n - - - - - - - - - - - - - -  \n"
        app.finaliseTape()
        self.current_context.end_of_machine = True
        return True
        # display final tape and end machine


class TuringMachine(StateContext, Transition):
    def __init__(self, starting_state, tape, starting_position):
        self.tape = tape
        self.tape_position = starting_position
        self.starting_state = starting_state
        self.end_of_machine = False

        self.availableStates["A"] = TuringStateA(self)
        self.availableStates["B"] = TuringStateB(self)

        self.setState(self.starting_state)

    def found0(self):
        return self.current_state.found0()

    def found1(self):
        return self.current_state.found1()

    def foundEND(self):
        return self.current_state.foundEND()

    def runMachine(self):
        symbols = {
            "0": self.found0,
            "1": self.found1,
            "END": self.foundEND
        }
        print "\nStarting Tape: ", self.tape
        print "\n - - - - - - - - - - - - - -  \n"

        while self.end_of_machine is False:
            if symbols[self.tape[self.tape_position]]() is False:
                break
            app.lblScannedState.config(text = "N/A")
            app.lblScannedSymbol.config(text = "N/A")    
            app.lblDirection.config(text = "N/A")
            app.lblNewSymbol.config(text = "N/A")
            app.lblNewState.config(text = "N/A")

        app.finalTapePopup() 

    def moveRight(self):    # handles moving right on the tape
        if self.tape_position >= len(self.tape) -2:
            self.tape.append("#")   # a # will be added to the end to stop any out of range errors by the GUI

        self.tape_position += 1 # moves along once to the right of the tape

    def moveLeft(self): # handles moving left on the tape
        self.tape = ["#"] + self.tape   # the machine will add a # to the start of the tape to stop any out of rang errors by the GUI

if __name__ == "__main__":
    root = Tk()
    app = TuringMachineGUI(root)
    root.geometry("1375x500+250+250")
    root.mainloop()