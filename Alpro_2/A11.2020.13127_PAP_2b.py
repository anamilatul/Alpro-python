#Program menentukan bilangan terkecil dari inputan 3bilangan
#Kasus2

def min2(bilA,bilB) :
    if bilA < bilB :
        return bilA
    else :
        return bilB

def min3(bilA,bilB,bilC) :
    nini = min2(bilA,bilB)
    if nini < bilC :
        if nini == bilA :
            print("Bilangan terkecil adalah bilangan A yaitu",bilA)
        else :
            print("Bilangan terkecil adalah bilangan B yaitu",bilB)
    else :
        print("Bilangan terkecil adalah bilangan C yaitu",bilC)

def main() :
    bilA = int(input("Masukkan bilangan A : "))
    bilB = int(input("Masukkan bilangan B : "))
    bilC = int(input("Masukkan bilangan C : "))
    min3(bilA,bilB,bilC)

if __name__ == "__main__" :
    main()