from State import State, StateContext
from time import sleep


class Transition:
    def foundA(self):
        print "Error, No instruction for A on current machine state"
        return False
    
    def foundB(self):
        print "Error, No instruction for B on current machine state"
        return False
        
    def foundC(self):
        print "Error, No instruction for C on current machine state"
        return False

    def foundBlank(self):
        print "Error, No instruction for a Blank symbol in this state"
        return False

    def finaliseTape(self):
        print "Error, Cannot currently finalise tape"
        return False


class State1(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def foundA(self):
        print " "
        print "Current Tape: ", self.CurrentContext.tape
        print "State: 1"
        sleep(0.5)
        print "Read: A"
        sleep(0.5)
        print "Move: Right"
        sleep(0.5)
        print "Load: B"
        sleep(0.5)
        print "New State: 2"
        sleep(0.5)
        self.CurrentContext.tape[self.CurrentContext.tape_pos] = "B"
        self.CurrentContext.setState("2")
        self.CurrentContext.tape_pos += 1
        return True

    def foundBlank(self):
        print " "
        print "Current Tape: ", self.CurrentContext.tape
        print "State: 1"
        sleep(0.5)
        print "Read: #"
        sleep(0.5)
        print "New State: HALT"
        sleep(0.5)
        self.CurrentContext.setState("HALT")
        return True


class State2(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def foundB(self):
        print " "
        print "Current Tape: ", self.CurrentContext.tape
        print "State: 2"
        sleep(0.5)
        print "Read: B"
        sleep(0.5)
        print "Move: Right"
        sleep(0.5)
        print "Load: C"
        sleep(0.5)
        print "New State: 3"
        sleep(0.5)
        self.CurrentContext.tape[self.CurrentContext.tape_pos] = "C"
        self.CurrentContext.setState("3")
        self.CurrentContext.tape_pos += 1
        return True

    def foundBlank(self):
        print " "
        print "Current Tape: ", self.CurrentContext.tape
        print "State: 2"
        sleep(0.5)
        print "Read: #"
        sleep(0.5)
        print "New State: HALT"
        sleep(0.5)
        self.CurrentContext.setState("HALT")
        return True


class State3(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def foundC(self):
        print " "
        print "Current Tape: ", self.CurrentContext.tape
        print "State: 3"
        sleep(0.5)
        print "Read: C"
        sleep(0.5)
        print "Move: Right"
        sleep(0.5)
        print "Load: D"
        sleep(0.5)
        print "New State: HALT"
        sleep(0.5)
        self.CurrentContext.tape[self.CurrentContext.tape_pos] = "D"
        self.CurrentContext.setState("HALT")
        self.CurrentContext.tape_pos += 1
        return True

    def foundBlank(self):
        print " "
        print "Current Tape: ", self.CurrentContext.tape
        print "State: 3"
        sleep(0.5)
        print "Read: #"
        sleep(0.5)
        print "New State: HALT"
        sleep(0.5)
        self.CurrentContext.setState("HALT")
        return True


class StateHALT(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def finaliseTape(self):
        print "Final Tape:", self.CurrentContext.tape
        return True

    
class TuringMachine(StateContext, Transition):
    def __init__(self):
        self.tape = ["A", "B", "C", "#"]
        self.tape_pos = 0

        self.availableStates["1"] = State1(self)
        self.availableStates["2"] = State2(self)
        self.availableStates["3"] = State3(self)
        self.availableStates["HALT"] = StateHALT(self)
        self.setState("1")

    def foundA(self):
       self.CurrentState.foundA()
    
    def foundB(self):
        self.CurrentState.foundB()
        
    def foundC(self):
        self.CurrentState.foundC()

    def finaliseTape(self):
        self.CurrentState.finaliseTape()
        

if "__main__" == __name__:
    TM = TuringMachine()
    while (True):
        symbol = TM.tape[TM.tape_pos]
        if symbol == "A": TM.foundA()
        elif symbol == "B": TM.foundB()
        elif symbol == "C": TM.foundC()
        elif TM.state_name == "HALT": 
            TM.finaliseTape()
            break