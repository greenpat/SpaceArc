import Obj
from Text import *
from Classes import *

clrscr()
line()
print('''
   ___                    __              
  / _ \___ ___  ___ _____/ /___ _________ 
 / // / -_) _ \/ _ `/ __/ __/ // / __/ -_)
/____/\__/ .__/\_,_/_/  \__/\_,_/_/  \__/ 
        /_/                               

''')
saprint('''
Amidst the panic and confusion you silently resolve to yourself -- you are leaving this planet.

The airwaves buzz with pundits and guest experts suggesting how to manage the crisis, but you are not receptive to their advice.

It is very possible that Earth will be spared a catastrophic impact or cooling event.
It is also very possible that all life will be extinguished within days.

Luckily for you, your community was chosen as an Ark build site several years ago. The massive vessel has been decades in the making, and employed a full third of your community.

Let's get going!
''', wipe = False)
pause()
c1 = opt('You swipe your keys and passport from the bureau.\n\nAs you flip through the pages, your eyes meet your own portrait. You see...',
        ['a young','a grown','an old'], suppress_display=True, return_text=True)

if c1 == 'a young':
    Obj.player.base_stats.add(Stats(speed = 2, tenacity = -1))
elif c1 == 'a grown':
    Obj.player.base_stats.add(Stats(strength = 2, speed = -1))
elif c1 == 'an old':
    Obj.player.base_stats.add(Stats(tenacity = 2, strength = -1))

# traits that can impact available choices
c2 = opt(c1+',\n',
         [
             'spirited',
             'reckless',
             'grizzled',
             'resourceful',
             'empathetic',
             'heroic'
         ], suppress_display=True, return_text=True, wipe=False)

if c2 == 'spirited':
    Obj.player.effects.append(Obj.effects['Spirited'])
if c2 == 'reckless':
    Obj.player.effects.append(Obj.effects['Reckless'])
if c2 == 'grizzled':
    Obj.player.effects.append(Obj.effects['Grizzled'])
if c2 == 'resourceful':
    Obj.player.effects.append(Obj.effects['Resourceful'])
if c2 == 'empathetic':
    Obj.player.effects.append(Obj.effects['Empathetic'])
if c2 == 'heroic':
    Obj.player.effects.append(Obj.effects['Heroic'])

# competencies that can impact available choices
# social, biological, technical, physical

c3 = opt(c1+', '+c2+'...\n',
         [
             'augmented reality entertainer', # social
             'hydroponic farmer', #biological
             'graph database developer', # technical
             'bioplastic athlete', #physical
             'cybercivics professor', #social
             'nanosurgical clinician', # biological
             'solar array technician', # technical
             'autonomous drone mechanic' # physical
         ],
         suppress_display=True, return_text=True, wipe=False
         )

clrscr()
line()
print('')
print("That's right... you're "+c1+", "+c2+", "+c3+"!\n")
if c3 == 'augmented reality entertainer':
    Obj.player.effects.append(Obj.effects['Social'])
    saprint('''
    Over two hundred years ago people first started designing machine interfaces for the explicit purpose of entertainment. Color, then sound, then depth perspective, then motion detection, then spatial awareness were added to play consoles.
    
    You always had a knack for crafting a thrill for your users.
    
    Every now and again you also enjoy a good book.
    ''', wipe=False, topline=False)
elif c3 == 'hydroponic farmer':
    Obj.player.effects.append(Obj.effects['Biological'])
    saprint('''
    After 8 years of soil chemistry, plant genetics, and aquifer logistics you finally earned your place at one of the elite agricultural conglomerates.
    
    Hey it\s not easy to produce 185 bushels of soy per acre-equivalent, but it pays well.
    ''', wipe=False, topline=False)

elif c3 == 'graph database developer':
    Obj.player.effects.append(Obj.effects['Technical'])
    saprint('''
    The irony of information storage is that people who generate and use data often don't
    understand what their minds are doing at that moment.
    
    You do. And there is a LOT of data architecture to clean up and traverse.
    
    You just wish you had friends.
    ''', wipe=False, topline=False)
