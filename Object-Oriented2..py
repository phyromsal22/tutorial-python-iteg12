class car:
    def ___init__(self, colour, model, year, speed):
        self.colour = colour
        self.model = model
        self.year = year
        self.speed = speed

    def drive(self):
        print(f"The {self.colour} {self.model} is driving at {self.speed} km/h")

    def stop(self):
        print(f"The {self.colour} {self.model} has stopped")
