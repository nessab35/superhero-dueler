# hero.py
import random

class Hero:

    starting_health = 100

    def __init__(self, name: str = '', power: int = 100, starting_health = 100):
        self.name = name
        self.power = power
        self.starting_health = starting_health
        self.current_health = starting_health

    #def chances(self, opponent): (move to fight)
        #'''Creating chances of winning for each player'''
        #total_power = self.power + opponent.power
        #win_chances_self = self.power / total_power
        #win_chances_opponent = opponent.power / total_power

       # print(f"{self.name} chances of winning is: {win_chances_self}")
       # print(f"{opponent.name} chacnes of winning is: {win_chances_opponent}")


    def fight(self, opponent):
        '''Current Hero will take turns fighting the  opponent hero passed in'''
        total_power = self.power + opponent.power
        win_chances_self = round((self.power / total_power) * 100, 2)
        win_chances_opponent = round((opponent.power / total_power) * 100, 2)

        print(f"{self.name}s chances of winning: {win_chances_self}%")
        print(f"{opponent.name}s chances of winning: {win_chances_opponent}%")

        contenders = [self, opponent]
        winner = random.choice(contenders)
        loser = [hero for hero in contenders if hero != winner][0]

        print(f"{winner.name} defeats {loser.name}")
        # TODO: fight each hero until a victor emerges
        #phases to implement:
        # 1) randomly chooses winner
        # hint: look into random library, more specifically the choice method



# Testing
if __name__ == "__main__":
    #my_hero = Hero("Batman", 100)
    #print(my_hero.name)
    #print(my_hero.current_health)

    #hero1 = Hero("Wonder Woman")
    #hero2 = Hero("Cat Woman")
    #hero1.fight(hero2)

    hero1 = Hero("Wonder Woman", 1000)
    hero2 = Hero("Cat Woman", 988)

    hero1.fight(hero2)
