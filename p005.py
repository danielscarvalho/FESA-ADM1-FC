def calc(a, b):
    return 1/a * b**2

def getval():
    return float(input("Informe o valor: "))

x=getval()
y=getval()

print("Resultado:", x+y, x-y, x*y, x/y, x**y, calc(x, y))
print("Resultado:", type(x+y), type(x-y), type(x*y), type(x/y), type(x**y), type(calc(x, y)))




