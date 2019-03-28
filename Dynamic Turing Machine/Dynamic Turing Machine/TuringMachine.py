from State import State, StateContext
from time import sleep
from collections import defaultdict

DIRECTION = 0
NEW_SYMBOL = 1
NEXT_STATE = 2


class Transition:

    # if the state machine cannot run the transition between each state this will serve as a default message
    def executeInstruction(self):
        print "Cannot Execute Instruction"
        return False


class TuringState(State, Transition):
    ''' this will serve as the main state in the state machine and will be used to
    dynamically create the states needed in the machine this is done through looking
    through the instructions provided and adding the states which have been speicifed
    as a TuringState() object. This means that there will be multiple of this state in
    the state machine, each representing the different states in the State and Turing Machine'''

    # depending on the state the machine is in, a dictionary will be used to contain all
    # instructions which can be executed in the current state. This will be different with each state in the machine
    instructions = {}

    # when the state is created the instructions which are relevent to the state will be passed in through a
    # parameter and then saved in the current states instructions dictionary
    def __init__(self, context, new_instructions):
        State.__init__(self, context)
        self.instructions = new_instructions

    def executeInstruction(self):
        print self.instructions
        print "symbol read: ", self.CurrentContext.tape[self.CurrentContext.tape_position]
        # the machine gets the current symbol on the tape and saves it to a variable to be used
        current_symbol = self.CurrentContext.tape[self.CurrentContext.tape_position]

        # if the symbol on the tape exists in the instructions, the instructions relevent to
        # the symbol will be carried out
        if current_symbol in self.instructions:

            # prints out the relevent information to help follow the progress of the Turing Machine
            print "Current Tape: ", self.CurrentContext.tape
            print "Current State: ", self.CurrentContext.state_name
            # sleep(0.3)

            # the machine will then change the current symbol on the tape to the new symbol provided in the instructions
            self.CurrentContext.tape[self.CurrentContext.tape_position] = self.instructions[current_symbol][NEW_SYMBOL]
            print "New Symbol: ", self.instructions[current_symbol][NEW_SYMBOL]
            #sleep(0.3)

            # then the machine will transition to the new state in the machine
            self.CurrentContext.setState(self.instructions[current_symbol][NEXT_STATE])
            print "New State: ", self.instructions[current_symbol][NEXT_STATE]
            #sleep(0.3)

            # the machine will move either left or right depending on the instructions,
            # if an invalid direction is provided, the heads position on the tape will not move
            if self.instructions[current_symbol][0] == "R":
                if self.CurrentContext.tape_position >= (len(self.CurrentContext.tape) - 2):
                    self.CurrentContext.tape += ["#"]
                self.CurrentContext.tape_position += 1
                print "Moving Right"
            elif self.instructions[current_symbol][0] == "L":
                if self.CurrentContext.tape_position <= 1:
				    self.CurrentContext.tape = ["#"] + self.CurrentContext.tape
                else:
                    self.CurrentContext.tape_position -= 1
            else:
                print "Not a Valid Direction"
        else:
            return False

            #sleep(0.3)
            return True


