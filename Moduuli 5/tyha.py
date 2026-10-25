nimet =[]

nimi = input("anna joku nimi: ")

while nimi != "":
    nimet.append(nimi)
    nimi = input ("anna joku nimi:")

print(nimet)

print("tulostetaan nimet:")

for n in nimet:
    print(f"terhvehyds, {n}!")

print("ohjelma loppui.")

