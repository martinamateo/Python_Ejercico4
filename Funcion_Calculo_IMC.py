# El peso se coloca en kilos Ej:78 / La altura se coloca metros "." (punto) centimetros. Ej: 1.80

peso=float(input("Peso: ")) 
altura=float(input("Altura: "))

def imc(peso, altura):
    return peso/(altura**2)
indice = imc(peso, altura)

print("imc: {}".format(indice))


