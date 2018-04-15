# Main script
# Repeats until you want to close the game
continue_playing_the_game = True
while continue_playing_the_game:

    # loads shared resources (which encounters also utilize)
    # includes "player" which is the central focus of game
    import Obj
    import Text
    import time

    # Default beginning
    Obj.game_restart()

    # game contains info about your single game session
    # dead can be good or bad
    while Obj.game['dead']==False:

        # On verge of moving forward, passing 'next' to 'prev'
        Obj.game['prev'] = Obj.game['next']

        # Run the chapter! Good luck!!
        __import__('Episodes.'+Obj.game['next'])

        # Remove old chapter artifacts
        try:
            del sys.modules['Episodes.'+game['prev']]
        except:
            pass

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
        game['next'] = 'e001_start'
        Text.phase()
    elif c == 2:
        continue_playing_the_game = False

quit()