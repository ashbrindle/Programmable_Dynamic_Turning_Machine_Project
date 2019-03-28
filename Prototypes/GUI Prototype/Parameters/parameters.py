from ttk import *   # for combobox
from Tkinter import *

instructions = []   # 2D list containing the instrctions 0: state, 1: symbol, 2: direction, 3: new symbol,
                    # 4: new state
tape = []   # list contining the turing tape
root = Tk()
root.wm_title("GUI Design")  # title bar on the window
directionchoices = ["R", "L"]   # preset choice of directions

class Machine:

    instructions = []   # 2D list containing the instrctions 0: state, 1: symbol, 2: direction, 3: new symbol,
                        # 4: new state
    tape = []  # list contining the turing tape

    def __init__(self):
        pass

    def saveinstructions(self):
        tmplist = []  # makes a temp list
        tmplist.append(entstate.get())  # fills the temp list
        tmplist.append(entsymbol.get())
        tmplist.append(cmbdirection.get())
        tmplist.append(entNsymbol.get())
        tmplist.append(entNstate.get())

        self.instructions.append(tmplist)  # then moves the list to each element of the instructions list

        entstate.delete(0, END)  # resets the entry/combo boxes
        entsymbol.delete(0, END)
        cmbdirection.delete(0, END)
        entNsymbol.delete(0, END)
        entNstate.delete(0, END)

    def savetape(self):
        input_string = entTape.get()  # saves entry to string
        self.tape = input_string.split(",")  # splits each value by comma, allowing for multiple entries

    def newwindow(self):
        top = Toplevel(master=root)
        length = len(self.tape)
        for x in range(length):
            btn = Button(top, text=self.tape[x], width=5, height=2, state=DISABLED)
            btn.pack(side=LEFT)

if __name__ == '__main__':

    m = Machine()

    # STATE ENTRY
    lblstate = Label(root, text="State: ")
    lblstate.grid(row=0, column=0)
    entstate = Entry(root, bd=5, width=12)
    entstate.grid(row=0, column=1)
    lblstatehelp = Label(root, text="The current state of the machine")
    lblstatehelp.grid(row=0, column=2)

    # SYMBOL ENTRY
    lblsymbol = Label(root, text="Symbol: ")
    lblsymbol.grid(row=1, column=0)
    entsymbol = Entry(root, bd=5, width=12)  # bd is the bored around the indicator (default at 2px, set to 5px)
    entsymbol.grid(row=1, column=1)
    lblsymbolhelp = Label(root, text="The current symbol under the head")
    lblsymbolhelp.grid(row=1, column=2)

    # DIRECTION ENTRY
    lbldirection = Label(root, text="Direction: ")
    lbldirection.grid(row=2, column=0)
    cmbdirection = Combobox(root, state="readonly", values=directionchoices, width=10)
    cmbdirection.grid(row=2, column=1)
    lbldirectionhelp = Label(root, text="The direction the head will travel (Left = L, Right = R")
    lbldirectionhelp.grid(row=2, column=2)

    # NEW SYMBOL ENTRY
    lblNsymbol = Label(root, text="New Symbol: ")
    lblNsymbol.grid(row=3, column=0)
    entNsymbol = Entry(root, bd=5, width=12)  # bd is the bored around the indicator (default at 2px, set to 5px)
    entNsymbol.grid(row=3, column=1)
    lblNsymbolhelp = Label(root, text="The new symbol replacing the previous")
    lblNsymbolhelp.grid(row=3, column=2)

    # NEW STATE ENTRY
    lblNstate = Label(root, text="New State: ")
    lblNstate.grid(row=4, column=0)
    entNstate = Entry(root, bd=5, width=12)  # bd is the bored around the indicator (default at 2px, set to 5px)
    entNstate.grid(row=4, column=1)
    lblNstatehelp = Label(root, text="The new state the machine will enter")
    lblNstatehelp.grid(row=4, column=2)

    # SUBMIT BUTTON (INSTRUCTIONS)
    btnAccept = Button(root, text="Submit Instructions", command=m.saveinstructions, width=30)
    btnAccept.grid(row=5, columnspan=2)

    # TAPE ENTRY
    lblTape = Label(root, text="Turing Tape: ")
    lblTape.grid(row=6, column=0)
    entTape = Entry(root, bd=5, width=12)
    entTape.grid(row=6, column=1)
    lblTapehelp = Label(root, text="The provided Turing Tape (Values seperated with comma (,))")
    lblTapehelp.grid(row=6, column=2)

    # SUBMIT BUTTON (TAPE)
    btnSubmitTape = Button(root, text="Submit Tape", command=m.savetape, width=30)
    btnSubmitTape.grid(row=7, columnspan=2)

    btnSubmitTape = Button(root, text="New Window", command=m.newwindow, width=30)
    btnSubmitTape.grid(row=8, columnspan=2)

    root.mainloop()