elif c3 == 'bioplastic athlete':
    Obj.player.effects.append(Obj.effects['Physical'])
    saprint('''
    There are no men and women divisions in sports anymore, only the purist
    leagues and the bioplastics.
    
    When you can 3D print a "tendon" into gloves that contracts in the presence of
    pressure, competitive climbing gets a whole lot murkier. Sometimes it just
    seems like one long debate about what defines a "battery" or "leverage" or "skin".
    
    At least you never stooped to doping. Those guys are cheaters.
    ''', wipe=False, topline=False)
elif c3 == 'cybercivics professor':
    Obj.player.effects.append(Obj.effects['Social'])
    saprint('''
    When your civic duty (d)evolves into web questionnaires and e-Tax filing, cybersecurity
    becomes a patriotic topic.
    
    Nothing has yet been invented to let students sleep through class undetected.
    ''', wipe=False, topline=False)
elif c3 == 'nanosurgical clinician':
    Obj.player.effects.append(Obj.effects['Biological'])
    saprint('''
    Miniaturized medical robots sometimes trigger Anaphylaxis or lesser immune system disorders,
    so they are often administered with anti-inflammatory treatments.
    
    A famous modern artist recently trained a surgical AI to invent knock-knock jokes and tell
    them using sign language.
    
    He was not sued on the condition that the codebase was permanently deleted.
    ''', wipe=False, topline=False)
elif c3 == 'solar array technician':
    Obj.player.effects.append(Obj.effects['Technical'])
    saprint('''
    You often wonder if a Dyson Sphere will ever be attempted. Let alone that, you
    wonder if even a Kardashev Type I civilization exists in the universe.
    
    You have a lot of time to wonder, because maintaining a vast arsenal of solar
    panels requires a lot of travel.
    ''', wipe=False, topline=False)
elif c3 == 'autonomous drone mechanic':
    Obj.player.effects.append(Obj.effects['Physical'])
    saprint('''
    You inherited a mid-size chop shop which specializes in drone repair. Most of the
    work is related to fizzled camera feeds or blown hydraulics. It's honest work.
    
    The strangest thing you've seen was the time when a customer requested an upgrade
    to the rotor strength of their "personal assistant" bot. It became apparent that
    the bot was a.. very.. personal assistant. Business was good enough to decline that job.
    ''', wipe=False, topline=False)

print("\nAnd your name is...\n")
Obj.player.name = input('(Type your name):')

c = opt('"Almost forgot! I can\'t leave without my..."\n',
        [
            'Laptop',
            'Dog',
            'Tazer',
            'Scripture',
            'Money'
        ], wipe = True
        )

clrscr()

if c == 1:
    Obj.player.items.append(Obj.items['Laptop'])
    Obj.player.base_stats.add(Stats(intellect = 1))
    print("You grab your laptop, obviously.")
    print("\n< +1 to Intellect >")
elif c == 2:
    Obj.player.items.append(Obj.items['Dog'])
    Obj.player.base_stats.add(Stats(speed = 1))
    print("You let out a sharp whistle, and your canine companion clamors to your side.")
    print("\n< +1 to Speed >")
elif c == 3:
    Obj.player.items.append(Obj.items['Tazer'])
    Obj.player.base_stats.add(Stats(strength = 1))
    print("You hope never to have to use your tazer... again... sort of.")
    print("\n< +1 to Strength >")
elif c == 4:
    Obj.player.items.append(Obj.items['Scripture'])
    Obj.player.base_stats.add(Stats(tenacity = 1))
    print("There has never been a more critical time for faith. You grab the tome.")
    print("\n< +1 to Tenacity >")
elif c == 5:
    Obj.player.items.append(Obj.items['Money'])
    print('"Heh heh" ... You stash away your vast accumulation of wealth.')
Obj.player.display()
pause()

Obj.game['next'] = 'e002_infiltration'
Obj.game['turns'] -= 1  # This chapter doesn't count