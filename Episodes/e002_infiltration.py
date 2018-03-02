from Util.Resources import *

clrscr()
line()
print(r'''
   ____     ____ ____           __  _         
  /  _/__  / _(_) / /________ _/ /_(_)__  ___ 
 _/ // _ \/ _/ / / __/ __/ _ `/ __/ / _ \/ _ \
/___/_//_/_//_/_/\__/_/  \_,_/\__/_/\___/_//_/
                                              
''')
saprint('''
It won\'t be easy, but you need to get aboard that ark.

Most other people are either hiding, stockpiling supplies, or looting. A few might be crazy enough to try escaping the Earth.
''', wipe = False, topline=False)
pause()
loc = 'home'

props = []

def home():
    global loc
    c = opt('''
    There is the direct route - through the facility checkpoint. You have no clue what security will be like at a time like this.
    
    You couldn't tunnel underneath, but you might be able to get through the perimeter fence and break in through the back.
    
    Maybe you could handle this the civilized way, by applying for passengership.
            ''',
            [
                'Drive through the checkpoint.',
                'Scale the fence.',
                'Inquire about becoming a passenger.'
            ]
            )
    if c == 1: loc = 'checkpoint'
    if c == 2: loc = 'fence'
    if c == 3: loc = 'couch'

def couch():
    global loc
    global props
    c = opt('You dial the registered number, but there is no response.',
            ['Try again in an hour.',
             'Stay on Earth.',
             'Change strategies.',
             '[Social] Dial the regional ark site manager.'],
            possible=[True,True,True,
                      effects['Social'] in player.effects and not 'permit' in props
                      ])
    if c == 1: loc = 'grounded'
    if c == 2: loc = 'earth'
    if c == 3: loc = 'home'
    if c == 4:
        saprint('''
        ... ... ... "{}, why are you calling me now? The world is burning!"
        
        "I'm going to be honest with you. I need your help getting aboard the ark."
        
        You argue for some time.
        '''.format(player.name))
        roll = statroll('tenacity')
        if roll >= 5:
            saprint('''
            "You know what? Try it. I wish you the best. The ark isn't adequately prepped for launch and you'll probably get wiped out by an errant asteroid.
            
            Tell the sentry to issue a contingency pass with temporary authorization 'Esperanto' ... and for God's sake don't hurt anyone."
            ''')
            props.append('permit')
            player.effects.append(effects['Password'])
            loc = 'home'
            pause('<You have learned a password.>')
        else:
            saprint('''
            "We've been over this, I can't help you!"
            
            It was worth a shot.
            ''')
            props.append('permit')
            loc = 'home'
            pause('< The ark site manager declines to help >')

def earth():
    saprint('''You decide to stay on Earth.
            
            It doesn\'t matter how you eventually die, nothing is worse than life without imagination.
            ''')
    game['dead'] = 'Didn\'t even try.'

def grounded():
    global loc
    c = opt('One hour later the phone now immediately returns a busy signal.',
            ['Try again tomorrow.',
             'Stay on Earth.',
             'Change strategies.'])
    if c == 1:
        clrscr()
        saprint('''You settle in for the night and turn on the news.
        Some time later a thunderous roar sweeps through the town, shattering
        windows and setting off car alarms. The newscasters announce what you
        already knew. The ark has left. You might as well get comfortable.
        ''')
        game['dead'] = 'Grounded by indecisiveness.'
    elif c == 2:
        loc = 'earth'
    elif c == 3:
        clrscr()
        saprint('''You decide to try another route. Just as you step out of the front door,
        a thunderous roar sweeps through the town, shattering windows and setting
        off car alarms. You might as well go back inside and get comfortable.
        ''')
        game['dead'] = 'Grounded by indecisiveness.'

