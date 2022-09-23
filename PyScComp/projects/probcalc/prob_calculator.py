import random

class Hat:
    def __init__(self, **data):
        self.contents = []
        self.datakeys = list(data.keys())
        self.datavalues = list(data.values())
        for item in range(0, len(self.datakeys)):
            for _ in range(0 ,self.datavalues[item]):
                self.contents.append(self.datakeys[item])

    def __str__(self):
        return str(self.contents)

    def draw(self, count):
        if count > len(self.contents):
            return self.contents
        else:
            for _ in range(0, count):
                randint = random.randint(0, len(self.contents) - 1)
                self.contents.pop(randint)
            return self.contents

    def contains(self, other):
        j = 0
        for i in range(0, len(other.contents)):
            if other.contents[i] in self.contents:
                j += 1
        return j == len(other.contents) - 1

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    hat2 = Hat(**expected_balls)
    for _ in range(0, num_experiments):
        temp = hat
        temp.draw(num_balls_drawn)
        if temp == expected_balls:
            m += 1
    probability = m/num_experiments
    return probability

hat = Hat(black=6, red=4, green=3)
hat2 = Hat(black =1, red=2, green = 1)
print(hat)
print(hat2)
print(hat.contains(hat2))