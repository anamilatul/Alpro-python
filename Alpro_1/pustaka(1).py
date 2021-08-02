#Kasus3
#berisi fungsi atau prosedur untuk mengolah bilangan integer

def luas_persegi(n) :
    return n * n

def fact(n) :
    if n == 0:
        return 1
    else :
        return n * fact(n-1)

def is_besar(n) :
    inBil = []
    mil = ""
    for j in range(1, n+1) :
        mil += str(j) + " "
        inBil.append(j)
    print(mil)
    return inBil[n-1]

def is_kecil(n) :
    inBil = []
    mil = ""
    for j in range (1, n+1) :
        mil += str(j) + " "
        inBil.append(j)
    print(mil)
    return inBil[0]

def is_ganjil(n) :
    if n % 2 != 0 :
        return True
    else :
        return False

def is_genap(n) :
    if n % 2 == 0 :
        return True
    else :
        return False

def ToPositive(n) :
    if n < 0 :
        n *= -1
    return n

def ToNegative(n) :
    if n > 0 :
        n *= -1
    return n

def sum_n(n) :
    jumlah = 0
    for j in range(1, n+1) :
        jumlah += j
    return jumlah

def avg_n(n) :
    return sum_n(n) / n