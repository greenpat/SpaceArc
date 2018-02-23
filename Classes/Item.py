from Classes.Stats import Stats


class OutOfCharges(Exception):
    def __init__(self, message='No charges remaining!'):
        super().__init__(message)


class Item:
    def __init__(self, name='Item', mass=1, volume=1, charges=None, max_charges=None, temporary=False,
                 **kwargs):
        self.name = name
        self.mass = mass
        self.volume = volume
        self.charges = charges
        self.max_charges = max_charges
        self.temporary = temporary
        self.stats = Stats(**kwargs)

    def use(self):
        if self.charges == None:
            pass
        elif self.charges > 0:
            self.charges = self.charges - 1
            print(self.charges)
        else:
            raise OutOfCharges()


if __name__ == '__main__':
    print('Testing Item()')
    sword = Item('Sword', mass=2, strength=1)
    print(sword.__dict__)
    print(sword.stats)
