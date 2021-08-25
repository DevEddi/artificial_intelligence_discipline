#funcoes


#Procedimento com argumentos
def f2(arg):
    print('Argumento: ', arg)


f2([2, 4, 1, 6])

#----------------
#Argumento padrão e múltiplos retornosa
#----------------

def opera(x, y=0):  #y é 0 por default
    return x+y, x-y, x**y
soma, sub, pot = opera(2, 5)
opera(4)

