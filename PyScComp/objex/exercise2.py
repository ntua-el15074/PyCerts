class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(f'my man {self.name} is a Human')

class Poopster(Human):
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __str__(self):
        if self.action:
            print(f'Mister {self.name} is a big ol\'n Poopster')
        else:
            print(f'Mister {self.name} ain\'t no Poopster')

    def poop(self):
        print('pritz')
        print('wowowoowoow')


x = input('Did you poop today?')
if x == 'yes':
    action = True
else:
    action = False

poop = Poopster('Peter', action)
poop.__str__()
poop.poop()

print(type(poop))
print(dir(poop))
