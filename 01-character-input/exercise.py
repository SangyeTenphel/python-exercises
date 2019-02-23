name = input('Enter your name: ')
age = input('Enter your age: ')
current_year = 2019
year = (current_year - int(age)) + 100
copies = input('How many times do u want to display the result: ')
for i in range(int(copies)):
    print(name,'will turn 100 yrs old in',year)
