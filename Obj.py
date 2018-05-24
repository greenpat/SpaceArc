from Classes import *

"""
This module contains global objects and core functions for gameplay
"""

game = {
    'next': 'e000_intro',
    'dead': False,
    'turns': 0
}
player = Actor(strength=3, speed=3, intellect=3, tenacity=3)


# Wipe the slate clean or possibly in future version load save
def game_restart(start_chapter='e000_intro',
                 save_player=Actor(strength=3, speed=3, intellect=3,
                                   tenacity=3)):
    global game
    global player
    game = {
        'next': start_chapter,
        'dead': False,
        'turns': 0
    }
    player = save_player


# While writing episodes, get reminder of all global effects & items
def remind():
    print("=" * 80)
    print("Global effects")
    print([i.name for i in list(effects.values())])
    print("Global items")
    print([i.name for i in list(items.values())])


# Global consistent effects
effects = {
    'Spirited': Effect('Spirited', tenacity=2, speed=1, intellect=-1),
    'Reckless': Effect('Reckless', speed=2, tenacity=1, intellect=-1),
    'Grizzled': Effect('Grizzled', strength=2, tenacity=1, speed=-1),
    'Resourceful': Effect('Resourceful', intellect=2, speed=1, strength=-1),
    'Empathetic': Effect('Empathetic', intellect=1, speed=1),
    'Heroic': Effect('Heroic', strength=1, tenacity=1),
    'Biological': Effect('Biological'),
    'Technical': Effect('Technical'),
    'Physical': Effect('Physical'),
    'Social': Effect('Social'),
    'Password': Effect('Password', temporary=True)
}

# Global consistent items
items = {
    'Laptop': Item('Laptop'),
    'Dog': Item('Dog'),
    'Tazer': Item('Tazer'),
    'Scripture': Item('Scripture'),
    'Money': Item('Money'),
    'Spiked Boots': Item('Spiked Boots', temporary=True),
    'Lye': Item('Lye', temporary=True)
}

if __name__ == '__main__':
    game_restart()
    remind()
    player.items.append(items['Laptop'])
    player.effects.append(effects['Heroic'])
    x = opt('Test prompt.', ['Choice A', 'Choice B', 'Choice C'])
    print(x)
    x = opt('Test prompt (text).', ['Choice A', 'Choice B'], return_text=True)
    print(x)
    x = statroll('random')
    print(x)
    x = statroll('intellect')
