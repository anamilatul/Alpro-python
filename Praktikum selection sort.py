#fungsi algoritma selection
#pengurutan secara ascending(dari kecil ke besar)

def selectionSort(L):
    #kamus
    n = len(L)

    #loop1, for digunakan untuk compare semua elemen list L
    for i in range(0,n-1):
        #assign variabel minimum dengan indeks awal
        minimum = i
        print("loop ", i+1)
        #loop2, for untuk mencari elemen paling kecil
        for j in range (i+1,n):
            #bandingkan elemen pada indeks minimum dengan elemen pada indeks ke j
            if L[minimum] > L[j] :
                #assign minimum dengan j
                minimum = j

        #swap L[minimum] dengan L[i]
        print("L[i] :",L[i],"; L[minimum] :", L[minimum])
        L[i],L[minimum] = L[minimum],L[i]
        print("L[i] :",L[i],"; L[minimum] :", L[minimum])
        print(L)
        print("\n")
    return L

def main() :
    A = [3,4,2,1,5]
    result = selectionSort(A)
    print(result)

    #tambahan
    # A[0] = 11
    # print(selectionSort(A))
    # ubahA()

if __name__ == "__main__" :
    main()