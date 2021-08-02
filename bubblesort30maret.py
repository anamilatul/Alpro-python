#pengurutan dengan algortima bubble sort

def bubbleSort(L) :
    #kamus
    n = len(L)
    urutan = False
    while not urutan :
        urutan = True
        for i in range (1,n) :
            if L[i-1] > L[i] :
                urutan = False
                print("Elemen yang ditukar yaitu",L[i-1], "dengan", L[i])
                L[i-1],L[i] = L[i],L[i-1]
            print(L)
        print("Status urutnya : ",urutan)
        print("\n")
    return L

def main() :
    A = [10,2,5,33,28]
    print("--nomor 2--")
    print("Diketahui array A :",A)
    print("...Pengurutan dengan algoritma bubble sort secara ascending...")
    print("Hasil : ",bubbleSort(A))

if __name__ == "__main__" :
    main()