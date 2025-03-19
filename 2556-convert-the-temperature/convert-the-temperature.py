class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00

        ans = [kelvin, Fahrenheit]

        return (ans)


       