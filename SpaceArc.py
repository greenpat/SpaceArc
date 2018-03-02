# Main script
# Repeats until you want to close the game
continue_playing_the_game = True
while continue_playing_the_game:

    # loads shared resources (which encounters also utilize)
    # includes "player" which is the central focus of game
    from Util.Resources import *

    # game contains info about your single game session
    # dead can be good or bad
    while game['dead']==False:

        # Refer to Util.Resources
        game['prev'] = game['next']

        # Allows for replay of same scenario
        try:
            del sys.modules['Episodes.'+game['next']]
        except:
            assert(True)

        # Run the chapter!! Good luck!
        __import__('Episodes.'+game['next'])

        # Remove old chapter artifacts
        try:
            del sys.modules['Episodes.'+game['prev']]
        except:
            assert(True)

        # This could be considered a "score"
        game['turns'] += 1

    # Death scenario
    pause()
    clrscr()
    line()
    print('')
    print(game['dead'])
    print('')
    line()
    print('')
    print("Thanks for playing!")
    print("Chapters: "+str(game['turns']))
    print('')
    c = opt("Play again?\n",['Yes','No'], wipe=False, suppress_display=True)
    if c == 1:
        clrscr()
        # Player instantiated in this module - wiping clean
        del sys.modules['Util.Resources']
        from Util.Resources import *
        game['next'] = 'e001_start'
        phase()
    elif c == 2:
        continue_playing_the_game = False

quit()