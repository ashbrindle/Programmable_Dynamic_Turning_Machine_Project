from Tkinter import *

instructions = [[]]     # 0: state, 1: symbol, 2: direction, 3: new symbol, 4: new state

def save():
    instructions[0].append(entstate.get())
    instructions[0].append(entsymbol.get())
    instructions[0].append(entdirection.get())
    instructions[0].append(entNsymbol.get())
    instructions[0].append(entNstate.get())

    print instructions

top = Tk()

lblstate = Label(top, text = "State")
lblstate.pack()
entstate = Entry(top, bd = 5) # bd is the bored around the indicator (default at 2px, set to 5px)
entstate.pack()

lblsymbol = Label(top, text = "Symbol")
lblsymbol.pack()
entsymbol = Entry(top, bd = 5) # bd is the bored around the indicator (default at 2px, set to 5px)
entsymbol.pack()

lbldirection = Label(top, text = "Direction")
lbldirection.pack()
entdirection = Entry(top, bd = 5) # bd is the bored around the indicator (default at 2px, set to 5px)
entdirection.pack()

lblNsymbol = Label(top, text = "New Symbol")
lblNsymbol.pack()
entNsymbol = Entry(top, bd = 5) # bd is the bored around the indicator (default at 2px, set to 5px)
entNsymbol.pack()

lblNstate = Label(top, text = "New State")
lblNstate.pack()
entNstate = Entry(top, bd = 5) # bd is the bored around the indicator (default at 2px, set to 5px)
entNstate.pack()

lblTape = Label(top, text = "Tape")
lblTape.pack()

entTape1 = Entry(top, width = 5) # bd is the bored around the indicator (default at 2px, set to 5px)
entTape1.pack(side = RIGHT)

entTape2 = Entry(top, width = 5)
entTape2.pack(side = RIGHT)

entTape3 = Entry(top, width = 5)
entTape3.pack(side = RIGHT)

entTape4 = Entry(top, width = 5)
entTape4.pack(side = RIGHT)

entTape5 = Entry(top, width = 5)
entTape5.pack(side = RIGHT)

entTape6 = Entry(top, width = 5)
entTape6.pack(side = RIGHT)

entTape7 = Entry(top, width = 5)
entTape7.pack(side = RIGHT)

AcceptButton = Button(top, text = "Submit", command = save)
AcceptButton.pack(side = BOTTOM)

top.mainloop()