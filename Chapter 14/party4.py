# If we want our object to be aware of these moments of construction and destruction, we add specially named methods to our object

class PartyAnimal:
    x = 0

    # Define a constructor
    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x += 1
        print('So far', self.x)

    # Define a destructor
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)
