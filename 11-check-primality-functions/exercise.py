def check_prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print(num,'is not a prime number')
                break
            else:
                print(num,'is a prime number')
                break
            
    ##    OR use the below code right under for            
    ##    else:
    ##       print(num,"is a prime number")
    ##
            
    else:
        print(num,'is not a prime number')

num = int(input('Enter a number: '))
check_prime(num)
