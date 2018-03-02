from Util.Resources import *

print("This is a test scenario")

c = opt("Append '>' to player name?",['Yes','No'])

if c==1:
    player.name = player.name+'>'
elif c==2:
    game['dead'] = True

game['next'] = 'e999_test'