from time import *
from random import randint
invent = []
choice = 0
def type(phrase, char):
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
type('Welcome to the C-H-O-I-C-E', 26)
sleep(0.5)
print('')
type('A text-based RPG where YOU decide what happens. ', 48)
sleep(0.5)
#holy crap this looks so much cleaner than before.
type('Your first choice is approaching, but first there is something you need to know. ', 81)
print('')#This is for a new line
sleep(0.5)
type('There is one thing you need to keep an eye on throughout the game: ', 67)
print('')
type('''Stamina.
    Stamina represents how you are feeling and how motivated you are. Stamina is represented in percentage ('%') - 100% is high stamina, 0% is no stamina. If stamina hits 0%, then the you die. Stamina can go above 100%. You start out with 100% stamina at the start of each game. The less stamina they have, the less energy there going to have to do things with. Each choice you make will cost some stamina, so be wise but don't sacrifice too much. There will always be a task with low stamina needs if stamina is low. ''', 525)
sleep(0.5)
print('')
print('-----')
type('You have three options:', 23)
sleep(0.5)
print('')
type('1. The Mountains [-0%]', 22)
sleep(0.5)
print('')
type('2. The Woodland [-0%]', 21)
sleep(0.5)
print('')
type('3. The Beach [-0%]', 18)
sleep(0.5)
print('')
type('Please type 1, 2 or 3 correspondent to the options.', 51)
sleep(0.5)
location = input(' ')
location = location.upper()
if location == '1':
    print('----------------------------------------------------')
    choice =+ 1
    print('WELCOME TO')
    type('The Mountains', 13)
    invent.clear()
    invent.append('Spyglass')
    invent.append('Map')
    invent.append('Water')
    for i in range (3):
        invent.append('Apple')
    type('There is a vast mountain.', )#INSERT CHAR NO.
