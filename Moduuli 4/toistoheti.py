komento = input ("anna komento:")

while komento != "lopeta": 
    if komento == "MAYDAY":
        break
    print("suoritetaan komento:", komento)
    komento = input("anna komento:")

print("toimminnot lopetettu")

