from State import State, StateContext
from time import sleep

DIRECTION = 0
NEWSYMBOL = 1
NEXTSTATE = 2


class Transition:

    def is0(self):
        print "Error"
        return False

    def is1(self):
        print "Error"
        return False

    def isHALT(self):
        print "Error"
        return False


class TuringStateA(State, Transition):
    instructions = {
        "0": ["R", "1", "B"],
        "HALT": ["R", "HALT", "HALT"]
    }

    def __init__(self, context):
        State.__init__(self, context)

    def is0(self):
        print "Current State: A"
        sleep(0.5)
        print "Current Symbol: 0"
        sleep(0.5)
        self.current_context.tape[self.current_context.tape_position] = self.instructions["0"][NEWSYMBOL]
        self.current_context.setState(self.instructions["0"][NEXTSTATE])     # changing to next machine state
        print "Moving Direction: ", self.instructions["0"][DIRECTION]
        sleep(0.5)
        if self.instructions["0"][DIRECTION] == "R":
            self.current_context.tape_position += 1         # moving right
        elif self.instructions["0"][DIRECTION] == "L":
            self.current_context.tape_position -= 1         # moving left
        print "New Symbol: ", self.instructions["0"][NEWSYMBOL]
        sleep(0.5)
        print "Next State: ", self.instructions["0"][NEXTSTATE]
        sleep(0.5)
        print "Tape: ", self.current_context.tape
        sleep(0.5)
        return True

    def isHALT(self):
        print "Current State: ", self.current_context.state
        sleep(0.5)
        print "Current Symbol: HALT"
        sleep(0.5)
        self.current_context.tape[self.current_context.tape_position] = self.instructions["HALT"][NEWSYMBOL]
        self.current_context.setState(self.instructions["HALT"][NEXTSTATE])     # changing to next machine state
        print "Moving Direction: ", self.instructions["HALT"][DIRECTION]
        sleep(0.5)
        if self.instructions["HALT"][DIRECTION] == "R":
            self.current_context.tape_position += 1         # moving right
        elif self.instructions["HALT"][DIRECTION] == "L":
            self.current_context.tape_position -= 1         # moving left
        print "New Symbol: ", self.instructions["HALT"][NEWSYMBOL]
        sleep(0.5)
        print "Next State: ", self.instructions["HALT"][NEXTSTATE]
        sleep(0.5)
        print "Tape: ", self.current_context.tape
        sleep(0.5)
        return True


class TuringStateB(State, Transition):
    instructions = {
        "1": ["R", "0", "A"],
        "HALT": ["R", "HALT", "HALT"]
    }

    def __init__(self, context):
        State.__init__(self, context)

    def is1(self):
        print "Current State: ", self.current_context.state
        sleep(0.5)
        print "Current Symbol: 1"
        sleep(0.5)
        self.current_context.tape[self.current_context.tape_position] = self.instructions["1"][NEWSYMBOL]
        self.current_context.setState(self.instructions["1"][NEXTSTATE])     # changing to next machine state
        print "Moving Direction: ", self.instructions["1"][DIRECTION]
        sleep(0.5)
        if self.instructions["1"][DIRECTION] == "R":
            self.current_context.tape_position += 1         # moving right
        elif self.instructions["1"][DIRECTION] == "L":
            self.current_context.tape_position -= 1         # moving left
        print "New Symbol: ", self.instructions["1"][NEWSYMBOL]
        sleep(0.5)
        print "Next State: ", self.current_context.state
        sleep(0.5)
        print "Tape: ", self.current_context.tape
        sleep(0.5)

    def isHALT(self):
        print "Current State: ", self.current_context.state
        sleep(0.5)
        print "Current Symbol: HALT"
        sleep(0.5)
        self.current_context.tape[self.current_context.tape_position] = self.instructions["HALT"][NEWSYMBOL]
        self.current_context.setState(self.instructions["HALT"][NEXTSTATE])     # changing to next machine state
        print "Moving Direction: ", self.instructions["HALT"][DIRECTION]
        sleep(0.5)
        if self.instructions["HALT"][DIRECTION] == "R":
            self.current_context.tape_position += 1         # moving right
        elif self.instructions["HALT"][DIRECTION] == "L":
            self.current_context.tape_position -= 1         # moving left
        print "New Symbol: ", self.instructions["HALT"][NEWSYMBOL]
        sleep(0.5)
        print "Next State: ", self.instructions["HALT"][NEXTSTATE]
        sleep(0.5)
        print "Tape: ", self.current_context.tape
        sleep(0.5)
        return True


class TuringStateHALT(State, Transition):

    def __init__(self, context):
        State.__init__(self, context)


class TuringMachine(StateContext, Transition):
    def __init__(self, tape):
        self.tape = tape
        self.tape_position = 0
        self.starting_state = "A"

        self.availableStates["A"] = TuringStateA(self)
        self.availableStates["B"] = TuringStateB(self)
        self.availableStates["HALT"] = TuringStateHALT(self)

        self.setState(self.starting_state)

    def is0(self):
        return self.current_state.is0()

    def is1(self):
        return self.current_state.is1()

    def isHALT(self):
        return self.current_state.isHALT()

if __name__ == "__main__":
    TM = TuringMachine(["0", "1", "0", "1", "0", "1", "0", "1", "HALT"])

    while TM.state != "HALT":
        if TM.tape[TM.tape_position] == "0":
            TM.is0()
        elif TM.tape[TM.tape_position] == "1":
            TM.is1()
        elif TM.tape[TM.tape_position] == "HALT":
            TM.isHALT()
    print TM.tape
