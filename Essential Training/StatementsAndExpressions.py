words = ['zac', 'vas', 'chi']
count = 0
while (count < 3):
    print(" print words with while loop" , words[count])
    count += 1
a, b = 0, 1
while (b < 1000):
    print(b, end=' ', flush=True)
    a, b = b, a + b
print()



for i in words: # for each elements of words the value i will be assigned to those elements
    print ("printing loop with ''for'' loop", i)
