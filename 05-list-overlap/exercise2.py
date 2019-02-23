import random

## generating a random list
a = [random.randint(0,100) for n in range(10)]
b = [random.randint(0,100) for n in range(11)]

## using single line of code
c = set([numbers for numbers in b if numbers in a])

print('First random list:',a)
print('Second random list:',b)
print('Common elements between the above two lists:',c)
