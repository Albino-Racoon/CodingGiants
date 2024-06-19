from random import randint, choice

class Character:
    def __init__(self):
        self.name = ""
        self.life = 1
        self.max_life = 1

    def do_attack(self, enemy):
        attack = randint(0, 3)
        if attack == 0:
            print(f"{enemy.name} dodges {self.name}'s attack.")
        else:
            print(f"{self.name} attacks {enemy.name}, dealing {attack} damage.")
            enemy.life -= attack

class Enemy(Character):
    def __init__(self, player):
        super().__init__()
        self.name = choice(['Goblin', 'Skeleton', 'Zombie'])
        self.life = randint(1, player.life)

class Player(Character):
    def __init__(self):
        super().__init__()
        self.life = 10
        self.max_life = 10
        self.name = input('Enter player name: ')

    def rest(self):
        print(f'{self.name} is resting, life: {self.life}/{self.max_life}')
        self.life += 1
        if self.life > self.max_life:
            self.life = self.max_life

    def combat(self, enemy):
        combat = True
        while combat:
            print(f"Player's life: {self.life}")
            print(f"{enemy.name}'s life: {enemy.life}")
            combat_action = input('Action (attack, run): ')
            if combat_action == 'attack':
                self.do_attack(enemy)
                if enemy.life <= 0:
                    print(f'{self.name} defeats {enemy.name}')
                    return True
                enemy.do_attack(self)
            elif combat_action == 'run':
                print(f'{self.name} runs')
                enemy.do_attack(self)
                combat = False
            else:
                print('Unknown action')

            if self.life <= 0:
                print(f'{self.name} dies')
                return False
        return True

player = Player()
game = True
while game:
    action = input('Action (explore, rest): ')

    if action == 'explore':
        if randint(0, 1) == 0:
            print(f'{player.name} found a cave')
        else:
            enemy = Enemy(player)
            print(f'{player.name} stumbled upon a {enemy.name}')
            game = player.combat(enemy)
    elif action == 'rest':
        player.rest()
    else:
        print('Unknown action')


"""
1. kopiraj vso kodo
2. zaženi vso kodo da se prepričaš da deluje
3. prevedi kodo v slovenščino ( tekstovne izpise)
4. dodaj še 5 vrst sovražnikov (npr. Ork, Troll, Zmaj, Vilin, Vampir)

"""