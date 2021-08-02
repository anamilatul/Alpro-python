#Dictionary

memberku = {"nim" : "a11.2020.2021", 
"nama" : "mila", 
"course" : ["alpro", "struktur data"]
}

# print(memberku)

memberku_1 = {"nim" : "a11.2020.2022", 
"nama" : "dipta", 
"course" : ["daspro", "alpro"]
}

#menggabungkan key1 dan 2
member_a11 = {1 : memberku, 2 : memberku_1}
print(member_a11)
print(member_a11[2])

#add element
member_a11["alamat"] = "semarang"
print(member_a11)

#assign/set nilai ke variabel
#outputnya akan menumpuk
member_a11["alamat"] = "batang"
print(member_a11)

#Cara akses 
#1. access for key
# print(memberku.keys())

#2. access for value
# print(memberku.values())

#3. access by items
# print(memberku.items())