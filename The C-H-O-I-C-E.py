from time import *
from random import randint
def type(char):
    a = 0
    for i in range (char):
        print(phrase[a], end='')
        sleep(0.05)
        a+=1
def speak(char):
    a = 0
    for i in range (char):
        sleep(0.07)
        a = a+1
stamina = 100
print('Booting', end='')
phrase = '.'
for i in range (11):
    print(phrase[0], end='')
    sleep(0.05)
print('.')
print('WELCOME')
sleep(0.5)
print('Gathering files: [', end='')
phrase= '|'
for i in range (10):
    print(phrase[0], end='')
    sleep(0.05)
print(']')
print('DONE')
sleep(0.5)
print('Applying Fonts : [', end='')
phrase= '|'
for i in range (10):
    print(phrase[0], end='')
    sleep(0.05)
print(']')
print('DONE')
sleep(0.1)
print('Finalizing     : [', end='')
phrase= '|'
for i in range (10):
    print(phrase[0], end='')
    sleep(0.05)
print(']')
print('DONE')
print('----------------------------------------------------')
sleep(0.5)
phrase = 'Welcome to the C-H-O-I-C-E'
type(26)
sleep(0.5)
print('')
phrase = 'A text-based RPG where YOU decide what happens. '
type(48)
sleep(0.5)
#holy crap this looks so much cleaner than before.
phrase = 'Your first choice is approaching, but first there is something you need to know. '
type(81)
print('')#This is for a new line
sleep(0.5)
phrase = 'There is one thing you need to keep an eye on throuought the game: '
new_varnew_var = type(67)

print('')
phrase = '''Stamina.
    Stamina represents how your character's feeling and how motivated they are. Stamina is represented in percentage ('%') - 100% is high stamina, 0% is no stamina. Stamina can go above 100%. Your character start out with 100% stamina at the start of each game. The less stamina they have, the less energy there going to have to do things with. Each choice you make will cost some stamina, so be wise but don't sacrifice too much. There will always be a task with low stamina needs if stamina is low. '''

type(508)
sleep(0.5)
print('')
print('-----')
phrase = 'You have three options:'
type(23)
sleep(0.5)
print('')
phrase = '1. The Mountains [-0%]'
type(22)
sleep(0.5)
print('')
phrase = '2. The Woodland [-0%]'
type(21)
sleep(0.5)
print('')
phrase = '3. The Beach [-0%]'
type(18)
sleep(0.5)
print('')
phrase ='Please type 1, 2 or 3 correspondent to the options.'
type(51)
sleep(0.5)
location = input(' ')
location = location.upper()
#[*_THIS IS WHERE THE RPG STARTS_*]
if location == '1':
    print('----------------------------------------------------')
    sleep(0.5)
    print('WELCOME TO')
    sleep(0.5)
    phrase = 'The Mountains'
    type(13)
    sleep(0.5)
    print('')
    phrase='In front of you there is a mountain. But not just any mountain, this mountain is HUGE. Your task is to climb up it. You are equipped with a map, a spyglass, a compass, some water, some food and a sleeping bag.'
    type(209)
