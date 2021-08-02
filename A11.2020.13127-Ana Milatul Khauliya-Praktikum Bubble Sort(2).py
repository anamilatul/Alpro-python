#program pengurutan array
def bubbleSort_Ascending(A) :
    n = len(A)
    urutan = False
    while not urutan :
        urutan = True
        for i in range(1,n) :
            if A[i-1] > A[i] :
                urutan = False
                print("Elemen yang ditukar yaitu ", A[i-1], "dengan", A[i])
                A[i-1], A[i] = A[i], A[i-1]
            print(A)
        print("Status urut : ", urutan)
        print(12*"--")
    return A

def bubbleSort_Descending(A) :
    n = len(A)
    urutan = False
    while not urutan :
        urutan = True
        for i in range(1,n) :
            if A[i] > A[i-1] :
                urutan = False
                print("Elemen yang ditukar yaitu ", A[i], "dengan", A[i-1])
                A[i], A[i-1] = A[i-1], A[i]
            print(A)
        print("Status urut : ", urutan)
        print(12*"--")
    return A

def main() :
    print("--nomor 1--")
    A = [10, 27, 5, 33, 2]
    print("Diketahui array A = ", A)
    print("...Pengurutan Secara Ascending...")
    print("Hasil : ",bubbleSort_Ascending(A))
    print(15*"==")
    print("...Pengurutan Secara Descending...")
    print("Hasil : ",bubbleSort_Descending(A))
    print(15*"==")
    print("--nomor 2--")
    A2 = [5, 2, 10, 27, 33]
    print("Diketahui array A = ", A2)
    print("...Pengurutan Secara Ascending...")
    print("Hasil : ",bubbleSort_Ascending(A2))
    print(15*"==")
    print("...Pengurutan Secara Descending...")
    print("Hasil : ",bubbleSort_Descending(A2))
    
if __name__ == "__main__" :
    main()
