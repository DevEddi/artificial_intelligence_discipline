
print("Informe a temperatura: ")
c = input()
f =(9/5) * float(c) +32
if f <= 0:
  print("Congelando")
elif  f <= 20:
  print("Frio")
elif  f <= 35:
  print("Quente")
else:
  print("Muito Quente")

