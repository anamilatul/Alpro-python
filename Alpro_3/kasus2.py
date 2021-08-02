#prosedur untuk menentukan bil terkecil antara bilangan A,B dan C
#kasus 2
def min2(bilA,bilB):
    if bilA < bilB:
        hasil = bilA
    elif bilA > bilB:
        hasil = bilB
    else:
        hasil = bilA
        print("a dan b merupakan bilangan yang sama yaitu ")
    return hasil

def min3(bilA, bilB, bilC):
    return min2(min2(bilA,bilB),bilC)

bilA = int(input("Masukkan bilangan A : "))
bilB = int(input("Masukkan bilangan B : "))
bilC = int(input("Masukkan bilangan C : "))
result = min3(bilA,bilB,bilC)
print(result)