# armor.py
import random

class Armor:
    def __init__(self, name, max_block: int = 0):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        '''Returns an int between 0 and max_block strenght'''
        random_value = random.randint(0, self.max_block)
        return random_value


# testing
if __name__ == "__main__":
    armor = Armor("debugging shield", 10)
    print(armor.name)
    print(armor.block())
