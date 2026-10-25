#TUNTIPALKKA, TUNTIMÄÄRÄ, PALKKA, viikonpaiva 

tuntipalkka = float(input("Anna tuntipalkka: "))
tuntimaara = float(input("Anna tuntimäärä: "))
viikonpaiva = input("Anna viikonpäivä: ")
PALKKA = tuntipalkka * tuntimaara
print(f"Palkka on {PALKKA} euroa")
if viikonpaiva == "maanantai" or viikonpaiva == "tiistai" or viikonpaiva == "keskiviikko" or viikonpaiva == "torstai" or viikonpaiva == "perjantai" or viikonpaiva == "lauantai" :
    print(f"viikonpaiva on {viikonpaiva} ja palkka on {PALKKA} euroa")
elif viikonpaiva == "sunnuntai":
    PALKKA = PALKKA * 2
    print(f"viikonpaiva on {viikonpaiva} ja palkka on {PALKKA} euroa")




