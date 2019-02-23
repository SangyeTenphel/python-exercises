def fibonnaci(num):
    a, b = 0, 1
        
    for i in range(num):
        print(a)
        a, b = b, a + b
        

num = int(input('How many Fibonnaci numbers to generate? '))
fibonnaci(num)

        
