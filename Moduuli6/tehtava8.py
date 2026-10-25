#Ohjelma, jossa viiden tuotteen kustannukset lasketaan yhteen ja tulostetaan lopuksi for silmukkaa käyttäen
kustannukset = []
for i in range(5):
    kustannus = float(input("Tuoteen valmistuskustannus: €"))
    kustannukset.append(kustannus)

print(f"Valmistuskustannukset yhteensä: {sum(kustannukset)} €")