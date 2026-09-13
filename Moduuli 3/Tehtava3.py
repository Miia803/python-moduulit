sukupuoli = int(input("Mikä on sinun sukupuolesi? (1 = mies, 2 = nainen): "))
if sukupuoli == 1:
    hemoglobiini =float(input("Mikä on sinun hemoglobiiniarvosi?"))
    if hemoglobiini >=175:
        print("Sinulla on korkea hemoglobiiniarvo")
    elif hemoglobiini <=117:
        print("Sinulla on matala hemoglogiiniarvo")
    else:
        print("Sinulla on normaali hemoglobiiniarvo")
elif sukupuoli == 2:
    hemoglobiini =int(input("Mikä on sinun hemoglobiiniarvosi?"))
    if hemoglobiini >=195:
        print("Sinulla on korkea normaali hemoglobiiniarvo")
    elif hemoglobiini <134:
        print("Sinulla on matala hemoglogiiniarvo")
    else:
        print("Sinulla on normaali hemoglobiiniarvo")

