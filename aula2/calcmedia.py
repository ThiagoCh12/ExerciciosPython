def media(notas):
    soma = 0
    for nota in notas:
        soma = soma+nota
    result = soma/4
    return result
        
i=0

notas = []

while i < 4:
    notas.append(float(input("entre com a nota: ")))
    i+=1

print(media(notas))