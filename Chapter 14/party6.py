# For this example, we move our PartyAnimal class into its own file. Then, we can ‘import’ the PartyAnimal class in a new file and extend it, as follows

from party_animal import PartyAnimal

class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points += 6
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.party()
j.six()
print(dir(j))