class TuringMachine(StateContext, Transition):
    ''' the main TuringMachine class will be the main way to access the state machine
    and set all of the correct attributes for defining the condition of the Turing Machine.
    This class will also include methods for adding an instruction to the temp_instructions
    dictionary which will handle all of the states in the machine and their associated instructions,
    as well as handle adding all of the states to the machine'''

    # when the machine is initalised, the tape, starting position and the starting state will be
    # defined to give a basis on the condition of the machine
    def __init__(self, new_tape, start_pos, start_state):

        # defining the attributes to the machine
        self.tape = new_tape
        self.tape_position = start_pos
        self.starting_state = start_state

        # this will hold all of the instructions before they are initalised in the machine,
        # this is a nested dictionary containing 2 sets of keys,
        # the state keys and the symbol keys
        self.temp_instructions = {}

        # this is used through the collections library, giving the ability to create a key
        # in the nested dictionary if none is present
        self.temp_instructions = defaultdict(dict)

    # calls the correct method with the current state of the machine
    def executeInstruction(self):
        return self.CurrentState.executeInstruction()

    # this method is used to save an instruction to the machines temporary dictionary.
    # This will be called whenever a single instruction is submitted and creates adds the
    # instruction or creates a new key if needed in the nested dictionary
    def setInstruction(self, state, symbol, direction, new_symbol, new_state):

        # saves the instruction to the nested dictionary using the state and the symbol provided,
        # while saving a list of the actions the machine will take
        self.temp_instructions[state][symbol] = [direction, new_symbol, new_state]

    # this method will initalise the machine when all of the instructions are present.
    # The machine will create the states dynamically depending on what instructions are saved
    def startMachine(self):

        # firstly the machine will get all of the keys (states) that are used in the instructions
        states = self.temp_instructions.keys()

        # and will then cycle through the states and add them to the machine with the instructions
        # associated with each state, passed in via a method parameter
        for state in states:
            self.avaliable_states[state] = TuringState(self, self.temp_instructions[state])

        # the machine will then go through all of the states that the machine should be able to transition
        # to and if it does not exist it will create it by looking into the nested dictionaries contents.
        # If the state does not exist it will be create with an empty set of instructions, these instructions
        # are set to be empty as the state will not transition anywhere
        for state in self.temp_instructions:
            for symbol in self.temp_instructions[state]:
                if self.temp_instructions[state][symbol][NEXT_STATE] not in self.avaliable_states.keys():
                    self.avaliable_states[self.temp_instructions[state][symbol][NEXT_STATE]] = TuringState(self, {})

        # the startign state will then be set
        self.setState(self.starting_state)

        # runs the machine while the machine does not reach a HALT state
        while (True):
            if self.state_name == "HALT":
                print "Final Tape: ", self.finaliseTape()
                break
            if (self.executeInstruction() == False):
                break

    def finaliseTape(self):
        finaltapestr = ""

        while self.tape[0] == "#":
            self.tape.pop(0)
            if self.tape[0] != "#":
                break
        if len(self.tape) > 1:
            while self.tape[-1] == "#":
                self.tape.pop(-1)
                if self.tape[-1] != "#":
                    break

        for index in range (len(self.tape)):
            finaltapestr += "[" + str(self.tape[index]) + "] "
        return finaltapestr



if __name__ == '__main__':
    # tape provided using CMV
    tape = ["1", "1", "1", "+", "1", "1", "1", "1", "="]

    # create the machine using a tape, starting position and a starting state
    TM = TuringMachine(tape, 0, "A")

    # each of the instructions are set in the machine,
    # [current state], [current symbol], [direction], [new symbol] and the [new state]
    TM.setInstruction("A", "0", "R", "0", "A")
    TM.setInstruction("A", "1", "R", "0", "B")
    TM.setInstruction("A", "+", "R", "+", "A")
    TM.setInstruction("A", "=", "L", "=", "E")
	
    TM.setInstruction("B", "0", "R", "0", "B")
    TM.setInstruction("B", "1", "R", "1", "B")
    TM.setInstruction("B", "+", "R", "+", "B")
    TM.setInstruction("B", "=", "R", "=", "C")
	
    TM.setInstruction("C", "1", "R", "1", "C")
    TM.setInstruction("C", "#", "L", "1", "D")
	
    TM.setInstruction("D", "0", "L", "0", "D")
    TM.setInstruction("D", "1", "L", "1", "D")
    TM.setInstruction("D", "+", "L", "+", "D")
    TM.setInstruction("D", "=", "L", "=", "D")
    TM.setInstruction("D", "#", "R", "#", "A")

    TM.setInstruction("E", "0", "L", "1", "E")
    TM.setInstruction("E", "1", "L", "1", "E")
    TM.setInstruction("E", "+", "L", "+", "E")
    TM.setInstruction("E", "#", "R", "#", "HALT")
    # saves all of the states in the machine and runs the machine
    TM.startMachine()

