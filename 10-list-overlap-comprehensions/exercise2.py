from random import randint
rand_range = randint(10,15)

a = []
b = []

for i in range(rand_range):
    a.append(randint(1,100))

for i in range(rand_range):
    b.append(randint(1,100))

print('First randomly generated list:',a)
print('Second randomly generated list',b)

common_element = [n for n in set(a) if n in b]
print('Common elements between them:',common_element)