def checkpoint():
    global loc
    if effects['Reckless'] in player.effects:
        c = opt('''You drive towards the checkpoint...''',
                choices=['Slow to a stop at the guard post','[Reckless] Ram the booth'])
        if c == 2:
            saprint('''Your foot gets heavy. Your heart starts racing. You steer toward the security kiosk...''')
            pause('Hang on!!')
            saprint('The checkpoint lays in ruin. You\'re through. Better get moving.')
            loc = 'entrance'
            return None

    c = opt('''
    You pull into the security checkpoint. A sentry stares intently.
    
    "Badge, please".
    ''',
            [
                'I don\'t have a badge.',
                '[Password] I need a contingency pass. "Esperanto".',
                '[Money] Of course, here you go (present fistful of cash)',
                '[Empathetic] Sir, your reflection on this moment will stay with you forever.',
                '[Tazer] (Lunge forward)',
                '[Dog] Sic \'em!',
                '[Physical] (Attempt to overpower guard)',
                '[Lye] (Throw at guard)'
            ],
            possible=[
                True,
                effects['Password'] in player.effects,
                items['Money'] in player.inventory.items,
                effects['Empathetic'] in player.effects and not 'empathize_with_guard' in props,
                items['Tazer'] in player.inventory.items,
                items['Dog'] in player.inventory.items,
                effects['Physical'] in player.effects,
                items['Lye'] in player.inventory.items
            ]
            )
    if c == 1:
        saprint('Then clear out of here!')
        pause()
        loc = 'home'
    if c == 2:
        saprint('"Esper... oh, right, right. One minute."\n\nThe guard waves you through.')
        pause()
        loc = 'entrance'
    if c == 3:
        saprint('"You can\'t just! .. It\'s a national crisis don\'t you! ... "\n\nThe guard takes the money and waves you through.')
        pause()
        loc = 'entrance'
    if c == 4:
        saprint('"I\'m very sorry, but... well, it\'s just that... I mean,')
        roll = statroll('intellect')
        if roll >= 3:
            saprint('"This never happened, do you understand?"\n\nThe guard waves you through.')
            pause()
            loc = 'entrance'
        else:
            saprint("You're not authorized!! Leave immediately!")
            props.append('empathize_with_guard')
            pause()
            loc = 'home'
    if c == 5:
        saprint('You leap forward to jolt the guard!')
        roll = statroll('speed')
        if roll >= 4:
            saprint('"Whoa, hold o-o-h-oh-oh-ohoh-aaaa-aaaahhhhhh!"\n\nThe guard drops to the floor, twitching. Sorry, guy.')
            loc = 'entrance'
            pause()
        else:
            saprint('"AHH GET BACK! GET ..."\n\nYou are put down by a barrage of anti-personnel rounds.')
            game['dead'] = 'Swiss cheese\'d'
    if c == 6:
        saprint('"Hey, please keep your dog ... Argh!!"\n\nThe guard is vulnerable to an attack!')
        roll = statroll('strength')
        if roll >= 4:
            saprint('You knock the guard out cold and continue forth.')
            loc = 'entrance'
            pause()
        else:
            saprint('"AHH GET BACK! GET ..."\n\nYou and your dog are put down by a barrage of anti-personnel rounds.')
            game['dead'] = 'Put down like a dog.'
    if c == 7:
        saprint('"HEY! Get... OFF of me!"\n\nYou struggle with the guard!')
        roll = statroll('strength')
        if roll >= 5:
            saprint('You knock the guard out cold and continue forth.')
            pause()
            loc = 'entrance'
        else:
            saprint('"AHH GET BACK! GET ..."\n\nYou are perforated by a barrage of anti-personnel rounds.')
            game['dead'] = 'Swiss cheese\'d'
    if c == 8:
        saprint('''You hurl the caustic powder at the guard\n\n"URGH! What! ARGHAAA"\n\nNow is your chance!''')
        roll = statroll('speed')
        if roll >= 3:
            saprint('Bullets whiz by your feet as you bolt towards the nearest door. You make your way into the facility.')
            pause()
            loc = 'entrance'
        else:
            saprint('"AHH YOU SON OF A! ..."\n\nOne of the bullets fired pierces your calf. You stumble ')
            game['dead'] = 'Branded a terrorist.'


def fence():
    global props
    global loc
    c = opt('''
    You arrive at the perimeter. It's quiet. A 16-foot steel mesh fence looms between you and the outskirt of the blast zone.
    ''',
        [
            'Go back.',
            '[Grizzled] Scale the fence.',
            '[Tenacity + Speed] Search the woods.',
            '[Luck] Walk for a bit.',
            '[Spiked Boots] Scale the fence.',
            'Go to the second entrance.'
        ],
        [
            True,
            effects['Grizzled'] in player.effects,
            player.stats.speed + player.stats.tenacity >= 7,
            'walked_the_fence' not in props,
            items['Spiked Boots'] in player.inventory.items,
            'discovered_2nd_entrance' in props
        ]
        )
    if c == 1:
        loc = 'home'
    if c == 2:
        saprint('''
        "Urgh, this should be fun."
        
        You crawl up the steel mesh. Your fingers hurt like hell, but you've been through much worse.
        ''')
        pause()
        loc = 'entrance'
    if c == 3:
        saprint('You clamor through the woods surrounding the facility, guided by instinct.')
        loc = 'shed'
        pause()
    if c == 4:
        roll = statroll('random')
        props.append('walked_the_fence')
        if roll > .9:
            saprint('You stumble upon a gaping hole in the fence. You must not have been the first person to try this!')
            pause()
            loc = 'entrance'
        elif roll > .5:
            props.append('discovered_2nd_entrance')
            saprint('You stumble upon a clearing... it looks like a second entrance.')
            loc = 'fence2'
            pause()
        else:
            saprint('Unfortunately, you find no weakpoints in the fence.')
            pause()
    if c == 5:
        saprint('''They're not pretty but the spiked boots you rigged together from old motorcycle parts interlock with the mesh fence and make climbing it much easier.''')
        pause()
        loc = 'entrance'
    if c == 6:
        loc = 'fence2'

