from Classes.Actor import Actor
from Classes.Effect import Effect
from Classes.Item import Item
from Utilities.Text import *
import random

# This file contains

player = Actor(life=100, strength=3, speed=3, intellect=3, tenacity=3)

player_default = Actor("Testronaut", life = 100, energy = 100, strength = 4, speed = 4, intellect = 4, tenacity = 4)

game = {
    'next': 'e000_intro',
    'dead': False,
    'turns': 0
}

reminder = ['Spirited','Reckless','Grizzled','Resourceful','Empathetic','Heroic','Biological','Technical','Physical','Social','Laptop','Dog','Tazer','Scripture','Money']

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

items = {
    'Laptop':Item('Laptop'),
    'Dog':Item('Dog'),
    'Tazer':Item('Tazer'),
    'Scripture':Item('Scripture'),
    'Money':Item('Money'),
    'Spiked Boots':Item('Spiked Boots'),
    'Lye':Item('Lye')
}

# checks for the global player and rolls based off of their stats
def statroll(statname:str):
    print('')
    if statname == 'random':
        input('< Challenge: [Random] >')
        print('')
        return(random.random())
    else:
        num = int(getattr(player.stats, statname))
        input('< Challenge: ['+statname.capitalize()+'] '+str(num)+' >')
        print('')
        return(sum([random.randint(0,2) for x in range(num)]))

# Choice repeatedly prompts the user with a number of choices
# the numbers are automatically generated
def opt(prompt, choices, possible=None, suppress_display=False, return_text=False, wipe=True, prompt_as_is:bool = False, topline = True):
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
            saprint(prompt, wipe = wipe, topline=False)
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
    selected_value = shown_choices[user_choice-1]
    return_value = choices.index(selected_value)+1
    if return_text:
        return_value = choices[return_value-1]
    return (return_value)
