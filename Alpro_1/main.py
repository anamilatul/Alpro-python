from pustaka(1) import *

def main() :
    n = int(input("Masukkan bilangan : "))
    print("luas persegi adalah :", str(luas_persegi(n)))
    print("factorial n :", str(fact(n)))
    print("bilangan terbesar adalah :", str(is_besar(n)))
    print("bilangan terkecil adalah :", str(is_kecil(n)))
    print("apakah n bilangan ganjil  :", str(is_ganjil(n)))
    print("apakah n bilangan genap  :", str(is_genap(n)))
    print("bilangan integer positif :", str(ToPositive(n)))
    print("bilangan integer negatif :", str(ToNegative(n)))
    print("jumlah bilangan n :", str(sum_n(n)))
    print("rata-rata n :", str(avg_n(n)))

if __name__ == "__main__" :
    main()