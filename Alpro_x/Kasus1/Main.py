#struktur program
#contoh memanggil Library yang dibuat user
import MyLib

def main():
    a = 12
    b = 11
    c = 2
    d = 1
    x = 100
    y = 5
    e = MyLib.tambah(c,d)
    f = MyLib.kurang(a,c)
    g = MyLib.bagiFloat(b,c)
    h = MyLib.bagiInt(b,c)
    i = MyLib.kali(a,b)
    print(e,f,g,h,i)
    listA = [int]*10
    MyLib.isiListRandom(listA,10)
    print("Panjang List :", MyLib.lenghtList(listA))
    MyLib.cetakList(listA,10)
    print("Penjumlahan elemen list ",MyLib.sumList(listA,10))
    print("Rata-rata elemen list ",MyLib.averageList(listA,10))
    print("Elemen max :", MyLib.maxList(listA,10))
    print("Elemen min :", MyLib.minList(listA,10))

if __name__ == '__main__' :
    main()