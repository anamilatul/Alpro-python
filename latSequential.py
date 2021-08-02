#Fungsi sequential search

def sequential(key,A) :
    #kamus
    n = len(A)
    ketemu = False

    #algoritma
    for i in range(n):
        if key == A[i] :
            ketemu = True
        print("loop ke-",i+1)
        print("Status ketemu :",ketemu)
    return ketemu

#Untuk mencari posisi indeksnya
# def sequential(key,A) :
#     #kamus
#     n = len(A)
#     ketemu = -1

#     #algoritma
#     for i in range(n):
#         if key == A[i] :
#             ketemu = True
#     return ketemu

def main():
    A = [6,8,20,9,7]
    k = int(input("Masukkan elemen yang dicari : "))
    print("Apakah elemen k ada di dalam array A ?",sequential(k,A))

if __name__ == "__main__":
    main( )