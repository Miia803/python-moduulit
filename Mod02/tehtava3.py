import math
kanta = float(input("Mikä on suorakulmion kanta? "))
korkeus = float(input("Mikä on suorakulmion korkeus? "))
ala = kanta * korkeus
print(f"Suorakulmion pinta-ala on {ala:.2f}") 
print(f"Suorakulmion piiri on {2 * (kanta + korkeus):.2f}")
