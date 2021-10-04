import random

class Data:
    size = 0
    rng = 0
    data = []

    def __init__(self, size:int, rng:int):
        self.size = size
        self.rng = rng
        for i in range(size):
            self.data.append(random.randint(0, rng))
        return

    def __repr__(self) -> str:
        return str(self.data)

data1 = Data(10, 10)
print(data1)