from State import State, StateContext
from time import sleep

CURRENTSTATE = 0
CURRENTSYBMOL = 1
DIRECTION = 2
NEWSYMBOL = 3
NEXTSTATE = 4


class Transition:
    def performAction(self, direction):
        print "Cannot Move"
        return False


class MachineState(State, Transition):

    def __init__(self, context):
        State.__init__(self, context)

    def performAction(self):

        for index in range(len(self.current_context.instructions)):
            if (self.current_context.instructions[index][CURRENTSTATE] == self.current_context.state and self.current_context.instructions[index][CURRENTSYBMOL] == self.current_context.tape[self.current_context.tape_position]):
                print "Current State: ", self.current_context.state
                sleep(0.5)
                print "Current Symbol: ", self.current_context.instructions[index][CURRENTSYBMOL]
                sleep(0.5)
                self.current_context.tape[self.current_context.tape_position] = self.current_context.instructions[index][NEWSYMBOL]
                self.current_context.setState(self.current_context.instructions[index][NEXTSTATE])     # changing to next machine state
                print "Moving Direction: ", self.current_context.instructions[index][DIRECTION]
                sleep(0.5)
                if self.current_context.instructions[index][DIRECTION] == "R":
                    self.current_context.tape_position += 1         # moving right
                elif self.current_context.instructions[index][DIRECTION] == "L":
                    self.current_context.tape_position -= 1         # moving left
                print "New Symbol: ", self.current_context.instructions[index][NEWSYMBOL]
                sleep(0.5)
                print "Next State: ", self.current_context.instructions[index][NEXTSTATE]
                sleep(0.5)
                print "Tape: ", self.current_context.tape
                sleep(0.5)
                return True


class TuringMachine(StateContext, Transition):
    def __init__(self):
        self.tape_position = 0
        self.starting_state = "A"
        self.instructions = []
        self.tape = ["0", "0", "0", "0", "0", "0", "END"]

    def initialiseMachine(self):
        for index in range(len(self.instructions)):
            if self.instructions[index][CURRENTSTATE] not in self.availableStates:
                self.availableStates[self.instructions[index][CURRENTSTATE]] = MachineState(self)
            if self.instructions[index][NEXTSTATE] not in self.availableStates:
                self.availableStates[self.instructions[index][NEXTSTATE]] = MachineState(self)
        self.setState(self.starting_state)

    def addInstruction(self, new_instruction):
        self.instructions.append(new_instruction)

    def performAction(self):
        return self.current_state.performAction()

if __name__ == "__main__":
    TM = TuringMachine()
    TM.addInstruction(["A", "0", "R", "1", "B"])
    TM.addInstruction(["B", "0", "R", "1", "A"])
    TM.addInstruction(["B", "END", "R", "1", "HALT"])
    TM.addInstruction(["A", "END", "R", "1", "HALT"])
    TM.initialiseMachine()
    while TM.state != "HALT":
        TM.performAction()
    print "Done"