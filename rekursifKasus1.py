#Program rekursif
#Kasus1

def jumlah(a,b):
    if b == 0 :
        hasil = a
    else :
        hasil = 1 + jumlah(a,(b-1))
    print(hasil)
    return hasil

def kurang(a,b):
    if b == 0:
        hasil = a
    else :
        hasil = -1 + kurang(a,(b-1))
    print(hasil)
    return hasil

def kali(a,b):
    if b == 1 :
        hasil = a
    else :
        hasil = a + kali(a,(b-1))
    print(hasil)
    return hasil

def pow(a,b):
    if b == 0 :
        hasil = 1
    else :
        hasil = a * pow(a,(b-1))
    print(hasil)
    return hasil

def fact(a):
    if a == 0:
        hasil = 1
    else :
        hasil = a*fact(a-1)
    print(hasil)
    return hasil

def main():
    a = int(input("Masukkan bilangan a : "))
    b = int(input("Masukkan bilangan b : "))
    print("Hasil penjumlahan a dan b :",jumlah(a,b),"\n")
    print("Hasil pengurangan a dan b :",kurang(a,b),"\n")
    print("Hasil perkalian a dan b :",kali(a,b),"\n")
    print("Hasil pemangkatan a dan b :",pow(a,b),"\n")
    print("Hasil faktorial a :",fact(a),"\n")

if __name__ == "__main__":
    main()