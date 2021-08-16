# Calcule a soma dos números pares entre 102 e 150;

s = 0
for x in range(102, 150):
    if x % 2 == 0:
        s = s + x
        print(s)

