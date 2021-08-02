#Program menentukkan bilangan terkecil dengan input bilangan
#Kasus1

def nilaiTerkecil(bilA,bilB) :
    if bilA < bilB :
        print("Bilangan terkecil adalah bilangan A yaitu ",bilA)
    else :
        print("Bilangan terkecil adalah bilangan B yaitu ",bilB)

def main() :
    bilA = int(input("Masukkan bilangan A : "))
    bilB = int(input("Masukkan bilangan B : "))
    nilaiTerkecil(bilA,bilB)


if __name__ == "__main__" :
    main()