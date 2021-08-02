import pustaka

def main() :
    bil1 = int(input("Masukkan bilangan pertama : "))
    bil2 = int(input("Masukkan bilangan kedua : "))
    pustaka.jumlah(bil1,bil2)
    pustaka.kurang(bil1,bil2)
    pustaka.kali(bil1,bil2)
    pustaka.bagi(bil1,bil2)

if __name__ == "__main__" :
    main()