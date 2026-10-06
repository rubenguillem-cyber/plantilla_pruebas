# Toda esta parte puede sustituirse por un vector
temperaturas = []
for temperatura in range(5):
    temperatura = float(input("Introduce un valor de temperatura: "))
    temperaturas.append(temperatura)
# Se puede hacer la prueba con: 
# temperaturas = [21, 25, 28, 33, 21]
print(temperaturas)

total = 0

for temperatura in temperaturas:
    total = total + temperatura

print(total)

media = total / len(temperaturas)

print(media)