class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature * 1.8 + 32


temperature_1 = Celsius(10)
print(temperature_1.temperature)