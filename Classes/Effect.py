from Classes.Stats import Stats


class Effect(Stats):
    def __init__(self, name='Effect', temporary=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.temporary = temporary
