fahrenheit_str = input("Syötä lämpötila Fahrenheit-asteina: ")
fahrenheit = float (fahrenheit_str)
celsius = (fahrenheit - 32) * 5 / 9
print (f"Lämpötila on Celsius-asteina: {celsius:6.2f}")
