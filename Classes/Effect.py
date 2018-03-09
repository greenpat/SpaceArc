from Classes import Stats


class Effect(Stats):
    def __init__(self, name='Effect', temporary=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.temporary = temporary

    def __str__(self):
        return self.name.title()

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    test = Effect(strength=2, intellect=3, name='Test Effect')
    print(test)
    print(test.__dict__)
    print([test]*3)