#Kasus 2
#Program save game
import random #untuk membangkitkan nilai acak dari state

#deklarasi variabel global dictGameSaving
global dictGameSaving
#inisialisasi variabel global dictGameSaving sebagai dictionary
dictGameSaving = {}

def saveGame(key,stateValue):
    #merupakan prosedur untuk save game state
    #key adalah kunci bertipe string
    #stateValue adalah vektor atau list dari state
    #langkah 1.Ambil global variabel, contoh : global variabel_globalnya
    global dictGameSaving
    #langkah 2.Cek apakah key ada di dalam dictGameSaving?
    if key in dictGameSaving:
    #langkah 2.1 (di dalam langkah 2)berikan pertanyaan h = input("apakah datanya mau ditumpuk?")
        h = input("Apakah datanya mau ditumpuk (Y/T) :")
    #langkah 2.1.1 (di dalam langkah 2.1) cek apakah h == "Y"
        if h == "Y" :
    #langkah 2.1.1.1 jika iya maka simpan stateValue di dalam dictionary dengan key
            dictGameSaving[key] = stateValue
    #langkah 2.1.1.2 lanjutan dari sebelumnya, panggil lihatGameState()
            lihatGameState()
    #langkah 2.2 ini adalah else, simpan stateValue di dalam dictionary dengan key
    else :
        dictGameSaving[key] = stateValue
    #langkah 2.3 lanjutan dari sebelumnya, panggil lihatGameState()
        lihatGameState()

def lihatGameState():
    #ambil global variable
    global dictGameSaving
    #outputkan global variable
    print(dictGameSaving)

def loadGame(key) :
    global dictGameSaving
    if key in dictGameSaving:
        return dictGameSaving[key]
    else:
        return 0

def main():
    n = input("Apakah mau menyimpan state (Y/T)? ")
    while(n != "T"):
        state = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        k = input("Masukkan kunci : ")
        saveGame(k,state)
        n = input("Apakah mau menyimpan state lagi (Y/T)? ")
        if n == "T":
            break

if __name__ =="__main__":
    main()
