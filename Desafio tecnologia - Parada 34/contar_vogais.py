import os

def contar_vogais(string):
    string = string.lower()
    result = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result

print(contar_vogais('Construí com meus sonhos um castelo. Desenhei um universo imaginário.As coisas simples fascinam meu cenário irreal.Realidade que só se choca quando se sente na pele. Devorando o seu ser, pedido de socorro incompreendido. A espera do meu engano sobreviver.Se tornar viver. - Brenda Polide.'))

os.system("pause")