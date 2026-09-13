vuosiluku = int(input("Anna vuosiluku: "))
print("Vuosi on karkausvuosi") if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0) else print("Vuosi ei ole karkausvuosi")




