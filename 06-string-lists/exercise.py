user_string = input('Enter the string to find whether it\'s a palindrome or not: ')

## This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.
if user_string == user_string[::-1]:
    print(user_string,'is a palindrome')
else:
    print(user_string,'is not a palindrome')
    
