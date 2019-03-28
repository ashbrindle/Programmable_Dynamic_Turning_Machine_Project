

class State:
    current_context = None

    def __init__(self, Context):
        self.current_context = Context

    def trigger(self):
        True


class StateContext:
    state = None
    current_state = None
    available_states = {}

    def setState(self, new_state):
        try:
            self.current_state = self.available_states[new_state]
            self.state = new_state
            self.current_state.trigger()
            return True
        except KeyError:
            return False

    def getStateIndex(self):
        return self.state