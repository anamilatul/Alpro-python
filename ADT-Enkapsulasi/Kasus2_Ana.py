#Kasus2
class CobaNoCons():
    #Attribut disini dengan akses private gunakan "__"
    __cekAttrib = " "
    
    #method
    def setAttrib(self,varAttr):
        self.__cekAttrib = varAttr
    def getAttrib(self):
        return self.__cekAttrib
    
def main():
    #instance mengakses pada konstruktor kosong
    cObj = CobaNoCons()
    #setter method untuk mengeset suatu nilai dari 
    # parameter akutual ke attribut class
    cObj.setAttrib("Hello Word!")
    #assign langsung ke atribut akan gagal karena diprivate
    cObj.__cekAttrib = "gagal"
    #getter method untuk mekanisme pemanggilan attribut kelas
    print(cObj.getAttrib())

if __name__ == "__main__":
    main()