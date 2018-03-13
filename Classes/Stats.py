class Stats:
    # These attribs are core game design - there will only be four
    attribs = ['strength', 'speed', 'intellect', 'tenacity']

    def __init__(self,
                 strength=0,
                 speed=0,
                 intellect=0,
                 tenacity=0
                 ):
        self.strength = int(strength)
        self.speed = int(speed)
        self.intellect = int(intellect)
        self.tenacity = int(tenacity)

    def __str__(self):
        return (
            f"Strength: {self.strength: >2}     Speed: {self.speed: >2}     " +
            f"Intellect: {self.intellect: >2}      Tenacity: {self.tenacity: >2}")

    # combine adds stats objects together and returns a single stats object
    @staticmethod
    def combine(*args: 'Stats'):
        assert all(isinstance(arg, Stats) for arg in args)
        return_stats = Stats()
        for stat in Stats.attribs:
            for tba in args:
                setattr(return_stats, stat,
                        getattr(return_stats, stat) + getattr(tba, stat))
        return (return_stats)

    # set all stats to default value
    def reset(self, default_value=0):
        for stat in self.__dict__:
            setattr(self, stat, default_value)

    # all stats get multiplied - unsure if actually useful
    def multiply(self, x):
        for stat in Stats.attribs:
            setattr(self, stat, getattr(self, stat) * x)

    # Permanently modify a stats by adding another stats
    def add(self, other_stats: 'Stats'):
        assert (isinstance(other_stats, Stats))
        for stat in self.__dict__:
            setattr(self, stat,
                    getattr(self, stat) + getattr(other_stats, stat))


if __name__ == '__main__':

    a = Stats(strength=3)
    print(a.__dict__)
    b = Stats(strength=1, intellect=4)
    print(b.__dict__)
    print(Stats.combine(a, b).__dict__)
    print(a)
    print('%' * 80)