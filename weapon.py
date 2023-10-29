# weapon.py
from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        '''This method returns a random value between 
        one half to the full attack power of the weapon'''
        # getting half of max damage
        half_of_max = self.max_damage // 2
        # chooses a random number between half of max damage and max damage
        return random.randint(half_of_max, self.max_damage)
