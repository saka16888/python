class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

c = Celsius(300)
#print(c.temperature)
print(c.to_fahrenheit())
