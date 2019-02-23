def reverse_string(w):
## split() into individual words
## [::-1] get each word starting from last step
## ' '.join() return a string seperated by ' ' i.e a space
    return ' '.join(w.split()[::-1])

sentence = input('Write a sentence: ')
print(reverse_string(sentence))
