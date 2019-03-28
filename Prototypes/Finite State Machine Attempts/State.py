
class State:
    CurrentContext = None
    def __init__ (self, context):
        self.CurrentContext = context

    def trigger(self):
        return True

class StateContext:
    state_name = None
    CurrentState = None
    availableStates = {}

    def setState(self, new_state):
        try:
            self.CurrentState = self.availableStates[new_state]
            self.state_name = new_state
            self.CurrentState.trigger()
            return True
        except KeyError:
            return False

    def getStateIndex(self):
        return self.state