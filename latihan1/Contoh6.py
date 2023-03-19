class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
        
    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y

# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(7, 2)) # Output: 9
print(Kalkulator.subtract(15, 5)) # Output: 10

# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(2, 3)) # Output: 6
print(Kalkulator.divide(18, 9)) # Output: 2.0