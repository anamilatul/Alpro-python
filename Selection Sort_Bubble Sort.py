#Selection sort ascending
#notasi algoritmik selection sort

#Fungsi selectionSort(L)
#{Kamus lokal}
#n ← len(L)
#{Algoritma}
#for i ← 0 to n-1 do
#   minimum ← i
#   for k ← i+1 to n do
#       if L[minimum] > L[k] then
#           minimum ← k
#       endif
#   L[i],L[minimum] = L[minimum],L[i]
#   endfor
#endfor
#return L


#algoritma selection 
#pengurutan secara ascending

def selectionSort(L):
    #kamus
    n = len(L)
    
    for i in range(0,n-1) :
        minimum = i
        print("Loop ke-", i+1)
        for k in range(i+1,n) :
            #membandingkan elemen pada indeks minimum dengan elemen indeks ke k
            if L[minimum] > L[k] :
                minimum = k
        #swap L[minimum] dengan L[i]
        print("L[i] :",L[i],"; L[minimum] :",L[minimum])
        L[i],L[minimum] = L[minimum],L[i]
        print("L[i] :",L[i],"; L[minimum] :",L[minimum])
        print(L)
        print(14*"--")
    return L

#algoritma bubble sort(ascending)

def bubbleSort(L) :
    n = len(L)
    urutan = False
    while not urutan :
        urutan = True
        for i in range(1,n) :
            if L[i-1] > L[i] :
                urutan = False
                print("Elemen yang ditukar yaitu ",L[i-1],"dengan", L[i])
                L[i-1],L[i] = L[i],L[i-1]
            print(L)
        print("Status urutnya : ",urutan)
        print(14*"--")
    return L

def main() :
    A = [10,2,5,33,28]
    print("--nomor 1--")
    print("Diketahui array A :", A)
    print("..Selection Sort..")
    print("Hasil :",selectionSort(A))
    print("\n")
    print("--nomor 2--")
    A = [10,2,5,33,28]
    print("Diketahui array A :", A)
    print("..Bubble Sort..")
    print("Hasil :",bubbleSort(A))


if __name__ == "__main__" :
    main()