class car:
    def __init__(self, color, brand, year, speed):
        self.color = color
        self.brand = brand
        self.year = year
        self.speed = speed

    def drive(self):
        print(f"The {self.color} {self.brand} is driving at {self.speed} km/h")

    def stop(self):
        print(f"The {self.color} {self.brand} has stopped")


my_car = car("red", "Toyota", 2020, 100)
your_car = car("blue", "Honda", 2019, 80)
my_car.drive()
your_car.stop()
