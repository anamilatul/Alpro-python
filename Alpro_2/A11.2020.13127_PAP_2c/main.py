import pustaka

def main() :
    bil1 = int(input("Masukkan bilangan pertama : "))
    bil2 = int(input("Masukkan bilangan kedua : "))
    print("Hasil penjumlahan kedua bilangan :", pustaka.jumlah(bil1,bil2))
    print("Hasil selisih kedua bilangan :", pustaka.kurang(bil1,bil2))
    print("Hasil kali kedua bilangan :", pustaka.kali(bil1,bil2))
    print("Hasil bagi kedua bilangan :", pustaka.bagi(bil1,bil2))

if __name__ == "__main__" :
    main()