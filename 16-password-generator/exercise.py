import string
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase
special = string.punctuation
number = string.digits
everything = upper + lower + special + number

def pass_generator(n):
    password = random.sample(everything,n)
    password = ''.join(password)
    return password

def weak_pass(n):
    password = random.sample(upper+lower,n)
    password = ''.join(password)
    return password

choice = input('Do u want a strong or weak password?: ')
n = int(input('Enter the length of password u want: '))

if choice == 'strong':
    print('The password is',pass_generator(n))
elif choice == 'weak':
    print('The password is',weak_pass(n))
else:
    print('Enter only strong or weak as option!')
