def take_list():
    num = int(input('How many lists do you want? '))
    old_elements =[]
    for i in range(num):
        n = input('Enter elements: ')
        old_elements.append(n)

    return list(set(old_elements))

new_list = take_list()
print(new_list)
