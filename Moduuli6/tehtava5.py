#listarakenne, anna sanoja listaan, kunnes sanotaan loppu 
sanat = []
edellinen = ""
while True:
    sana = input("anna sana lisättävään tarinaan: ")
    if sana == "loppu" or sana == edellinen:
        break
    sanat.append(sana)
    edellinen = sana

print(f"annettuja sanoja: {len(sanat)}")
print(" ".join(sanat))

