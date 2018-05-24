# loads shared resources (which encounters also utilize)
# includes "player" which is the central focus of game
import Obj
from Text import *
import sys

# Main script
# Repeats until you want to close the game
continue_playing_the_game = True
while continue_playing_the_game:

    # game contains info about your single game session
    # dead can be good or bad
    while Obj.game['dead'] == False:

        # On verge of moving forward, passing 'next' to 'prev'
        Obj.game['prev'] = Obj.game['next']

        # Run the chapter! Good luck!!
        __import__('Episodes.' + Obj.game['next'])

        # Automatic cleanup of temporary items & effects from chapter
        Obj.player.drop_temp()

        # Remove old chapter artifacts
        try:
            del sys.modules['Episodes.' + Obj.game['prev']]
        except:
            pass

        # This could be considered a "score"
        Obj.game['turns'] += 1

    # Death scenario
    end_message()
    c = opt("Play again?\n", ['Yes', 'No'], wipe=False, suppress_display=True)
    if c == 1:
        # Player instantiated in this module - wiping clean
        Obj.game_restart(start_chapter='e001_start')
        clrscr()
    elif c == 2:
        continue_playing_the_game = False

quit()
