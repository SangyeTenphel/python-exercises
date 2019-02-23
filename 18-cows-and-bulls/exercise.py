import random


def calculate_cows_and_bulls(org_list, guess_list):
    cow = 0
    bull = 0
    

    for i in range(len(org_list)):
        if guess_list[i] == org_list[i]:
            cow += 1
        elif guess_list[i] in org_list:
            bull += 1

    return cow, bull
    
    

if __name__ == '__main__':

    org_num = random.randrange(1000,9999)
    org_list = [int(d) for d in str(org_num)]
    print(org_list)

    guesses = 0
    cows = 0
    bulls = 0
    
    while cows < len(org_list):
        guess_num = input('Enter a guess between 0000 to 9999: ')
        guess_list = [int(d) for d in str(guess_num)]

        cows, bulls = calculate_cows_and_bulls(org_list, guess_list)
        print('You have',cows,'cows',',',bulls,'bulls')
        
        guesses +=1

    print('No. of guesses: ',guesses)
        

     
