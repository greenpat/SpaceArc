from Classes import Stats
from Classes import Item
from Classes import Effect


class Actor:
    def __init__(self, name='Actor', **kwargs):
        self.name = name
        self.base_stats = Stats(**kwargs)
        self.items = []
        self.effects = []

    @property
    def stats(self):
        return (
            Stats.combine(
                self.base_stats,
                *self.items,
                *self.effects
            )
        )

    def display(self):
        temp_stats = self.stats
        ll, nl = 80, len(self.name)  # line length, name length
        print("")
        print(f"==========   {self.name}   " + "=" * (ll - 10 - 6 - nl))
        print("Items: ", end='')
        [print('[' + str(i) + ']', end=' ') for i in self.items]
        print("")
        print("Effects: ", end='')
        [print('[' + str(i) + ']', end=' ') for i in self.effects]
        print("")
        print(self.stats)
        print("=" * 80)


if __name__ == '__main__':
    test_actor = Actor(name='Testronaut', strength=3,
                       intellect=3, tenacity=3, speed=3)
    test_actor.items.append(Item('hose', strength=1))
    test_actor.items.append(Item('welder', tenacity=2))
    test_actor.effects.append(Effect("In Vacuum", intellect=12))
    test_actor.display()
