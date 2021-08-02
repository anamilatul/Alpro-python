import math #untuk memanggil akar/sqrt

class Vector2D(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        #kembalikan (a,b) + (c,d) = (a+c,b+d)
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        #kembalikan (a,b) - (c,d) = (a-c,b-d)
        #lihat persamaan 2
        #1 baris kode, mulai
        return Vector2D(self.x - other.x, self.y - other.y)
        #berhenti disini
    def __mul__(self,other):
        #(a,b) * (c,d) = (a*c,b*d)
        #lihat persamaan 3
        #1 baris kode, mulai
        return Vector2D(self.x * other.x, self.y * other.y)
        #berhenti disini
    def __abs__(self):
        #kembalikan ||a,b|| = akar ((a,b)) * (a,b)),atau
        #akar (A PANGKAT 2+b pangkat 2), gunakan math.sqrt
        #lihat persamaan 4
        #1 baris kode, mulai
        return Vector2D(int(math.sqrt((self.x)**2)), int(math.sqrt((self.y)**2)))
        #ket. dimodifikasi jadi akar(A PANGKAT 2,b pangkat 2) dg math.sqrt
        #berhenti disini
    def __eq__(self,other):
        #cek apakah dua vektor sama
        #1 sampai 4 baris kode, mulai
        return (self.x == other.x) and (self.y == other.y)
        #berhenti disini
    def __str__(self):
        return str(self.x)+" "+str(self.y)

def main():
    v1 = Vector2D(1,2)
    v2 = Vector2D(3,4)
    v3 = v1+v2
    v4 = v1-v2
    v5 = v1*v2
    v6 = abs(v4)
    print(v1.x,v1.y)
    print(v2.x,v2.y)
    print(v3.x,v3.y)
    print(v4.x,v4.y)
    print(v5.x,v5.y)
    print(v6)
    print(v1 == v4)
    print(Vector2D(1,0) == Vector2D(1,0))

if __name__ == "__main__":
    main()

