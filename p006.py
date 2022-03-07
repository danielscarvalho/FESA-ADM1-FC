acumulador=0

while True:
    val = float(input("Novo val: "))
    if val < 0:
        break
    acumulador = acumulador + val
    
print(acumulador)
