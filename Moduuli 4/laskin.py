#yksinkertainen laskin #
from ast import While


print("\n---Tervetuloa yksinkertaiseen laskimeen---")

while True:
    #infotaan käyttäjälle miten ohjelma toimii print tulosteen avulla


    print("Valitse mitä toimintoa haluat käyttää:")
    print("A: yhteenlasku\n, B: Vähennyslasku\n, C: kertolasku\n, D:Jakolasku\n, Q = lopeta\n") 

    #kysytään käyttäjältä mitä laskutoimitusta haluaa käyttää
    valinta = input ("Anna valintasi: ").upper()

    #tarkistetaan haluaako käyttäjä lopettaa

    if valinta == "Q": 
        print("Lopetetaan ohjelma....")
        break

        #kysytään käyttäjältä kaksi lukua  

    a = float(input ("Anna esimmäinen luku: "))
    b = float(input ("Anna toinen luku: "))

    #suoritetaan laskutoimitus  

    if valinta == "A":
        print(f"lukujen {a} ja {b} summa on : {a + b}.")
    elif valinta == "B":
        print(f"lukujen {a} ja {b} erotus on : {a - b}.")
    elif valinta == "C":
        print(f"lukujen {a} ja {b} tulo on : {a * b}.")
    elif valinta == "D":
        print(f"lukujen {a} ja {b} osamäärä on : {a / b}.")
    
    else:
        print("Virhellinen valinta")

print ("Ohjelma päättynyt")


#keski parempi kohta ilmoittaa virheellisestä valinnasta 
# kommentoi koodi, mitä se tekee missäkin kohdassa
#        