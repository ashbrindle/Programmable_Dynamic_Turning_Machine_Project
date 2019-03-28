import GUI
class State:
    instructions = []
    current_context = None

    def __init__(self, context):
        self.current_context = context
        self.instructions = []

    def executeInstruction(self):
        for index in range(len(self.instructions)):
            if self.current_context.tape_position == len(self.current_context.tape):
                break
            if self.instructions[index].symbol == self.current_context.tape[self.current_context.tape_position]:
                self.current_context.tape[self.current_context.tape_position] = self.instructions[index].new_symbol
                print "New Symbol:", self.instructions[index].new_symbol

                if self.instructions[index].direction == 'R':
                    print "Right"
                    self.current_context.moveRight()
                    
                elif self.instructions[index].direction == 'L':
                    print "Left"
                    self.current_context.moveLeft()

                self.current_context.setState(self.instructions[index].next_state)
                self.current_context.state_name = self.instructions[index].next_state
                print "Current State: ", self.current_context.state_name
                break


    def setInstruction(self, symbol, direction, new_symbol, next_state):
        new_instruction = Instruction()
        new_instruction.symbol = symbol
        new_instruction.direction = direction
        new_instruction.new_symbol = new_symbol
        new_instruction.next_state = next_state
        self.instructions.append(new_instruction)

class Instruction:
    symbol = ''
    direction = 'None'
    new_symbol = ''
    next_state = ''

class TuringMachine:
    current_state = None
    state_name = ""
    available_states = {"HALT": None}
    tape = []
    tape_position = 0
    temp_instructions = []
    starting_state = None

    def runMachine(self):
        for instruction in self.temp_instructions:
            if instruction[0] not in self.available_states:
                self.available_states[instruction[0]] = State(self)
            self.available_states[instruction[0]].setInstruction(instruction[1], instruction[2], instruction[3], instruction[4])

        self.current_state = self.available_states[self.starting_state]
        self.state_name = self.starting_state
        print "Starting State: ", self.state_name

        while self.state_name is not "HALT":
            self.executeInstruction()

    def moveRight(self):    # handles moving right on the tape
        self.tape_position += 1
        #if self.tape_position == len(self.tape):
        self.tape.append("#")   # if the position is at the end, add a blank symbol

    def moveLeft(self): # handles moving left on the tape
        self.tape_position -= 1
        #if self.tape_position < 0:
        self.tape = ["#"] + self.tape   # if the position is at the start, add a blank symbol

    def changeSymbol(self, symbol):
        self.tape[self.tape_position] == str(symbol)    # changes the current squares symbol on the tape

    def saveInstruction(self, state, symbol, direction, new_symbol, next_state):
        current_instruction = [state, symbol, direction, new_symbol, next_state]
        self.temp_instructions.append(current_instruction)

    def setTape(self, tape):
        self.tape = (tape.split(","))
        while len(self.tape) < 8:
            self.tape.append("#")

    def setState(self, state):
        self.current_state = self.available_states[state]

    def executeInstruction(self):
        self.current_state.executeInstruction()
