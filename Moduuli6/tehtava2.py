#kokonaisluku, kolmella jaollinen, viidellä jaollinen, molemmille jaollinen
luku = int(input("anna kokonaisluku: "))
if luku % 3 == 0 :
    print(f"{luku} on kolmella jaollinen")
if luku % 5 == 0 :
    print(f"{luku} on viidellä jaollinen")
if luku % 3 == 0 and luku % 5 == 0 :
    print(f"{luku} on jaollinen molemmilla luvuilla!")
    

