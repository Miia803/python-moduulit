#sqrt-funktion käyttö
from math import sqrt
while True:
    luku = int(input("anna luku: "))
    print(f"luvun {luku} neliöjuuri on {sqrt(luku)}")
    if luku < 0:
        print("virheellinen numero")
    elif luku > 0:
        print(f"luvun {luku} neliöjuuri on {sqrt(luku)}")
    elif luku == 0:
        break
    

