#While tuotantolinja
print("Tuote valmistettu")
jatketaanko = input("Jatketaanko tuotantoa (kyllä/ei)? ")
while jatketaanko == "kyllä":
    print("Tuote valmistettu")
    jatketaanko = input("Jatketaanko tuotantoa (kyllä/ei)? ")
if jatketaanko == "ei":
    print("Tuotanto lopetettu")
    