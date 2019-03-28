class State:
    current_context = None

    def __init__(self, context):
        self.current_context = context

    def trigger(self):
        return True

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

class Transition:   # execute instruction, change state
    def pressButton(self):
        print "Error: No Button Exists"

class LightSwitchOn(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def pressButton(self):
        print "Lights Off"
        self.current_context.setState("OFF")


class LightSwitchOff(State, Transition):
    def __init__(self, context):
        State.__init__(self, context)

    def pressButton(self):
        print "Lights On"
        self.current_context.setState("ON")

class LightSwitch(StateContext, Transition):
    def __init__(self):
        self.available_states["OFF"] = LightSwitchOff(self)
        self.available_states["ON"] = LightSwitchOn(self)
        self.setState("OFF")

    def pressButton(self):
        self.current_state.pressButton()

if __name__ == "__main__":
    MySwitch = LightSwitch()
    print "Current State: ", MySwitch.state
    MySwitch.pressButton()
    print "Current State: ", MySwitch.state
    MySwitch.pressButton()
    print "Current State: ", MySwitch.state
