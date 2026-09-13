nimi = input("Mikä on sinun nimesi? ")

if nimi == "Matti":
    print("Seuraava, kiitos!")
else:
    print("Montako keittoannosta haluat?")
    annos = int(input("montako keittoannosta haluat: "))
    print(f"Keittoannoksia on {annos} * 5.90 euroa = {annos * 5.90} euroa")
    print("Seuraava kiitos")
