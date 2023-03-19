class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")
mobilA = Mobil("Innova", "Silver")
mobilA.info() # Output: Mobil Innova berwarna Silver