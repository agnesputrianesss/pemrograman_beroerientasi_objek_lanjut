# Nama  : Agnes Putri Saraswati
# Kelas : TI21K
# NIM   : 210511104 

class Perusahaan:
    def __init__(self, name):
        self.name = name
        self.karyawan = Karyawan()
        print("PT. MB textile")

class Data:
    def __init__(self, name, sience, placed):
        self.name = name
        self.sience = sience
        self.placed = placed

class Karyawan:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print("Nama: ",item.name,",Sejak", item.sience, "penempatan",item.placed)
    
    def remove_item(self, item):
        self.items.remove(item)

perusahaan = Perusahaan(" ")
data1 = Data("Agnes Putri Saraswati", 2019, "MB Kuningan")
data2 = Data("Nisa Uzufatul Jannah.", 2020, "MB Cirebon")
data3 = Data("Yeyet Nurul Hayati.", 2023, "MB Majalengka")
print("="*40)

perusahaan.karyawan.add_item(data1)
perusahaan.karyawan.add_item(data2)
perusahaan.karyawan.add_item(data3)
perusahaan.karyawan.items
print(" ")
