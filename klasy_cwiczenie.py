class ElectricCar:
    def __init__(self):
        self.energy = 100

    def charge(self):
        self.energy = 100
        return "OK"

    def drive(self, distance):
        if distance > self.energy:
            value = self.energy
            self.energy = 0
        else:
            value = distance
            self.energy = self.energy - distance

        return value


ec = ElectricCar()
print(ec.drive(80))
print(ec.drive(50))
print(ec.charge())
print(ec.drive(90))
