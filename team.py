# team.py
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


    def view_all_heroes(self):
        '''Prints out all the hereos to the console'''
        for hero in self.heroes:
            print(hero.name)
