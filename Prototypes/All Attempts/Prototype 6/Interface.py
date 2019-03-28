from Tkinter import *
import tkMessageBox
import sys
from time import sleep
from State import State, StateContext
from collections import defaultdict


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

        self.turing_machine_options = [
            "Hello World Turing Machine",
            "Flip 1 | 0 Turing Machine",
            "Option 3",
            "Option 4"]
        self.tape_options = [
            "0, 1, 0, 2, 3, A, B, 1, 0, J",
            "0, 1, 0, A, 3, 6, F, Q, 9, 9"]

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

        self.btnRight = Button(
            root,
            text = ">",
            bg = "DarkGoldenrod3",
            fg = "black",
            font = self.arrow_font,
            height = 4,
            width = 2,
            borderwidth = 1,
            relief = "solid")
        self.btnRight.pack()
        self.btnRight.place(x = 700, y = 30)

        self.btnLeft = Button(
            root,
            text = "<",
            bg = "DarkGoldenrod3",
            fg = "black",
            font = self.arrow_font,
            height = 4,
            width = 2,
            borderwidth = 1,
            relief = "solid")
        self.btnLeft.pack()
        self.btnLeft.place(x = 30, y = 30)

        self.lblSelectTapeTitle = Label(
            root,
            text = "Select Machine Tape:",
            font = self.title_font)
        self.lblSelectTapeTitle.pack()
        self.lblSelectTapeTitle.place(x = 468, y = 200)

        self.selected_tape = StringVar()
        self.selected_tape.set(self.tape_options[0])
        self.optTape = OptionMenu(
            root,
            self.selected_tape,
            *self.tape_options)
        self.optTape.pack()
        self.optTape.config(
            bg = "white",
            fg = "black",
            font = self.dropdown_font,
            width = 37,
            borderwidth = 1,
            relief = "solid",
            justify = LEFT)
        self.optTape["menu"].config(
            bg = "white",
            fg = "black",
            font = self.dropdown_font,
            borderwidth = 1,
            relief = "solid")
        self.optTape.place(x = 468, y = 230)

        self.btnSelectTape = Button(
            root,
            text = "Submit Machine Tape",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 37,
            borderwidth = 1,
            relief = "solid")
        self.btnSelectTape.pack()
        self.btnSelectTape.place(x = 468, y = 265)

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
        self.lblInstructionsBorder.place(x = 468, y = 318)

        self.lblScannedState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblScannedState.pack()
        self.lblScannedState.place(x = 665, y = 324)

        self.lblScannedSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblScannedSymbol.pack()
        self.lblScannedSymbol.place(x = 665, y = 346)

        self.lblDirection = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblDirection.pack()
        self.lblDirection.place(x = 665, y = 366)

        self.lblNewSymbol = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblNewSymbol.pack()
        self.lblNewSymbol.place(x = 665, y = 386)

        self.lblNewState = Label(
            root,
            text = "N/A",
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7)
        self.lblNewState.pack()
        self.lblNewState.place(x = 665, y = 408)

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
            height = 18,
            width = 27)
        self.lstShowInstructions.pack(side = "left", fill = "y")
        self.scrlInstructions.config(command = self.lstShowInstructions.yview)
        self.lstShowInstructions.insert(0, "No Instructions Loaded,")
        self.lstShowInstructions.insert(1, "Add Instructions on the Right")
        self.lstShowInstructions.insert(2, "Side of the Window")

        self.lblCustomTapeTitle = Label(
            root,
            text = "Custom Tape (CSV):",
            font = self.title_font)
        self.lblCustomTapeTitle.pack()
        self.lblCustomTapeTitle.place(x = 230, y = 115)

        self.txtTape = Text(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 32,
            borderwidth = 1,
            relief = "solid")
        self.txtTape.pack()
        self.txtTape.place(x = 230, y = 143)

        self.btnTape = Button(
            root,
            text = "Submit Tape",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.btnTape.pack()
        self.btnTape.place(x = 229, y = 175)

        self.lblStartingTitle = Label(
            root,
            text = "Change Starting State:",
            font = self.title_font)
        self.lblStartingTitle.pack()
        self.lblStartingTitle.place(x = 230, y = 200)

        self.txtStartState = Text(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 32,
            borderwidth = 1,
            relief = "solid")
        self.txtStartState.pack()
        self.txtStartState.place(x = 230, y = 233)

        self.btnStartState = Button(
            root,
            text = "Submit State",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.btnStartState.pack()
        self.btnStartState.place(x = 230, y = 265)

        self.btnHelp = Button(
            root,
            text = "Help",
            bg = "DarkGoldenRod3",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.btnHelp.pack()
        self.btnHelp.place(x = 230, y = 300)

        self.btnRun = Button(
            root,
            text = "Run Machine",
            bg = "green4",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.btnRun.pack()
        self.btnRun.place(x = 230, y = 335)

        self.btnExit = Button(
            root,
            text = "Exit Application",
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            command = root.destroy,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.btnExit.pack()
        self.btnExit.place(x = 230, y = 370)

    def selections(self, item):
        #self.tape = self.tapes[item]
        #self.starting_state = self.starting_states[item]
        #self.tape_position = self.tape_positions[item]
        self.fillTape()
        if self.tape_position >= 0:
            for pos in range(self.tape_position):
                self.scrollRight(self.tape)
        root.update()

    def left(self):
        self.scrollLeft(self.tape)

    def right(self):
        self.scrollRight(self.tape)

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
    
    def submitTape(self):
        if self.txtTape.get("1.0", END) == "\n":
            self.txtTape.insert(END, "#")

        while len(str(self.txtTape.get("1.0", END))) < 16:
            self.txtTape.insert(END, ",#")

        input_tape = str(self.txtTape.get("1.0", END))
        input_tape = input_tape[:-1]
        self.tape = input_tape.split(",")

        self.fillTape()

        self.txtTape.delete('1.0', END)
        print "Current Tape: ", self.tape   

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

    def setStartingState(self):
        # if str(self.txtStartingState.get("1.0", END)) != "":
        #     self.starting_state = str(self.txtStartingState.get("1.0", END))
        #     self.starting_state = self.starting_state[:-1]
        #     print "starting State set to: ", self.starting_state
        pass

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



if __name__ == "__main__":
    root = Tk()
    app = TuringMachineGUI(root)
    root.geometry("750x450+250+250")
    root.mainloop()