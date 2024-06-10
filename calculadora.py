def calcular(x, y, op=1):
    if(op == 1):
        print("A soma é: ", x + y)
    elif(op == 2):
        print("O resto é: ", x - y)
    elif(op == 3):
        print("O produto é: ", x * y)
    elif(op == 4):
        print("O quociente é: ", x / y)
    elif(op == 5):
        print("O resto da divisão é: ", x % y)
    elif(op == 6):
        print("A potência é: ", x ** y)

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
print("OPERAÇÕES")
print("1 Adição")
print("2 Subtração")
print("3 Multiplicação")
print("4 Divisão")
print("5 Resto da divisão")
print("6 Potência")
op = int(input("Escolha a operação: "))
calcular(x, y, op)
