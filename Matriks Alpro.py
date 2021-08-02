#Program matriks
A = [[1,2,3],
    [4,5,6],
    [7,8,9]
    ]
B = [[10,20,20],
    [40,50,60],
    [70,80,90]
    ]

#nomor 1
def nana(A) :
    print("Nomor 1, Perkalian Matriks A dengan skalar k")
    k = int(input("Masukkan bilangan : "))
    for i in range(len(A)) :
        for j in range(len(A[0])) :
            print(k * A[i][j], end=" ")
        print("\n")

#Nomor 2
def perkalianAB(A,B) :
    print("Nomor 2, Perkalian matriks A dengan matriks B")
    mat = [0]*len(A)
    for i in range(len(A)) :
        mat[i] = [0] * len(A[0])
        for j in range(len(A[0])) :
            mat[i][j] = A[i][j] * B[i][j]
            print(mat[i][j], end=" ")
        print("\n")

#Nomor 3
def jumlahMatriks(A,B) :
    print("Nomor 3, Penjumlahan matriks A dengan matriks B")
    mat=[0] * len(A)
    for i in range(len(A)) :
        mat[i] = [0] *len(A[0])
        for j in range(len(A[0])) :
            mat[i][j] = A[i][j] + B[i][j]
            print(mat[i][j], end=" ")
        print("\n")

def penjumlahan(A,B) :
    print("Nomor 3, Penjumlahan semua elemen pada Matriks A dan Matriks B")
    mat = [0] * len(A)
    jml = 0
    for i in range(len(A)):
        mat[i] = [0] * len(A[0])
        for j in range(len(A[0])) :
            mat[i][j] = A[i][j] + B[i][j]
            jml = mat[i][j] + jml
    print(jml)

def main() :
    nana(A)
    perkalianAB(A,B)
    jumlahMatriks(A,B)
    penjumlahan(A,B)

if __name__ == "__main__" :
    main()