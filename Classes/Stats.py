class Stats:
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

    # combine adds stats objects together and returns a single stats object
    @staticmethod
    def combine(*args: 'Stats'):
        for tba in args:  # tba 'to be added'
            assert (isinstance(tba, Stats))  # should only add stats
        return_stats = Stats()
        for stat in Stats.attribs:
            for tba in args:
                setattr(return_stats, stat, getattr(return_stats, stat) + getattr(tba, stat))
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
            setattr(self, stat, getattr(self, stat) + getattr(other_stats, stat))