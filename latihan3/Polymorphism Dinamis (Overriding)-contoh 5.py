# Nama   : Agnes Putri Saraswati
# NIM    : 210511104
# Kelas  : TIF21K
# Matkul : Pemrogaman Berorientasi Objek 2

class Kucing:

    def bersuara(self):
        print("Meow")


class Anjing:
    def bersuara(self):
        print("Guk guk")


def cetak_suara(objek):
    objek.bersuara()


kucing = Kucing()
ajing = Anjing()
cetak_suara(kucing)  # Output: Meow
cetak_suara(ajing)  # Output: Guk guk
