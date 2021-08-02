x = 10
n = ""
# x = int(input("Masukkan x :"))
while x > 0 :
    if x % 2 == 0 :
        n = "0" + n
    else :
        n = "1" + n
    x = x / 2

print (n)