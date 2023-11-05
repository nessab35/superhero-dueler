from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena():
    def __init__(self, team_one = None, team_two = None):
        '''Insttantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = team_one
        self.team_two = team_two


    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")
        return Ability(name, int(max_damage))


    def create_weapon(self):
        ''''Prompy user for Weapon Information
        return Weapon with values from user input
        '''
        name = input("What is the weapon name? ")
        max_damage = input("What is max damage of your weapon? ")
        return Weapon(name, int(max_damage))


    def create_armor(self):
        ''''Prompt user for Armor inforamtion
        return Armor with values from user input
        '''
        name = input("What is your armor name? ")
        max_block = input("What is the max block of your armor? ")
        return Armor(name, int(max_block))


    def create_hero(self):
        '''Prompt user for Hero informaiton 
        return Hero with vallues from user input
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding item\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_weapon(self.create_armor())
        return hero


    def build_team_one(self):
        '''Proimpt the user to build team_one'''
        if self.team_one == None:
            team_name = input("what is the name of Team One?> ")
            self.team_one = Team(team_name)

        numOfTeamMembers = int(input("How many members woudld you like on Team one?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)


    def build_team_two(self):
        '''Prompy the user to build team_two'''
        if self.team_two == None:
            team2_name = input("What is the name of Team Two?> ")
            self.team_two = Team(team2_name)

        numOfTeamMembers2 = int(input("How many members would you like on Team two?> "))
        for i in range(numOfTeamMembers2):
            hero = self.create_hero()
            self.team_two.add_hero(hero)


    def team_battle(self):
        '''Battle team_one and team_two together'''
        self.team_one.attack(self.team_two)


    def show_stats(self):
        '''Prints team statistics to terminal'''
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # Displays the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        #  Displays the average K/D for Team Two
        team2_kills = 0
        team2_deaths = 0
        for hero in self.team_two.heroes:
            team2_kills += hero.kills
            team2_deaths += hero.deaths
        if team2_deaths == 0:
            team2_deaths = 1
        print(self.team_two.name + "average K/D was: " + str(team2_kills / team2_deaths))


        # List of heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("Survived from " + self.team_one.name + ": " + hero.name)

        # List of heroes from Team Two that survived
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("Survived from " + self.team_two.name + ": " + hero.name)



# testing
if __name__ == "__main__":
    game_running = True

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play again? Y or N: ")

        if play_again.lower() == "n":
            game_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
