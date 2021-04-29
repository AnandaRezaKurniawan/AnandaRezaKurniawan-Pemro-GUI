class Aritmatika :
    @staticmethod
    def tambah (a,b):
        return a + b

    @staticmethod
    def kurang (a,b):
        return a - b

    @staticmethod
    def bagi (a,b):
        return a / b

    @staticmethod
    def bagi_int (a,b):
        return a // b

    @staticmethod
    def pangkat (a,b):
        return a ** b

# langsung panggil class dan fungsi
print (Aritmatika.tambah(5,5))

# buat objek terlebih dahulu
objekA = Aritmatika()

print (objekA.pangkat(2,3))
