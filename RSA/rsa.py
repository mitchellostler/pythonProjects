from random import random
import math, sys

primeArr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

#TODO: once program is complete upgrade to 1024 bit primes
def prime_select(primeArr):
    index1 = random(len(primeArr))
    index2 = random(len(primeArr))
    while index1 == index2:
        index2 = random(len(primeArr))
    return [primeArr[index1], primeArr[index2]]

def coprime_tester(value1, value2):
    while value1 != 0 and value2 != 0:
        if value1 > value2:
            value1 %= value2
        else:
            value2 %= value1

    return max(value1, value2) == 1

def public_key_finder(pqArr):
    global phi
    phi = (pqArr[0] - 1)*(pqArr[1] - 1)
    print(phi)
    pubKey = 3
    while coprime_tester(pubKey, phi) != True:
        pubKey += 1
    return pubKey

#implementation of Euclid's extended algorithm
def private_key_finder(publicKey, totient):
    prevPhi, currPhi = totient, publicKey
    prevDiv, currDiv  = totient, 1
    nextPhi, nextDiv = 0, 0
    flag = True
    while currPhi > 1:
        quotient = math.floor(prevPhi/currPhi)
        nextPhi = prevPhi % currPhi
        nextDiv = prevDiv - currDiv*quotient

        prevPhi, prevDiv = currPhi, currDiv
        currPhi, currDiv = nextPhi, nextDiv
        if currDiv < 0:
            currDiv += totient

    return currDiv


#implementation of rsa
promptArr = ['login','createuser','generate', 'encrypt', 'decrypt', 'exit']

print('WELCOME TO RSA ENCRYPTION PROGRAM\n')
cmdInput = ''
while cmdInput != 'exit':
    cmdInput = input('Enter a command:\n')
    if cmdInput not in promptArr:
        print('Invalid command')
        continue
    
    if 

pqArr = prime_select(primeArr)
