x=2000000
y=2
suma_primos = 0

while y < x:
    z=2
    while z * z <= y:
        if y % z == 0:
            break
        z=z+1
    else:
        suma_primos = suma_primos + y
    y=y+1

print("Suma total de primos de 2 millones:", suma_primos)