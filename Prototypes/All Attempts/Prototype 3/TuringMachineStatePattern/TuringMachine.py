from State import State, StateContext
import time

CURRENT_STATE = 0
CURRENT_SYMBOL = 1
DIRECTION = 2
NEW_SYMBOL = 3
NEXT_STATE = 4


class Transition:

    def insertTape(self, new_tape):
        print "Error, Unable Insert Tape"
        return False

    def changeTape(self, new_tape):
        print "Error, Unable to Change Tape"
        return False

    def addInstruction(self, new_instruction):  #list
        print "Error, Unable Add an Instruction"
        return False

    def runMachine(self):
        print "Error, Unable to Run Machine"
        return False

    def deleteInstruction(self, instruction):
        print "Error, Unable to Delete an Instruction"
        return False

    def findInstruction(self):
        print "Error, Unable to Read an Instruction"
        return False

    def executeInstructions(self):
        print "Error, Unable to Execute Instruction"
        return False

    def moveTape(self, direction):
        print "Error, Unable to Move Tape Position"
        return False


class NoTape(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def insertTape(self, new_tape):
        print "Adding Tape: ", new_tape
        print "Current State: [No Tape]"
        self.current_context.tape = new_tape
        self.current_context.setState("NoInstruction")
        print "New State: [No Instruction]"
        return True


class NoInstruction(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def changeTape(self, new_tape):
        print "Changing Tape: ", new_tape
        print "Current State: [No Instruction]"
        self.current_context.tape = new_tape
        self.current_context.setState("NoInstruction")
        print "New State: [No Instruction]"
        return True

    def addInstruction(self, new_instruction):
        print "Adding Instruction: ", new_instruction
        print "Current State: [No Instruction]"
        self.current_context.instructions.append(new_instruction)
        self.current_context.setState("HasInstruction")
        print "Current Instructions: ", self.current_context.instructions
        print "New State: [Has Instruction]"
        return True


class HasInstruction(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def changeTape(self, new_tape):
        print "Changing Tape: ", new_tape
        print "Current State: [Has Instruction]"
        self.current_context.tape = new_tape
        self.current_context.setState("HasInstruction")
        print "New State: [Has Instruction]"
        return True

    def addInstruction(self, new_instruction):
        print "Adding Instruction: ", new_instruction
        print "Current State: [Has Instruction]"
        self.current_context.instructions.append(new_instruction)
        self.current_context.setState("HasInstruction")
        print "Current Instructions: ", self.current_context.instructions
        print "New State: [Has Instruction]"
        return True

    def deleteInstruction(self, instruction_index):
        print "Removing Instruction [" + str(instruction_index) + "]: " + self.current_context.instructions[instruction_index]
        print "Current State: [Has Instruction]"
        self.current_context.instructions.pop[instruction_index]

        if len(self.current_context.instructions) > 0:
            self.current_context.setState("HasInstruction")
            print "Current Instructions: ", self.current_context.instructions
            print "New State: [Has Instruction]"
        elif len(self.current_context.instructions) <= 0:
            self.current_context.setState("NoInstruction")
            print "Current Instructions: ", self.current_context.instructions
            print "New State: [No Instruction]"
        return True

    def runMachine(self):
        print "<--- Running Machine ---> "
        print "Current Tape: ", self.current_context.tape
        print "Current Instructions: ", self.current_context.instructions
        '''puts the instructions into states here? or maybe just reads them from a 2D list?'''
        self.current_context.setState("RunningMachine")
        return True


class RunningMachine(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def executeInstructions(self):
        for index in range(len(self.current_context.instructions)):
            if self.current_context.instructions[index][CURRENT_SYMBOL] == self.current_context.tape[self.current_context.tape_position] and self.current_context.instructions[index][CURRENT_STATE] == self.current_context.machine_state:
                self.current_context.instruction_found = True
                print "Position on Tape: ", self.current_context.tape_position
                self.current_context.tape[self.current_context.tape_position] = self.current_context.instructions[index][NEW_SYMBOL]
                print "Current State:", self.current_context.instructions[index][CURRENT_STATE]
                time.sleep(0.5)
                print "Current Symbol:", self.current_context.instructions[index][CURRENT_SYMBOL]
                time.sleep(0.5)
                print "New Symbol:", self.current_context.instructions[index][NEW_SYMBOL]
                time.sleep(0.5)
                self.current_context.direction = self.current_context.instructions[index][DIRECTION]
                self.current_context.machine_state = self.current_context.instructions[index][NEXT_STATE]
                print "Next State:", self.current_context.instructions[index][NEXT_STATE]
                time.sleep(0.5)

                if self.current_context.instructions[index][DIRECTION] == "R":
                    print "Direction: Right (1 Square)"
                elif self.current_context.instructions[index][DIRECTION] == "L":
                    print "Direction: Left (1 Square)"
                else:
                    print "Invalid Direction, Machine Halting"
                    self.current_context.setState("NoTape")
                    self.current_context.finished = True
                time.sleep(0.5)
                print "Tape: ", self.current_context.tape
                print " "
                time.sleep(1)
                if self.current_context.machine_state == "HALT":
                    self.current_context.setState("NoTape")
                    self.current_context.finished = True
                else:
                    self.current_context.setState("RunningMachine")
                break
        if self.current_context.instruction_found == False:
            print "No Instruction Found, Machine Halting"
            self.current_context.finished = True
            self.current_context.setState("NoTape")

    def moveTape(self, direction):
        if direction == "R" and self.current_context.tape_position < len(self.current_context.tape):
            self.current_context.tape_position += 1
            self.current_context.setState("RunningMachine")
        elif direction == "L" and self.current_context.tape_position > 0:
            self.current_context.tape_position -= 1
            self.current_context.setState("RunningMachine")
        else:
            print "End of Tape, Machine Halting"
            self.current_context.finished = True
            self.current_context.setState("NoTape")


class TuringMachine(StateContext, Transition):
    def __init__(self):
        self.tape = []
        self.instructions = []
        self.machine_state = "A"
        self.tape_position = 1
        self.direction = None
        self.finished = False

        self.available_states["NoTape"] = NoTape(self)
        self.available_states["NoInstruction"] = NoInstruction(self)
        self.available_states["HasInstruction"] = HasInstruction(self)
        self.available_states["RunningMachine"] = RunningMachine(self)
        self.setState("NoTape")

    def insertTape(self, tape):
        return self.current_state.insertTape(tape)

    def changeTape(self, new_tape):
        return self.current_state.changeTape(new_tape)

    def addInstruction(self, new_instruction):
        return self.current_state.addInstruction(new_instruction)

    def deleteInstruction(self, instruction_index):
        return self.current_state.deleteInstruction(instruction_index)

    def runMachine(self):
        return self.current_state.runMachine()

    def executeInstructions(self):
        return self.current_state.executeInstructions()

    def moveTape(self, direction):
        return self.current_state.moveTape(direction)

    def getMachineState(self):
        return self.machine_state

if __name__ == "__main__":
    TM = TuringMachine()
    TM.insertTape(["0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "END"])
    TM.addInstruction(['A', '0', 'L', '1', 'B'])
    TM.addInstruction(['B', '0', 'L', '1', 'A'])
    TM.addInstruction(['A', '1', 'L', '0', 'B'])
    TM.addInstruction(['B', '1', 'L', '0', 'A'])
    TM.addInstruction(['A', 'END', 'R', 'END', 'HALT'])
    TM.addInstruction(['B', 'END', 'R', 'END', 'HALT'])
    TM.runMachine()

    '''PROBLEM, CHANGING SYMBOL, MOVING RIGHT, THEN CHANGING SYMBOL BACK. AND ONLY MOVING THEN, WATCH THE CODE RUN'''

    print "Starting Instructions: ", TM.instructions
    print "Starting Tape: ", TM.tape

    while TM.finished is False:
        TM.executeInstructions()
        TM.moveTape(TM.direction)
    print "Final Tape: ", TM.tape