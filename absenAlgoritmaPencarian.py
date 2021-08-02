#Program Pencarian dengan menerapkan algoritma Binary Search dan Sequential Search

#Pengurutan bilangan dengan Insertion Sort
def insertionSort(A):
    #kamus
    n = len(A)
    temp = 0
    #Algoritma
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j >= 0 and A[j] > temp :
            A[j+1] = A[j]
            j = j-1
        A[j+1] = temp
    return A

#fungsi binary search
def binarySearch(key,A) :
    #kamus
    n = len(A)
    left = 0
    right = n-1
    statusKetemu = False
    #algoritma
    insertionSort(A)
    print("Array A saat ini :",A)
    while left <= right and not statusKetemu :
        middle = (left+right) // 2
        print("left :",left)
        print("right :",right)
        print("middle :",middle)
        print(10*"==")
        if key == A[middle] :
            statusKetemu = True
        else :
            if key < A[middle] :
                right = middle - 1
            else :
                left = middle + 1
    return statusKetemu

#fungsi sequential search
# def sequentialSearch(key,A):
#     #kamus
#     n = len(A)
#     statusKetemu = False
#     #algoritma
#     for i in range(n) :
#         if key == A[i] :
#             statusKetemu = True
#         print("loop ke-",i+1)
#         print("Status ketemu : ",statusKetemu)
#     return statusKetemu

def main():
    A = [3,4,2,1,5]
    print("Diketahui array A = ",A)
    k = int(input("Masukkan elemen yang sedang dicari : "))
    print("-----Binary Search-----")
    print("Apakah elemen k ada di dalam array A ?",binarySearch(k,A))
#     print("\n")
#     print("-----Sequential Search-----")
#     print("Apakah elemen k ada di dalam array A ?",sequentialSearch(k,A))

if __name__  == "__main__" :
    main()