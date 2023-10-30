# team.py
import random

class Team():
    def __init__(self, name: str = ''):
        '''Initilaize your team with it's team name and an empty list of heroes'''
        self.name = name
        self.heroes = list()


    def add_hero(self, hero):
        '''Add Hero object to self.heroes'''
        self.heroes.append(hero)


    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.'''
        foundHerro = False
        # loop through each hero in our list
        for hero in self.heroes:
            #if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to true
                foundHerro = True
        # if looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHerro:
            return 0


    def stats(self):
        '''Print team stats'''
        for hero in self.heroes:
            if hero.death == 0:
                hero.death += 1
            kd = hero.kills/ hero.deaths
            print(f"{hero.name} Kill/Deaths: {kd}")


    def revive_heroes(self, health= 100):
        '''Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health


    def view_all_heroes(self):
        '''Prints out all the hereos to the console'''
        for hero in self.heroes:
            print(hero.name)


    def attack(self, other_team):
        '''Battle each team against each other'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            my_hero = random.choice(living_heroes)
            opponent_hero = random.choice(living_opponents)
            my_hero.fight(opponent_hero)

            if hero.is_alive():
                living_opponents.remove(opponent_hero)
            else:
                living_heroes.remove(my_hero)
