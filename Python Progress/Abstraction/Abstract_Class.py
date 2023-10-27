from abc import ABC, abstractmethod


class Car(ABC):
    def Show(self):
        print("My car has 4 wheels !!!")

    @abstractmethod
    def Speed(self):
        pass


class Toyota(Car):
    def Speed(self):
        print("\n--- Toyota ---")
        print("Supra Max Speed = 280 km/h")
        print("Land Cruiser Max Speed = 175 km/h")


class Maruti_Suzuki(Car):
    def Speed(self):
        print("\n--- Maruti_Suzuki ---")
        print("Baleno Max Speed = 190 km/h")
        print("Alto Max Speed = 140 km/h")


ms = Maruti_Suzuki()
ms.Show()
ms.Speed()

t = Toyota()
t.Show()
t.Speed()
