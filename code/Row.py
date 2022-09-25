import Utils

class Row:
    def __init__(self, t):
        self.cells = t
        self.cooked = Utils.copy(t)
        self.isEvaled = False


