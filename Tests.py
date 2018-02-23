from Utilities.Resources import *

print(id(player))
player.display()
player.base_stats.add(Stats(intellect=3))
print(id(player))
player.display()

def reset_player_to_default_starting_values():
    print('resetting player')
    global player
    print(id(player))
    player.display()
    del(player)
    player = Actor(life=100, strength=3, speed=3, intellect=3, tenacity=3)
    print(id(player))
    player.display()
    print('done resetting player')

reset_player_to_default_starting_values()

print(id(player))
player.display()