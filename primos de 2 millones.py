x=2000000
y=2
while y < x:
    if x % y == 0:
        x=x/y
    else:
        y=y+1
print(f"el mayor primo que divide a 2 millones es: {y}")  