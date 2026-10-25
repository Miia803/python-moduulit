#ohjelma joka simuloi tehtaan tuotantolinjaa. tallennetaan tuotteiden nimet ja määrät oimiin listoihin. jos käyttäjä vastaa kyllä, ohjelma kysyy seuraavan tuotteen ja määrän. kunnes käyttäjä syöttää ei. Ohjelma tulostaa kaikki valmistetut tuotteet ja niiden määrät
tuotteet = []
määrät = []
while True:
    tuote = input("Mitä tuotetta valmistetaan? : ")
    määrä = int(input("Kuinka monta valmistetaan? : "))
    tuotteet.append(tuote)
    määrät.append(määrä)
    jatketaanko = input("Jatketaanko tuotantoa (kyllä/ei)? ")
    if jatketaanko == "ei":
        break
print("Tuotanto lopetettu!")

print("Valmistetut tuotteet: ")
for i in range(len(tuotteet)):
    print(f"{tuotteet[i]}: {määrät[i]} kpl")