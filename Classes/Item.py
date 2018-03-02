import Classes


class Item(Classes.Stats):
    def __init__(self, name='Item', temporary=False, **kwargs):
        self.name = name
        self.temporary = temporary
        super().__init__(**kwargs)