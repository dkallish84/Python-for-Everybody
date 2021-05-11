# We use the class keyword to define the data and code that will make up each of the objects. The class keyword includes the name of the class and begins an indented block of code where we include the attributes (data) and methods (code).

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
