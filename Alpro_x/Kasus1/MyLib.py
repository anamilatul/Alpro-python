#Program MyLib
import random

def tambah(a,b) :
    #
    return a + b

def kurang(a,b) :
    return a - b

def kali(a,b) :
    return a * b

def bagiInt(a,b) :
    return a // b

def bagiFloat(a,b) :
    return a / b

def isiListRandom(A,n) :
    for i in range (n) :
        A[i] = random.randint(0,100)

def cetakList(A,n) :
    for i in range(n) :
        print(A[i], end=" ")
    print()

def lenghtList(A) :
    i = 0
    for i in A :
        i = i + 1 #atau i +=1
    return i

def sumList(A,n) :
    sum = 0
    for i in range(n) :
        sum = sum +A[i]
    return sum

def averageList(A,n) :
    return sumList(A,n) / n

def maxList(A,n) :
    max = A[0]
    for i in range(1,n) :
        if A[i] > max :
            max = A[i]
    return max

def minList(A,n) :
    min = A[0]
    for i in range(1,n) :
        if A[i] < min :
            min = A[i]
    return min
