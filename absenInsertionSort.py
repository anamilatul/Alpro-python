#Program pwngurutan array
#Fungsi insertion sort
#Ascending

def InsertionSort(A) :
    #Kamus
    n = len(A)
    temp = 0

    #Algoritma
    for i in range(1,n) :
        temp = A[i]
        j = i-1
        print("Loop ke-",i)
        print("temp = A[",i,"] = ",i)
        print("j = ",i)
        while j >= 0 and A[j] > temp :
            A[j+1] = A[j]
            print("A[j+1] = ",A[j+1])
            j = j-1
            print("j saat ini = ",j)
        A[j+1] = temp
        print(A)
        print(12*"==")
        print("\n")
    return A

def main() :
    A = [5, 2, 10, 27, 33]
    print("Diketahui array A = ",A)
    print("Hasil akhir = ",InsertionSort(A))

if __name__ == "__main__" :
    main()