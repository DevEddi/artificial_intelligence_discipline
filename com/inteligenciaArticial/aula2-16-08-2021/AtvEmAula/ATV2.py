"""
Supondo que a população de um país A seja da ordem de 80.000
habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200.000 habitantes com uma taxa de crescimento
de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a
população do país B, mantidas as taxas de crescimento.
"""

PopA = 80000
PopB = 200000
x = 0
while PopA <= PopB:
     PopB = PopB * 1.5
     PopA = PopA * 3
     x = x + 1
print(x)


