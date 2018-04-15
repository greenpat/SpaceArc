from Text import *
import time
import Obj

if True:
    phase()
    for i in 'Welcome to...':
        if i in (' ','.'):
            time.sleep(.25)
        print(i, flush=True,end='')
        time.sleep(.1)
    time.sleep(.5)
    print('')

c = None

# Good ANSI arts:
# Graffiti, Rounded, Speed, Avatar, Small Slant

while c != 3:
    c = Obj.opt(r'''
/ ___\/  __\/  _ \/   _\/  __//  _ \/  __\/   _\
|    \|  \/|| / \||  /  |  \  | / \||  \/||  /  
\___ ||  __/| |-|||  \_ |  /_ | |-|||    /|  \_ 
\____/\_/   \_/ \|\____/\____\\_/ \|\_/\_\\____/
    
    
Please select an option.''',
                    ['Prologue',
                    'How to Play',
                    'Begin'],
            suppress_display = True, wipe=False, prompt_as_is=True, topline=True
                    )

    if c == 1:
        clrscr()
        line()
        print('''
   ___           __                  
  / _ \_______  / /__  ___ ___ _____ 
 / ___/ __/ _ \/ / _ \/ _ `/ // / -_)
/_/  /_/  \___/_/\___/\_, /\_,_/\__/ 
                     /___/           
        
        ''')
        saprint('''
        2309 CE: An era of realization.
        
        In the past 150 years, humankind has gained a practical self awareness. Policymakers rewrite laws to explicitly align individual interests against target outcomes. City-states, countries, and trade blocs are less distinguishable than ever before.
        
        For a time, the collective energy of the world tilts toward extraplanetary exploration. Research into sustainable interstellar travel flourishes. Money pours into eccentric propulsion systems. All people are invited to participate in the celebration of science.
        
        ''', wipe=False)
        pause()
        saprint('''
        The wayward star Gliese 709 makes an uninvited pass through humankind's solar system, plunging a system which had found order for hundreds of thousands of years into chaos. A vast number of frozen, dormant Oort objects are dragged back into near-Earth trajectory. A number of irregular moons of Neptune and Uranus collide with their parent planets. At least one is thrown towards the inner solar system.
        
        Humankind feverishly calculates collision paths and refurbishes its nuclear arsenal. It is all too uncertain whether the candle of civilization will finally be snuffed out.
        
        It is decided that the long-duration interstellar colonization vessels will be launched immediately.
        ''')
        pause()
    elif c == 2:
        clrscr()
        line()
        saprint('''
        How to play:
        
        SparArc is a sci-fi text based adventure game written using Python 3.
        As you progress through chapters, you will be prompted to make choices by entering the corresponding number into the console. Think choose-your-own adventure book with character persistence.
        
        At any choice prompt, type 'q' to quit.
        
        Enjoy!
        -Patrick
        ''')
        pause()
    elif c == 3:
        for i in range(20):
            print('----'*(i % 80)+'>>>', flush=True)
            #time.sleep(.1)

game['next'] = 'e001_start'
game['turns'] -= 1  # this chapter doesn't count