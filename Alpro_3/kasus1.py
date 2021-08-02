#program prosedur untuk menentukan bil. terkecil antara bil a bil b
#kasus1
def min2(bilA,bilB):
    if bilA < bilB:
        hasil = bilA
    elif bilA > bilB:
        hasil = bilB
    else:
        hasil = bilA
        print("a dan b merupakan bilangan yang sama yaitu ")
    print(hasil)

bilA = int(input("Masukkan bilangan A : "))
bilB = int(input("Masukkan bilangan B : "))
min2(bilA,bilB)
