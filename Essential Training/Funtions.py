'''
def control(n):
    if n <=1: # control if n is less or equal than 1
        return False
    for i in range(2,n):# start the range from 2 b'cause 2 is a prime nr
        if n % i==0: # check if the rest of the division is =0.  in case the rest of the divison is 0 return false
            return False
    else:
            return True

def getPrimeNumbers():
    for x in range(2000): # I see in the range of nrs from 0-100 which are prime, at this point n=100
        if control(x):
            print(x, end=' ', flush=True)
getPrimeNumbers()
'''



