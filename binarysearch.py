#Fungsi binary search

def binarySearch(key,A):
    #kamus
    n = len(A)
    left = 0
    right = n-1
    ketemu = False #untuk pertamakali elemen yg dicari belum ketemu

    #loop
    while left <= right and not ketemu :
        #compute middle position
        middle = (left+right) // 2
        print("left :",left)
        print("right :",right)
        print("middle :",middle)
        print("\n")
        if key == A[middle] :
            ketemu = True
        else :
            #key smaller then middle element
            if key < A[middle] :
                right = middle - 1
            else :
                left = middle +1
    return ketemu

def main() :
    A = [1,2,3,4,5]
    k = int(input("Masukkan elemen yang dicari : "))
    print("Apakah elemen k ada di array A? ",binarySearch(k,A))

if __name__ == "__main__" :
    main()