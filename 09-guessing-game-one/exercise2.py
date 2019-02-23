import random

random_number = random.randint(1,9)
guess = 0
count = 0

while guess!= random_number and guess!= 'exit':
    guess = input('Enter a number: ')

    if guess == 'exit':
        break
    
    guess = int(guess)
    count +=1
    
    if guess > random_number:
        print('You guessed to high')
    elif guess < random_number:
        print('You guessed too low')
    else:
        print('You got it!')
        print('It took you',count,'tries!')

    
