import time
import re
import Obj
import random

"""
This module contains functions related to parsing and cleaning text in order to
ultimately display to the player. The assumption for SpaceArc is that the window
will be 80 characters wide.
"""

def saprint(docstring = '', wipe=True, topline=True):
    """
    :param docstring: long, messy string to be formatted
    :param wipe: whether the current display will be wiped clean
    :param topline: whether a line will precede text
    :param width: how many chars wide before newline
    :return: cleaned up string
    """
    if wipe: clrscr()
    if topline: line()

    s = re.sub('\t',' ',docstring)  # leading tabs (common) replaced throughout
    s = re.sub('^[\\n\\s]+|[\\n\\s]+$','',s)  # leading/trailing space removed
    s = re.sub('[\\n\\s]{2,}','\n\n',s)  # extra space of any type becomes newlines

    # Replace lines with shorter lines up to 80 chars
    print(re.sub('([\\w .,]{0,80})(?![\\w .,]+$)[ \\n]','\\1\\n',s))

# Not true clear screen but should empty the visible command prompt
def clrscr():
    print('\n'*100)

# Print the default line of characters
def line(char='-'):
    print(char*80)

# Briefly break text by requiring user to push button
def pause(prompt:str = '(Press enter)'):
    print('')
    input(prompt)

# Standard user prompt with logic to govern choice availability
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

def statroll(statname: str, player = Obj.player):
    """
    :param statname: a string, one of Classes.Stats.attribs or 'random'
    :player: the Actor whose stats are being rolled on
    :return: returns a dice roll [0-2]*stat or uniform dist for random [0-1]
    """
    print('')
    if statname == 'random':
        input('< Challenge: [Random] >')
        return (random.random())
    else:
        num = int(getattr(player.stats, statname))
        input('< Challenge: [' + statname.capitalize() + '] ' + str(
            num) + ' >')
        return (sum([random.randint(0, 2) for x in range(num)]))

# blastoff animation
def phase():
    picture = r'''
      /\
     (  )
     (  )
    /|/\|\
   /_||||_\
      #
      ##
      ###
      ####
      ######
       #######
       #########
        ##########
            ############
                  ############
                        ############
                              ############
                                    ############
                              #####################
                        ################################
                    ###########################################
                ######################################################
        ###################################################################
################################################################################
    '''.split('\n')
    for i in picture:
        print(i, flush=True)
        time.sleep(.10)
