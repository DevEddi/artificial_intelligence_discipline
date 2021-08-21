"""
Crie um programa que:
◦
Solicite ao usuário o número de avaliações de um
aluno;
◦
Solicite ao usuário o número de alunos;
◦
Para cada aluno, solicite o nome e as notas
necessárias. Armazene num dicionário em que a
chave é o nome e os valores são as notas;
◦
Após a leitura de todas as notas, imprima o nome
do aluno e sua média final;
◦
Calcule a média da turma (baseado na média final)
"""

print("Digite quantidade de avaliações que aluna teve: ")
qntAvalicao = int(input())

print("Digite quantidade de alunos da turma: ")
qntAluno = int(input())

"""
for x in  range(qntAluno):
    print("Digite o nome do aluno: ")
    nomeAluno = input()
    print("Digite os valores das notas: ")
    avalNota = []
    for z in range(qntAvalicao):
        avalNota.append(float(input("Avaliação: ")))
print("Nome: " + str(nomeAluno) +  " nota: " + str(avalNota))
"""
for x in  range(qntAluno):
    print("Digite o nome do aluno: ")
    nomeAluno = input()
    print("Digite os valores das notas: ")
    dicionario = {}
    for z in range(qntAvalicao):
        dicionario[nomeAluno] = float(input())
print("Nome: " + str(nomeAluno) +  " nota: " + str(dicionario[nomeAluno]))
