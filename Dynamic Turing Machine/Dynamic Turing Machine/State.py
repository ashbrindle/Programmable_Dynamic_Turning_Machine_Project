class State:
    CurrentContext = None

    def __init__(self, context):
        self.CurrentContext = context


class StateContext:
    state_name = None
    CurrentState = None
    avaliable_states = {}

    def setState(self, new_state):
        try:
            self.CurrentState = self.avaliable_states[new_state]
            self.state_name = new_state
            return True
        except KeyError:
            print "no state"
            return False

    def getStateIndex(self):
        return self.state_name
