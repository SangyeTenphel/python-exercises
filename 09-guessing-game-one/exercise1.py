import random

random_number = random.randint(1,9)

guess = int(input('Enter a number: '))

if guess == random_number:
    print('You guessed right')
elif guess > random_number:
    print('You guessed too high')
else:
    print('You guessed too low')
print('Correct answer:',random_number)
    

