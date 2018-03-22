from Classes import Stats


class Item(Stats):
    """
    Inherits from stats, represents physical items that character has access to
    """
    def __init__(self, name='Item', temporary=False, **kwargs):
        self.name = name
        self.temporary = temporary
        super().__init__(**kwargs)

    def __str__(self):
        return self.name.title()

    def __repr__(self):
        return self.name

if __name__ == '__main__':
    x = Item('hat', strength=3, tenacity=1)
    print(x)
    testlist = [x] * 3
    print(testlist)
    print(f"This is my {x}!")
