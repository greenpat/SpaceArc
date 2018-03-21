class Stats:
    """
    An object represting core stats - inherited by items, effects
    """

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
        """
        :param args: objects of type Stats or inheriting from
        :return: a Stats object with attributes equal to the combined sum
        """
        assert all(isinstance(arg, Stats) for arg in args)
        return_stats = Stats()
        for stat in Stats.attribs:
            for _ in args:
                setattr(return_stats, stat,
                        getattr(return_stats, stat) + getattr(_, stat))
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
    a = Stats(strength=3, intellect=3)
    b = Stats(strength=1, intellect=-1)
    c = Stats(tenacity=5)
    print(Stats.combine(a, b, c).__dict__)
    print('that')

    from test.test_Stats import *

    unittest.main()

    print('this')
    Tests.Test_Stats.unittest.main()
