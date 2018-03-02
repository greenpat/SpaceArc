import Classes

class Inventory(list):

    @property
    def stats(self):
        return_stats = Classes.Stats()
        for stat in Classes.Stats.attribs:
            setattr(return_stats, stat, sum(getattr(x, stat) for x in self[:]))
        return return_stats

if __name__ == '__main__':
    test = Inventory()
    for i in range(10):
        test.append(Classes.Item('sword',strength=1))
    print(test)
    print(test[0].name)
    print([thing.name for thing in test])
    print(test.stats.__dict__)