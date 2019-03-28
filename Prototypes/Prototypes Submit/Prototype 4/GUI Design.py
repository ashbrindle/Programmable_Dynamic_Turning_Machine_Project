from Tkinter import *
import tkMessageBox
import sys
from time import sleep

class CustomTapeWindow():
    def __init__(self, window):
        self.tape_font = ("times", 20)
        self.position_font = ("times", 15, "italic")
        self.instruction_font = ("times", 15)
        self.addInstruction_font = ("times", 10)
        self.currentInstruction_font = ("times", 10)
        self.arrow_font = ("calibri", 10, "bold")
        self.run_font = ("bold")
        self.submitTape_font = ("calibri", 10, "bold")
        self.title_font = ("times", 15)
        self.title2_font = ("times", 11)

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

        self.lblInstructionsTitle = Label(
            root,
            text = "Add Instruction:",
            font = self.title_font)
        self.lblInstructionsTitle.pack()
        self.lblInstructionsTitle.place(x = 468, y = 115)

        self.lblAddInstructionsBorder = Label(
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
        self.lblAddInstructionsBorder.pack()
        self.lblAddInstructionsBorder.place(x = 468, y = 140)

        self.txtScannedState = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtScannedState.pack()
        self.txtScannedState.place(x = 675, y = 146)

        self.txtScannedSymbol = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtScannedSymbol.pack()
        self.txtScannedSymbol.place(x = 675, y = 168)

        self.txtDirection = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtDirection.pack()
        self.txtDirection.place(x = 675, y = 188)

        self.txtNewSymbol = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtNewSymbol.pack()
        self.txtNewSymbol.place(x = 675, y = 208)

        self.txtNewState = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.addInstruction_font,
            width = 7,
            borderwidth = 1,
            relief = "solid")
        self.txtNewState.pack()
        self.txtNewState.place(x = 675, y = 230)

        self.btnSaveInstruction = Button(
            root,
            text = "Save Instruction",
            bg = "green4",
            fg = "white",
            font = self.arrow_font,
            height = 1,
            width = 36,
            borderwidth = 1,
            relief = "solid")
        self.btnSaveInstruction.pack()
        self.btnSaveInstruction.place(x = 468, y = 265)

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
        self.lblAllInstructionsTitle.place(x = 262, y = 115)

        self.instructionsFrame = Frame(
            root,
            borderwidth = 2,
            relief = "solid")
        self.instructionsFrame.pack()
        self.instructionsFrame.place(x = 262, y = 140)

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

        self.lblInsertTapeTitle = Label(
            root,
            text = "Insert Tape (CSV):",
            font = self.title_font)
        self.lblInsertTapeTitle.pack()
        self.lblInsertTapeTitle.place(x = 20, y = 115)

        self.txtTape = Text(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.txtTape.pack()
        self.txtTape.place(x = 20, y = 140)

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
        self.btnTape.place(x = 19, y = 165)

        self.lblStartingTitle = Label(
            root,
            text = "Insert Starting State:",
            font = self.title_font)
        self.lblStartingTitle.pack()
        self.lblStartingTitle.place(x = 20, y = 190)

        self.txtStartState = Text(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.txtStartState.pack()
        self.txtStartState.place(x = 20, y = 215)

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
        self.btnStartState.place(x = 19, y = 240)

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
        self.btnRun.place(x = 19, y = 275)

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
        self.btnHelp.place(x = 19, y = 310)

        self.lblDeleteTitle = Label(
            root,
            text = "Delete Instruction",
            font = self.title_font)
        self.lblDeleteTitle.pack()
        self.lblDeleteTitle.place(x = 20, y = 335)

        self.lblDeleteTitle2 = Label(
            root,
            text = "(Instruction Number):",
            font = self.title_font)
        self.lblDeleteTitle2.pack()
        self.lblDeleteTitle2.place(x = 20, y = 360)

        self.txtDeleteInstruction = Entry(
            root,
            bg = "white",
            fg = "black",
            font = self.submitTape_font,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.txtDeleteInstruction.pack()
        self.txtDeleteInstruction.place(x = 20, y = 385)

        self.btnDeleteInstruction = Button(
            root,
            text = "Delete Instruction",
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.btnDeleteInstruction.pack()
        self.btnDeleteInstruction.place(x = 19, y = 411)

        self.btnDeleteAllInstructions = Button(
            root,
            text = "Clear All Instructions",
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            height = 1,
            width = 31,
            borderwidth = 1,
            relief = "solid")
        self.btnDeleteAllInstructions.pack()
        self.btnDeleteAllInstructions.place(x = 19, y = 446)

        self.btnExit = Button(
            root,
            text = "Exit Application",
            bg = "red3",
            fg = "white",
            font = self.submitTape_font,
            command = root.destroy,
            height = 1,
            width = 66,
            borderwidth = 1,
            relief = "solid")
        self.btnExit.pack()
        self.btnExit.place(x = 257, y = 446)

if __name__ == "__main__":
    root = Tk()
    app = CustomTapeWindow(root)
    root.geometry("750x480+250+250")
    root.mainloop()