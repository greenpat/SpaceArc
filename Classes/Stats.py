class Stats:
    attribs = ['life', 'energy', 'strength', 'speed', 'intellect', 'tenacity']

    @staticmethod
    def combine(*args: 'Stats'):
        for tba in args:  # tba 'to be added'
            assert (isinstance(tba, Stats))  # should only add stats
        return_stats = Stats()
        for stat in Stats.attribs:
            for tba in args:
                setattr(return_stats, stat, getattr(return_stats, stat) + getattr(tba, stat))
        return (return_stats)

    def __init__(self,
                 life=0,
                 energy=0,
                 strength=0,
                 speed=0,
                 intellect=0,
                 tenacity=0
                 ):
        self.life = int(life)
        self.energy = int(energy)
        self.strength = int(strength)
        self.speed = int(speed)
        self.intellect = int(intellect)
        self.tenacity = int(tenacity)

    def reset(self):
        for stat in self.__dict__:
            setattr(self, stat, 0)

    def multiply(self, x):
        # all stats get multiplied
        for stat in Stats.attribs:
            setattr(self, stat, getattr(self, stat) * x)

    def add(self, other_stats: 'Stats'):
        assert (isinstance(other_stats, Stats))
        for stat in self.__dict__:
            setattr(self, stat, getattr(self, stat) + getattr(other_stats, stat))
