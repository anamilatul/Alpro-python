#Program pendataan mata kuliah

def insertionSort(id,makul):
    n = len(id)
    temp_id = 0
    temp_makul = ""
    
    for i in range (1,n):
        temp_id = id[i]
        temp_makul = makul[i]

        j = i-1
        while j >= 0 and id[j] > temp_id :
            id[j+1] = id[j]
            makul[j+1] = makul[j]
            j = j-1
        id[j+1] = temp_id
        makul[j+1] = temp_makul

def inputData(id,makul,n):
    for i in range(n):
        id[i] = int(input("Masukkan Id : "))
        makul[i] = input("Masukkan nama matkul : ")

def lihatData(id,makul,n):
    print("Id || MataKuliah")
    for i in range(n):
        print(id[i],"||",makul[i])
    print("\n")

def urutData(id,makul,n):
    insertionSort(id,makul)
    print("Id || MataKuliah")
    for i in range(n):
        print(id[i],"||",makul[i])
    print("\n")


def main():
    n = int(input("Masukkan jumlah data : "))
    arrId = [int]*n
    arrMakul = [str]*n
    while (True):
        print("Jumlah data yang dimasukkan :",n)
        print("Pilih menu (Ketik 1, 2, 3 atau 0 untuk keluar)\n1.Input Data \n2.Lihat Data \n3.Urut Data")
    
        menu = input("Ketikkan : ")
        if menu == "1" :
            inputData(arrId,arrMakul,n)
        elif menu == "2" :
            lihatData(arrId,arrMakul,n)
        elif menu == "3" :
            urutData(arrId,arrMakul,n)
        if menu == "0" :
            break

if __name__ == "__main__":
    main()