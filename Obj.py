from Classes import *
from Text import *
import random

"""
This module contains global objects and core functions for gameplay
"""


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
    'Password': Effect('Password')
}

# Global consistent items
items = {
    'Laptop': Item('Laptop'),
    'Dog': Item('Dog'),
    'Tazer': Item('Tazer'),
    'Scripture': Item('Scripture'),
    'Money': Item('Money'),
    'Spiked Boots': Item('Spiked Boots'),
    'Lye': Item('Lye')
}


# checks for the global player and rolls "dice" based off of their stats
def statroll(statname: str):
    global player
    print('')
    if statname == 'random':
        input('< Challenge: [Random] >')
        return (random.random())
    else:
        num = int(getattr(player.stats, statname))
        input('< Challenge: [' + statname.capitalize() + '] ' + str(num) + ' >')
        return (sum([random.randint(0, 2) for x in range(num)]))


def opt(prompt, choices, possible=None, suppress_display=False,
        return_text=False, wipe=True, prompt_as_is: bool = False, topline=True):
    """
    :param prompt: The text presented to the player
    :param choices: A list of all possible dialogue choices
    :param possible: A boolean list of which choices are "available"
    :param suppress_display: Prevents player.display() from triggering
    :param return_text: If True opt returns text of choice instead of integer
    :param wipe: If True clears the screen of prior text
    :param prompt_as_is: If True prompt is printed without cleanup
    :param topline: If True prints a line of characters at top of prompt
    :return: Returns an integer corresponding to choice.
        If there are "unavailable" choices then there will be a mapping process
        If return_text is true then chosen text is returned instead
    """
    if possible == None:
        possible = [True] * len(choices)
    shown_choices = [c for c, p in zip(choices, possible) if p == True]
    valid_selected = False
    while (not valid_selected):
        if wipe:
            clrscr()
        if topline:
            line()
        if prompt_as_is:
            print(prompt)
        else:
            saprint(prompt, wipe=False, topline=False)
        print('')
        for i in range(len(shown_choices)):
            print(str(i + 1) + ': ', shown_choices[i])
        if not suppress_display:
            player.display()
        user_choice = input('[>')
        if user_choice == 'q':
            print("QUITTING GAME")
            raise ("Quit")
        try:
            user_choice = int(user_choice)
            if int(user_choice) - 1 in range(len(shown_choices)):
                valid_selected = True
        except:
            valid_selected = False
            user_choice = 999
    selected_value = shown_choices[user_choice - 1]
    return_value = choices.index(selected_value) + 1
    if return_text:
        return_value = choices[return_value - 1]
    return (return_value)


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