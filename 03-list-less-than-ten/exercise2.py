a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = [num for num in a if num < 5]
print('numbers less than 5:',new_list)
user_num = int(input('Enter a number: '))
user_list = [num for num in a if num < user_num]
print('numbers less than your number:',user_list)
