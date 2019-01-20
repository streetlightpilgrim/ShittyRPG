class x:
    def __init__(self):
        self.stat = 10
    def __repr__(self):
        return self.stat

class y(x):
    def __init__(self):
        super().__init__()
        self.stat = 5 + super().__repr__()
        print(self.stat)

z = y()
