arvot = []

while True:
    luku = int(input("Anna luku (0 lopettaa): "))
    if luku == 0:
        break
    arvot.append(luku)

print("Pienimmästä suurimpaan:", sorted(arvot))
print("Suurimmasta pienimpään:", sorted(arvot, reverse=True))