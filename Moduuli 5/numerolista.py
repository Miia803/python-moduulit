numerot =[]

num = int(input("anna numero listaan: "))

while num != 0:
    numerot.append(num)
    num = int (input("anna numero listaan: "))

print(numerot)

summa = 0 

for numero in numerot:
    summa += numero 
    print("summa nyt: ", summa)

print("lopullinen summa on:", summa)
