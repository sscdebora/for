n1=float(input("Insira a primeira nota:\n"))
n2=float(input("Insira a segunda nota:\n"))
media=(n1+n2)/(1+1)
if media>=7.5:
    print("Sua média:{}" .format(media))
    print("Parabéns, você foi aprovado!")

#Média ponderada é calculada pela soma das notas, sendo que as notas devem ser multiplicadas pelo seu peso, e divididas pela soma dos pesos por prova.
else:
    n3=float(input("Insira a terceira nota:\n"))
    media=(n1+n2+(n3*3))/(1+1+3)
    if media >6:
        print("Parabéns, você foi aprovado!")
    else:
        print("Você foi reprovado.")