def fence2():
    global loc
    global props
    c = opt('''There is no guard posted. Instead a wide steel gate looms before you, alongside an accompanying control panel.
                ''',
            [
                'Enter random digits.',
                '[Resourceful] Short circuit the control panel',
                '[Technical + Laptop] Access motor procedures',
                'Go back.'
            ],
            [
                'desperate_digits' not in props,
                effects['Resourceful'] in player.effects and 'pry_control_panel' not in props,
                effects['Technical'] in player.effects and items['Laptop'] in player.inventory.items,
                True
            ]
            )
    if c == 1:
        props.append('desperate_digits')
        roll = statroll('random')
        if roll >= .95:
            saprint('''...*whir, whir*... *bing!*

                            What? It, it worked?

                            ...WHAT.
                            ''')
            pause()
            loc = 'entrance'
        else:
            saprint('''...*gz gz gz*...

                            Yeah, typing random numbers didn't work.
                            ''')
            pause()
    if c == 2:
        saprint('You pry on the control panel housing with all your strength.')
        props.append('pry_control_panel')
        roll = statroll('strength')
        if roll >= 5:
            saprint('After a few failed attempts (and singed fingertips) you manage to freak out the gate\'s circuitry. It creeps open just wide enough to slip by.')
            pause()
            loc = 'entrance'
        else:
            saprint('Argh! There\'s just no way you are going to snap off the case.')
            pause()
            loc = 'fence2'
    if c == 3:
        saprint('What a lucky break! You connect to the device and toggle the gate status to OPEN')
        pause()
        loc = 'entrance'
    if c == 4:
        loc = 'fence'

def shed():
    global loc
    c = opt('''You come across an abandoned shed. It doesn't look like it's part of the facility. You peer inside.
    
    There is an assortment of rusted tools and a broken down motorcycle.
    ''',
    [
        'Go back to the fence.',
        '[Biological] You spot a bag of lye in the corner. Pick it up.',
        '[Resourceful] Jury rig spiked boots.',
        '[Reckless + Tazer] light the shed on fire.'
    ],
        [
            True,
            effects['Biological'] in player.effects and items['Lye'] not in player.inventory.items,
            effects['Resourceful'] in player.effects and items['Spiked Boots'] not in player.inventory.items,
            effects['Reckless'] in player.effects and items['Tazer'] in player.inventory.items
        ]

        )
    if c == 1:
        loc = 'fence'
    if c == 2:
        saprint('< You grab the caustic bag of lye. >')
        pause()
        player.inventory.add(items['Lye'])
    if c == 3:
        saprint('< You craft a set of spiked boots. >')
        pause()
        player.inventory.add(items['Spiked Boots'])
    if c == 4:
        saprint('You stoke the cinders until a roaring blaze billows over the top of the treeline!\n\nYou watch the guard post and slip by when the sentry inevitably run towards the fire.')
        pause()
        loc = 'entrance'

def entrance():
    global loc
    saprint('Nice job! You made it to the entrance!')
    game['dead'] = 'you made it to entrance'

locs = {
    'home':home,  # baseline
    'couch':couch,  # dangerously clouse to staying on earth
    'earth':earth,  # chose to stay on earth
    'grounded':grounded,  # waited too long
    'checkpoint':checkpoint,  # front door
    'fence':fence,  # sneaky
    'shed':shed,  # fence tools
    'fence2':fence2,  # luck 2nd discovery
    'entrance':entrance  # get in
}

while (game['dead'] == False) and (game['next'] == 'e002_infiltration'):
    locs[loc]()

# Knock out
if effects['Password'] in player.effects:
    player.effects.remove(effects['Password'])
if items['Spiked Boots'] in player.inventory.items:
    player.inventory.remove(items['Spiked Boots'])
if items['Lye'] in player.inventory.items:
    player.inventory.remove(items['Lye'])