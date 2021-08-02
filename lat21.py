#1-bubblesort,descending
# data = [2,1,3,7]
# program = True

# while program:
#     n = 0
#     for x in range(len(data)-1):
#         if data[x]<data[x+1]:
#             data[x],data[x+1] = data[x+1],data[x]
#             n += 1
#     if n == 0 :
#         program = False

# print(data)

#2-rekursif
# def kali(x,y):
#     if x == 0 :
#         return 0
#     else :
#         return y+kali(x-1,y)
# print(kali(4,5))

#3
# def volume(s):
#     return s*s*s
# def luas(s):
#     return (s*s)*6
# def rataRata(x,y,z):
#     return (x+y+z)/2

# v1 = volume(10)
# v2 = volume(12)
# v3 = volume(25)

# l1 = luas(10)
# l2 = luas(12)
# l3 = luas(25)

# print(v1)
# print(v2)
# print(v3)

# print(rataRata(v1,v2,v3))

#pakeko
#1
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x*factorial(x-1)
# n1 = factorial(int(input("Bilangan factorial pertama : ")))
# n2 = factorial(int(input("Bilangan factorial kedua : ")))
# print("Nilai factorial pertama :",n1)
# print("Nilai factorial kedua :",n2)
# print("Nilai perkaliannya :",n1*n2)
# n3 = n1*n2

# if n3%2 == 0 :
#     print("Genap")
# else:
#     print("Ganjil")

#2
# L = [12,5,8,6,7,0,9]
# print(L)
# n = 0
# n2 = 0
# print("Bilangan kelipatan 3 dalam list adalah :") #nb:kalo pingin 0 ga masuk, if n == 0 :continue
# for x in L:
#     if x%3 == 0:
#         n += x
#         n2 += 1
#         print(x)
# print("Total list kelipatan 3 :",n)
# print("Banyaknya list kelipatan 3 :",n2)

#3-koordinat ADT

# class point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def geser(self,p):
#         self.x = self.x + p.x
#         self.y = self.y + p.y

# x1 = int(input("Masukkan nilai sumbu x awal : "))
# x2 = int(input("Masukkan nilai sumbu y awal : "))
# p1 = point(x1,x2)

# x3 = int(input("Masukkan nilai sumbu x pergeseran : "))
# x4 = int(input("Masukkan nilai sumbu y pergeseran : "))
# p2 = point(x3,x4)

# print("Titik awal : sumbu x =",x1,"sumbu y =",x2)
# print("Titik geser : sumbu x =",x3,"sumbu y =",x4)

# p1.geser(p2)
# print(p1.x,p1.y)

#4-ADT stnk
# class data(object):
#     def __init__(self,nama,jk,umur):
#         self.nama = nama
#         self.jk = jk
#         self.umur = umur
#     def tampil(self):
#         print("nama :",self.nama,"\njk :",self.jk,"\numur :",self.umur)
# n = data("Ana","Perempuan",19)
# n.tampil()