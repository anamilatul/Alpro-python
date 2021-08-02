#Kasus2
#kamus
berat = 0

#Algoritma
nih = input("Masukkan Nama : ")
berat = int(input("Masukkan Berat Badan : "))
print("Hai,", nih)
if berat <= 50 :
    print("Berat Badanmu", berat, "Kg termasuk kategori Kurus")
elif 51 <=berat<= 70 :
    print("Berat Badanmu", berat, "Kg termasuk kategori Normal")
else :
    print("Berat Badanmu", berat, "Kg termasuk kategori Gemuk")