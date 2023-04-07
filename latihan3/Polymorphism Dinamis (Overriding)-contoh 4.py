# Nama   : Agnes Putri Saraswati
# NIM    : 210511104
# Kelas  : TIF21K
# Matkul : Pemrogaman Berorientasi Objek 2

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Starting car...")


class Motorcycle(Vehicle):

    def start(self):
        print("Starting motorcycle...")


class Bus(Vehicle):

    def start(self):
        print("Starting bus...")


vehicles = [Car(), Motorcycle(), Bus()]
for vehicle in vehicles:
    vehicle.start()
