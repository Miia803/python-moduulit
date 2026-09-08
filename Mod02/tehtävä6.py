# random
import random


print("Tämä ohjelma arpoo satunnaisen luvun 1-10 väliltä")
luvut = random.randint(1, 10)
print(f"Arvottu luku: {luvut}")
luvut2 = random.randint(1, 10)
print(f"Arvottu luku2: {luvut2}")
luvut3 = random.randint(1, 10)
print(f"Arvottu luku3: {luvut3}")

print(f"arvottu luvut: {luvut}, {luvut2}, {luvut3}")

print("Tämä ohjelma arpoo kolminumeroisen koodin, jossa jokainen numero on 0-9")
koodi = ""
for i in range(3):
    koodi += str(random.randint(0, 9))
print(f"Arvottu koodi: {koodi}")


print("Tämä ohjelma arpoo nelinumeroisen koodin, jossa jokainen numero on 0-6")
koodi = ""
for i in range(4):
    koodi += str(random.randint(0, 6))
print(f"Arvottu koodi: {koodi}")

