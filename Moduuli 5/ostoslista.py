ostoslista = ["kahvi", "rahka", "voi", "leipä"]

while ostoslista:
    tuote = input ("mitä ostit kaupasta")

if tuote in ostoslista:
    
    ostoslista.remove(tuote)
    print("Tuotteita jäljellä", ostoslista)

else:
    print ("tuotteita ei ole listalla")


