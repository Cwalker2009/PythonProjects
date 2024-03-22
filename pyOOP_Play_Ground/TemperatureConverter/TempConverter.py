class TemperatureConverter:
    def __init__(self,temperature):
        """
        Initializes a TemperatureConverter object.

        Args:
            temperature (float): The initial temperature value.
        """
        self.temperature = temperature
    def convert(self, unit):
        """
        Converts the temperature to the specified unit (C or F) and prints the result.

        Args:
            unit (str): The unit to convert to ("C" or "F").

        Raises:
            ValueError: If an invalid unit is provided.
        """
        self.unit = unit
        if unit == "C":
            res = (self.temperature - 32) * 5/9
            print(f"{self.temperature} F is equal to {res} C")
        elif unit == "F":
            res = (self.temperature * 9/5) + 32
            print(f"{self.temperature} C is equal to {res} F")
        else:
            raise ValueError("invalid unit is passed, C or F should be passed.")
        
if __name__ == "__main__":
    while True:
        try:
            temperature = float(input("Enter temperature: "))
            converter = TemperatureConverter(temperature)

            while True:
                unit = input("Enter unit (C or F): ").upper()
                converter.convert(unit)
        
        except ValueError:
            print("Error Something else is wrong with the code")