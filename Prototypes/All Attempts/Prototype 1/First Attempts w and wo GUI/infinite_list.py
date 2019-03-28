import os


class Machine:

    def __init__(self):
        self.tape = ["1", "1", "1", "1"]
        self.instructions = []
        self.instructions_populated = False

    def menu(self):
        option = raw_input("""
        1: Add an Instruction
        2: View Instructions
        3: Input Tape
        4: Run
        Please Select an Option: """)

        if option == "1":
            self.fillInstructions()
        elif option == "2":
            self.viewInstructions()
        elif option == "3":
            self.fillTape()
        elif option == "4":
            self.run()

    def populateInstructions(self, filename):

        print (os.getcwd())

        try:
            file = open(filename, "r")      # opens the file specified in the method parameters
        except IOError:     # catches an error is the file does not exist
            print "Instructions file does not exist"
            return      # early return if network population fails
        for line in file:
            self.instructions.append(map(str, line.strip().split(',')))       # fills the network 2d list with comma seperated values using the split method

        self.network_populated = True       # the network will then get set to populated
        file.close


    def fillTape(self):
        input = raw_input("Tape? ")

        self.tape = (input.split(","))

        print "Current Tape: " + str(self.tape)

        self.menu()

    def viewInstructions(self):
        for instruction in range(len(self.instructions)):
            print self.instructions[instruction]

        self.menu()

    def run(self):
        tape_position = 0
        current_instruction_set = []
        instructionfound = False
        current_state = raw_input("What is the Starting State: ")
        print ""

        if current_state.islower():
            print "Starting State Must be Capitalised"
            self.run()

        print "Machine will begin at the start of the list"
        current_symbol = self.tape[tape_position]

        print "Starting Tape: " + str(self.tape)
        print ""


        while current_state != "H":
            current_symbol = self.tape[tape_position]
            for index in range(len(self.instructions)): # goes through the instructions
                if self.instructions[index][0] == current_state and self.instructions[index][1] == current_symbol:  # if both the symbol and state match the instruction
                    current_instruction_set = self.instructions[index]  # make a copy of that instruction to be executed
                    instructionfound = True

            if instructionfound == True:
                print "Current Tape: " + str(self.tape)

                print "Scanned Symbol: " + str(current_symbol)
                print "Scanned State: " + str(current_state)

                self.tape[tape_position] = current_instruction_set[3]   # assigns new value to the tape
                print "New Value on Square: " + str(self.tape[tape_position])

                current_state = current_instruction_set[4]  # assigns new state to machine
                print "New State of Machine: " + str(current_state)

                if current_instruction_set[2] == "R" and current_instruction_set[4] != "H":
                    tape_position += 1

                    if tape_position == len(self.tape):

                        self.tape.append(' ')
                    print "Moving Right"
                    print "--------------------------------------"
                    print ""

                elif current_instruction_set[2] == "L" and current_instruction_set[4] != "H":
                    tape_position -= 1

                    if tape_position == -1:
                        self.tape = [' '] + self.tape
                        tape_position = 0

                    print "Moving Left"
                    print "--------------------------------------"
                    print ""

                    if tape_position < 0 or tape_position > len(self.tape):
                        print "<--- End of Tape --->"
                        print "Final Tape: " + str(self.tape)
                        self.menu()

        else:
            print "<--- End of Tape --->"
            print "Final Tape: " + str(self.tape)


        self.menu()

if __name__ == "__main__":
    m = Machine()
    m.populateInstructions("instructions.txt")
    m.menu()