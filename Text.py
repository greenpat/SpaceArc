import time
import re
import Obj
import random

"""
This module contains functions related to parsing and cleaning text in order to
ultimately display to the player. The assumption for SpaceArc is that the window
will be 80 characters wide.
"""


def saprint(docstring='', wipe=True, topline=True):
    """
    :param docstring: long, messy string to be formatted
    :param wipe: whether the current display will be wiped clean
    :param topline: whether a line will precede text
    :return: None, print cleaned string as side effect
    """
    if wipe: clrscr()
    if topline: line()

    # Clean initial input text
    s = re.sub('\t', ' ',
               docstring)  # leading tabs (common) replaced throughout
    s = re.sub('^[\\n\\s]+|[\\n\\s]+$', '', s)  # leading/trailing space removed
    s = re.sub('[\\n\\s]{2,}', ' {eol} ', s)  # marker for empty lines

    # Print up to 80 chars wide but preserve paragraphs
    s = s.split(' ')
    nchar = 0
    while s:
        c = s.pop(0)
        if c == '{eol}':
            print('\n')
            nchar = 0
            continue
        elif nchar + len(c) > 80:
            print('')
            nchar = 0
        print(c, end=' ')
        nchar = nchar + len(c) + 1
    print('')


# Not true clear screen but should empty the visible command prompt
def clrscr():
    print('\n' * 100)


# Print the default line of characters
def line(char='-'):
    print(char * 80)


# Briefly break text by requiring user to push button
def pause(prompt: str = '(Press enter)'):
    print('')
    input(prompt)


# Standard user prompt with logic to govern choice availability
def opt(prompt, choices, possible=None, suppress_display=False,
        return_text=False, wipe=True, prompt_as_is: bool = False,
        topline=False):
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
    valid_selected = False

    if possible == None:
        possible = [True] * len(choices)
    shown_choices = [c for c, p in zip(choices, possible) if p == True]

    while (not valid_selected):

        # Secion 1: Prompt
        if wipe: clrscr()
        if topline: line()
        if prompt_as_is:
            print(prompt)
        else:
            saprint(prompt, wipe=False, topline=False)

        # Section 2: Choices
        print('')
        for i in range(len(shown_choices)):
            print(str(i + 1) + ': ', shown_choices[i])
        if not suppress_display:
            Obj.player.display()

        # Section 3: Input
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

    # Section 4: Return Value
    selection = shown_choices[user_choice - 1]
    if return_text:
        return selection
    else:
        return choices.index(selection) + 1


def statroll(statname: str, player=Obj.player):
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
