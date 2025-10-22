import random
import time
import sys

print('=' * 30)
print('Guess The Number')
print('=' * 30)

Guess_Number = random.randint(1, 10)

# animation
chars = "|/-\\"
for i in range(20):  
    sys.stdout.write('\rComputer Is Thinking... ' + chars[i % len(chars)])
    sys.stdout.flush()
    time.sleep(0.1)

print('')
print('=' * 30)
try:
    Player_Guess = int(input('Computer Already Pick The Number\n' \
    'Guess The Number From 1 To 10: '))
except:
    print('=' * 30)
    Player_Guess = int(input('Wrong Input\n' \
    'Pick Number From 1 To 10: '))

if Player_Guess > Guess_Number:
    print('=' * 30)
    print('Too High')

elif Player_Guess < Guess_Number:
    print('=' * 30)
    print('Too Low')
    
while Player_Guess != Guess_Number:
    try:
        print('=' * 30)
        Player_Guess = int(input('You Were Wrong\n' \
        'Guess Again: '))
    
    except ValueError:
        print('=' * 30)
        Player_Guess = int(input('Wrong Input\n' \
        'Pick Number From 1 To 10: '))
    
    if Player_Guess > Guess_Number:
        print('=' * 30)
        print('Too High')
    elif Player_Guess < Guess_Number:
        print('=' * 30)
        print('Too Low')
        
print('=' * 30)
print('Yay! You Guessed The Number')
input('Press Enter To Exit')
