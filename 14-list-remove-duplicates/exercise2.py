def for_loop(old_elements):
    
    new_elements = []

    for n in old_elements:
        if n not in new_elements:
            new_elements.append(n)
    return new_elements

def using_set(old_elements):
    return list(set(old_elements))

old_elements =[]

num = int(input('How many elements u want in your list? '))

for i in range(num):
        element = input('Enter elements: ')
        old_elements.append(element)

print('Using for loop:',for_loop(old_elements))
print('Using set:',using_set(old_elements))


            
