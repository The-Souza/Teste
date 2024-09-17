texto = "IMPORTANTE: EssA string pode ser informada atrAvés de qualquer entrada de suA preferência ou pode ser previAmente definidA no código"
letras = []
contagem = 0

for letra in texto:
    if letra == 'A':
        letras.append(letra)
        contagem += 1
    elif letra == 'a':
        letras.append(letra)
        contagem += 1

print(letras)
print()
print('Quantidade de letras "A":', contagem)
