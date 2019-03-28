class A():

    def __init__(self):
        pass

    def printB(self):
        self.bye()

class B(A):

    def __init__(self):
        A.__init__(self)

    def bye(self):
        print "bye"

    def printhi(self):
        print "im B"

if __name__ == "__main__":

    b = B()
    a = A()
    a.printB()
