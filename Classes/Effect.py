import Classes.Stats

class Effect(Classes.Stats):
    def __init__(self, name='Effect', temporary=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.temporary = temporary

if __name__=='__main__':
    test = Effect(strength=2, intellect=3, name='Test Effect')
    print(test)
    print(test.__dict__)