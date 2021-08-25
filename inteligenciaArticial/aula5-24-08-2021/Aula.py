#funcoes


#Procedimento com argumentos
def f2(arg):
    print('Argumento: ', arg)


f2([2, 4, 1, 6])

#----------------
#Argumento padrão e múltiplos retornos
#----------------

def opera(x, y=0):  #y é 0 por default
    return x+y, x-y, x**y
soma, sub, pot = opera(2, 5)
opera(4)

#example 2
def teste():
    pass
    pass
    return "Jose", [2, 4, 5], 3.14
nome, l1, num = teste()
print(nome)
print(l1)
print(num)


#----------------
#
#----------------

def fib(n):
    """Retorna o nesimo termo fibonacci"""
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))
print(fib)

#----------------
#
#----------------