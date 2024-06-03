# [expressão for elemento in lista if condição]
quadrados = [x**2 for x in range(1, 6)]

print(quadrados)

quadrados2 = []
for x in range(1, 6):
    quadrados2.append(x**2)

print(quadrados2)

# FILTRAGEM DE ELEMENTOS
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

pares2 = []
for x in range(10):
    if x % 2 == 0:
        pares2.append(x)
print(pares2)

# TRANSFORMAÇÃO DE ELEMENTOS
mensagens = ["Hoje", "estou", "animado!"]
maiuscula = [msg.upper() for msg in mensagens]
print(maiuscula)

mensagens2 = ["Amanhã", "será", "melhor!"]
maiuscula2 = []
for msg in mensagens2:
    maiuscula2.append(msg.upper())
print(maiuscula2)

# { novo_valor: expressao for elemento in lista if condição}
quadrados_dicionario = { x: x**2 for x in range(1, 6) }
print(quadrados_dicionario)

q2 = {}
for x in range(1, 6):
    q2[x] = x**2
print(q2)
