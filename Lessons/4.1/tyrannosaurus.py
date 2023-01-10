'''
Definition of the Tyrannosaurus class
'''

from dinosaur import *
from carnivore import *

class Tyrannosaurus(Dinosaur, Carnivore):
    def __init__(self, size, weight, diet):
        Dinosaur.__init__(self, size, weight)
        Carnivore.__init__(self, diet)

