a = [5, 10, 15, 20, 25]
b = []

def new_list(a):
    return [a[0],a[-1]]

b = new_list(a)
print(b)
