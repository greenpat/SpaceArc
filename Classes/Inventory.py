from Classes.Item import Item
from Classes.Stats import Stats


class InventoryException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Inventory:
    def __init__(self, items=None, max_size=None, max_volume=None, max_mass=None):
        self.items = items
        if self.items is None:
            self.items = []
        self.max_size = max_size
        self.max_volume = max_volume
        self.max_mass = max_mass

    @property
    def mass(self):
        return (sum(x.mass for x in self.items))

    @property
    def volume(self):
        return (sum(x.volume for x in self.items))

    @property
    def stats(self):
        return Stats(
            life=sum(x.stats.life for x in self.items),
            energy=sum(x.stats.energy for x in self.items),
            strength=sum(x.stats.strength for x in self.items),
            speed=sum(x.stats.speed for x in self.items),
            intellect=sum(x.stats.intellect for x in self.items),
            tenacity=sum(x.stats.tenacity for x in self.items)
        )

    def add(self, new_item: 'Item'):
        if self.max_mass is not None:
            if self.mass + new_item.mass > self.max_mass:
                raise InventoryException('Inventory overweight!')
        if self.max_volume is not None:
            if self.volume + new_item.volume > self.max_volume:
                raise InventoryException('Inventory takes up too much space!')
        if self.max_size is not None:
            if len(self.items) == self.max_size:
                raise InventoryException('Only {0} item slots!'.format(self.max_size))
        self.items.append(new_item)
        print('\n< Added item: ' + new_item.name + ' >')

    def remove(self, old_item):
        self.items.remove(old_item)

    def remove_all_temporary(self):
        [self.items.remove(x) for x in self.items if x.temporary]


if __name__ == '__main__':
    test = Inventory()
    for i in range(10):
        test.add(Item('sword'))
