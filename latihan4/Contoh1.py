class Pekerja:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Perusahaan:
    def __init__(self, nama, pekerja):
        self.nama = nama
        self.pekerja = pekerja
    
    def daftar_pekerja1(self):
        for pekerja in self.pekerja:
            print("Khongguan", pekerja.nama, pekerja.umur)

    def daftar_pekerja2(self):
        for pekerja in self.pekerja:
            print("Hatari", pekerja.nama, pekerja.umur)

pekerja1 = Pekerja("Agnes", 21)
pekerja2 = Pekerja("Uyuy", 20)
perusahaan1 = Perusahaan("Khongguan", [pekerja1])
perusahaan2 = Perusahaan("Hatari", [pekerja2])
perusahaan1.daftar_pekerja1()
perusahaan2.daftar_pekerja2()