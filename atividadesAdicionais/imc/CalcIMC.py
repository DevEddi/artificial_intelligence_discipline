

print("Digite o seu peso: ")
peso = input()
print("Digite a sua altura: ")
altura = input()

imc = float(peso)/ (float(altura) * 2)


if imc < 17:
 print("Muito abaixo do peso")
elif imc < 18.49:
 print("Abaixo do peso")
elif imc < 24.99:
 print("Peso normal")
elif imc < 29.99:
  print("Acima do peso")
elif imc < 34.99:
        print("Obesidade 1")
elif imc < 39.99:
    print("Obesidade 2")
else:
    print("Obesidade 3")

