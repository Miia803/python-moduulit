#ohjelma joka laskee monessa sanassa on enemmän kuin 5 kirjainta. käytetään ien()
sanat = []
while True:
    sana = input("anna sana (tyhjä lopettaa): ")
    if sana == "":
        break
    sanat.append(sana)

laskuri = 0
for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print(f"sanat joissa on enemmän kuin 5 kirjainta: {laskuri}")