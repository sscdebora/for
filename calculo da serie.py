print("Débora Cristina Souza Santos, result final é 26.46888742423745")
#soma= (1/1 + 2/3 + 3/5 + .... 99/50)
controle=0
soma=0
for i in range (1,100,2):
    controle=controle+1
    print(controle, "/", i)
    soma=soma+(controle/i)
print(soma)
