import time
import re

# 'space arc print' custom meant to neatly display text
# from a docstring 80 characters wide
def saprint(docstring = '', wipe = True, topline = True):
    if(wipe):
        clrscr()
    if(topline):
        line()
    docstring = re.sub('[ \\t]+',' ', docstring)  # get rid of padding
    docstring = re.sub('^\\s+|\\s+$','',docstring)
    docstring = re.sub('\n[ \\t]+|[ \\t]+\n','\n', docstring)  # get rid of SOL spaces
    docstring = re.sub('(?<!\\n)\n(?!\\n)',' ', docstring)  # get rid of single newlines
    docstring = docstring.split('\n')
    print('')
    for i in range(0, len(docstring)):
        words_to_print = docstring[i].split(' ')
        if words_to_print[0] == '':
            print('')
            continue
        line_length = 0
        while len(words_to_print)>0:
            if len(words_to_print[0])+line_length+1 > 80:
                print('')
                line_length = 0
            line_length += (len(words_to_print[0])+1)
            print(words_to_print.pop(0), end=' ', flush=True)

def clrscr():
    print('\n'*100)

def line():
    print('-'*80)

def pause(prompt:str = '(Press enter)'):
    print('')
    input(prompt)

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