elif location == '2':
    print('----------------------------------------------------')
    sleep(0.5)
    print('WELCOME TO')
    sleep(0.5)
    phrase = 'The Woodland'
    type(12)
    sleep(0.5)
    print('')
    phrase = 'You are wandering through a dark forest. '
    type(41)
    sleep(0.5)
    phrase = 'The air is dank and light is sparse. '
    type(37)
    sleep(0.5)
    phrase = 'There are 2 paths. One is narrow and dark ([-0%]). '
    type(49)
    sleep(0.5)
    phrase = 'The other wide and clear. ([-0%]) '
    type(32)
    sleep(0.5)
    print(' ')
    phrase = 'Which path is the one you choose to start your journey?'
    type(55)
    sleep(0.5)
    print('')
    phrase = 'Please type 1 or 2 correspondent to the option you want:'
    type(56)
    sleep(0.1)
    location = input(' ')
    if location == '1':
        phrase = 'You chose the narrow and dark path. '
        type(36)
        sleep(0.5)
        phrase = 'The darkness shadows over you. '
        type(31)
        sleep(2)
        phrase = 'There is a soft rustle in the bushes. '
        type(38)
        sleep(0.5)
        phrase = 'You pause and hold your breath. '
        type(32)
        sleep(1)
        phrase = 'Silence fills the air, yet you can feel someone, or somethings presence. '
        type(73)
        sleep(1)
        phrase = 'Another rustle. '
        type(16)
        sleep(1)
        phrase = 'Something finally makes its way out of the bushes. '
        type(51)
        sleep(0.5)
        phrase = 'It speaks to you. '
        type(18)
        sleep(0.5)
        print('')
        phrase = 'Hello? '
        speak(7)
        phrase='''Will you:
        1) Run away [-15%]
        2) Talk back [-3%]'''
        type(61)
        phrase = 'Please type 1 or 2 correspondent to the option you want:'
        type(56)
        sleep(0.1)
        location = input(' ')
        if location == '1':
            #Code for ran away
            print('Location = 1')
        elif location == '2':
            print('Location = 2')
    elif location == '2':
            phrase = 'You chose the wide path. It seems welcoming. '
            type(45)
            sleep(0.5)
            phrase = 'A bug scuttles across the path. '
            type(32)
            sleep(0.5)
            phrase = 'You continue walking. '
            type(22)
            sleep(0.5)
            phrase = 'Another bug crosses your path. Closer to you this time. '
            type(56)
            sleep(0.5)
            phrase = 'This time, about 5 start to wander across the path. '
            type(52)
            print('')
            print('-----')
            phrase = 'Do you: '
            type(8)
            print('')
            phrase = '1. Try to kill the bugs as they go past. [-10%]'
            type(47)
            print('')
            sleep(0.5)
            phrase = '2. Ignore the bugs. [-1%]'
            type(26)
            print('')
            sleep(0.5)
            phrase = '3. Walk faster, and try to get away. [-5%]'
            type(43)
            sleep(0.5)
            print('')
            print('-----')
            location = input('')
            if location == '1':
                stamina = stamina-10
                print('STAMINA =', stamina)
                sleep(0.5)
                phrase = 'You have fun trying to squash the bugs, it makes you feel happy.'
                type(64)
                print('')
                print('[STAMINA +10%]')
                stamina == stamina + 10
                sleep(0.5)
                phrase = 'But soon floods of bugs are overcrowding the path. '
                type(51)
                sleep(0.5)
                phrase = 'You try to step away from the giant sea but you lose your balance as the bugs push and pull at your feet. '
                type(106)
                sleep(1)
                phrase = 'You fall into the layer of bugs. '
                type(33)
                sleep(0.5)
                phrase = 'They crawl across every inch of your body, finding there way through the maze of cloth. '
                type(88)
                sleep(0.5)
                print('')
                print('-----')
                phrase = 'What do you do: '
                type(16)
                sleep(0.5)
                phrase = '1. Try to wriggle free of the bugs grasp. '
                type(42)
                phrase = '2. Accept your fate. '
                type(21)
                phrase = '3. Try to find something to help you in your pockets. '
                type(54)
                sleep(0.5)
                print('')
                print('-----')
            elif location == '2':
                stamina = stamina-1
                print('STAMINA=', stamina)
                sleep(0.5)
                phrase = 'You ignore the bugs and carry on walking. '
                type(42)
                sleep(0.5)
                phrase = 'You hear many more bugs scuttle behind you. '
                type(44)
                sleep(0.5)
                phrase = 'The scuttling increases further, like static following behind you. '
                type(67)
                sleep(0.5)
                phrase = 'You pick up the pace, slightly disturbed by the amount of scuttling going on out of your vision. '
                type(97)
                sleep(0.5)
                phrase = 'You speed up into a brisk jog, then a run. '
                type(43)
                sleep(0.5)
                phrase = 'It sounds like the bugs are getting closer - it feels like it. '
                type(63)
            else:
               print('')
               print('Unknown input. Aborting.')
               exit
    elif location == '2':
        stamina = stamina-5
        print('STAMINA=', stamina)
        sleep(0.5)
        phrase = 'You speed up into a brisk walk, to try not to get bitten. '
        type(58)
    else:
        print('')
        print('Unknown input. Aborting.')
        exit
elif location == '3':
    print('----------------------------------------------------')
    sleep(0.5)
    print('WELCOME TO')
    sleep(0.5)
    phrase = 'The Beach'
    type(9)
    sleep(0.5)
else:
    print('')
print('Unknown input. Aborting.')
exit
