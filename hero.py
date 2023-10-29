# hero.py
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:

    starting_health = 100

    def __init__(self, name: str = '', starting_health = 100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health


    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)


    def attack(self):
        '''Calculate total damage from all ability attacks'''
        total_damage = 0
        # loop through all hero's abilities
        for ability in self.abilities:
            # add damage of each attack to our running total
            total_damage += ability.attack()
        # returning total damage
        return total_damage


    def add_armor(self, armor):
        '''Add armor to armors list'''
        self.armors.append(armor)


    def defend(self):
        '''Calculate the total block amount from all armor blocks.return: total_block:Int'''
        total_block = 0
        if len(self.armors) > 0 and self.current_health > 0: 
            for armor in self.armors:
                total_block += armor.blocks()
        return total_block


    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        total_damage = damage - self.defend()
        total_damage = max(0, total_damage) # ensures damage isnt negative
        self.current_health -= total_damage
        return self.current_health


    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health <= 0:
            return False
        else:
            return True


    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in
        prints the chances of each person winning'''

        total_power = self.starting_health + opponent.starting_health
        hero_chance = (self.starting_health / total_power) * 100
        opponent_chance = (opponent.starting_health / total_power) * 100

        print(f"Your chances of winning: {hero_chance}%")
        print(f"Opponent chance of winning: {opponent_chance}%")

        if len(self.abilities) == 0 and  len(opponent.abilities) == 0:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():
            opponent_damage = self.attack()
            self_damage = opponent.attack()

            opponent.take_damage(opponent_damage)
            self.take_damage(self_damage)

        if not opponent.is_alive():
            print(f"{self.name} won!")
            return
        elif not self.is_alive():
            print(f"{opponent.name} won!")
            return

    def add_weapon(self, weapon):
        '''Add weapon to self.abilites'''
        self.abilities.append(weapon)





    #def chances(self, opponent): (move to fight)
        #'''Creating chances of winning for each player'''
        #total_power = self.power + opponent.power
        #win_chances_self = self.power / total_power
        #win_chances_opponent = opponent.power / total_power

       # print(f"{self.name} chances of winning is: {win_chances_self}")
       # print(f"{opponent.name} chacnes of winning is: {win_chances_opponent}")
    #def fight(self, opponent):
        #'''Current Hero will take turns fighting the  opponent hero passed in'''
        #total_power = self.power + opponent.power
        #win_chances_self = round((self.power / total_power) * 100, 2)
        #win_chances_opponent = round((opponent.power / total_power) * 100, 2)

        #print(f"{self.name}s chances of winning: {win_chances_self}%")

        #contenders = [self, opponent]
        #winner = random.choice(contenders)
        #loser = [hero for hero in contenders if hero != winner][0]

        #print(f"{winner.name} defeats {loser.name}")
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
#fight
    #hero1 = Hero("Wonder Woman", 1000)
    #hero2 = Hero("Cat Woman", 988)
    #hero1.fight(hero2)
#ability
    #ability = Ability("great debugging", 50)
    #ability_2 = Ability("dodge", 20)
    #hero = Hero("Batman", 200)
    #hero.add_ability(ability)
   #hero.add_ability(ability_2)
    #print(hero.abilities)
#attack
    #ability = Ability("excellent debugging", 50)
    #another_ability = Ability("samrty pants", 90)
    #hero = Hero("Batman", 300)
    #hero.add_ability(ability)
    #hero.add_ability(another_ability)
    #print(hero.attack())
#Armor/ defend
    #armor_1 = Armor("Shield", 10)
    #armor_2 = Armor("Helemt", 78)
    #hero_1 = Hero("Batman")
    #print("armor 1")
    #hero_1.add_armor(armor_1)
    #print(hero_1.defend())
    #print("------------")
    #print("armor 2")
    #hero_1.add_armor(armor_2)
    #print(hero_1.defend())
# take_damage
    #hero = Hero("Batman", 200)
    #shield = Armor("Shield", 50)
    #hero.add_armor(shield)
    #hero.take_damage(50)
    #print(hero.current_health)
# is_alive
    #hero = Hero("Batman", 200)
    #hero.take_damage(150)
    #print(hero.is_alive())
    #hero.take_damage(15000)
    #print(hero.is_alive())
# fight
    #hero1 = Hero("Wonder Woman")
    #hero2 = Hero("Cat Woman")
    #ability1 = Ability("Super Speed", 300)
    #ability2 = Ability("Super Eyes", 130)
    #ability3 = Ability("Wizard Wand", 80)
    #ability4 = Ability("Wizard Beard", 20)
    #hero1.add_ability(ability1)
    #hero1.add_ability(ability2)
    #hero2.add_ability(ability3)
    #hero2.add_ability(ability4)
    #hero1.fight(hero2)
# add_weapon
    hero = Hero("Wonder Woman")
    weapon = Weapon("Cat Woman", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
