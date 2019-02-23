num = int(input('Enter number to find divisor of: '))
listRange = list(range(1,num+1))
divisors = []
for n in listRange:
    if num % n == 0:
        divisors.append(n)
        
print(divisors)
        
