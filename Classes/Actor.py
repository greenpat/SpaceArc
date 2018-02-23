from Classes.Inventory import Inventory
from Classes.Stats import Stats


class Actor:
    def __init__(self, name='Actor', **kwargs):
        self.name = name
        self.base_stats = Stats(**kwargs)
        self.inventory = Inventory()
        self.effects = []
        self.life = self.stats.life
        self.energy = self.stats.energy

    @property
    def stats(self):
        return (
            Stats.combine(
                self.base_stats,
                self.inventory.stats,
                *self.effects
            )
        )

# todo: update this display
    def display(self):
        temp_nums = [str(i).rjust(2, ' ') for i in self.stats.__dict__.values()]
        print('')
        print(('=' * 10) + ('   ') + self.name + ('   ') + ('=' * (80 - (len(self.name) + 16))))
        print("Items: ", end='')
        for i in self.inventory.items:
            print('[' + i.name + '] ', end='')
        print('')
        print("Effects: ", end='')
        for i in self.effects:
            print('[' + i.name + '] ', end='')
        print('')
        print('Life:    ', str(round(self.life, 1)), '/', temp_nums[0], '      Energy:   ',
              str(round(self.energy, 1)), '/',
              temp_nums[1])
        print(
            'Strength: ', temp_nums[2], ' Speed:    ', temp_nums[3], ' Intellect:', temp_nums[4], ' Tenacity: ',
            temp_nums[5], sep='')
        print('=' * 80)


if __name__ == '__main__':
    test_actor = Actor(name='Testronaut', life=100, energy=50, strength=3, intellect=3, tenacity=3, speed=3)
    test_actor.display()


