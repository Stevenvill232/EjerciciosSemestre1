numero = []
a = int(input("Digitar valor 1 -> "))
numero.append(a)
b = int(input("Digitar valor 2 -> "))
numero.append(b)
c = int(input("Digitar valor 3 -> "))
numero.append(c)
d = int(input("Digitar valor 4 -> "))
numero.append(d)
numero.sort()
print(numero)
print("el mayor es", numero[-1])
print("el menor es", numero[0])