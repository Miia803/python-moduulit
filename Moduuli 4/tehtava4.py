salasana = "qwerty"  

käyttäjätunnus = "omanimi"

 

yritykset = 0

yht = 5

print("Tervetuloa kokeilemaan onko käyttäjätunnuksesi ja salasanasi yleisimpien joukossa. Yrityksiä on 5. Onnea matkaan")

 

 

while True:

    yritykset +=1

    kyritys = input("anna käyttäjänimesi: ")

    syritys = input("anna salasanasi: ")

    if yritykset == yht:

        print("pääsy evätty")

        break

 

    if salasana != syritys or käyttäjätunnus != kyritys:

        print("väärin")

        continue

    if salasana == syritys and käyttäjätunnus == kyritys:

        print("Tervetuloa")

        break