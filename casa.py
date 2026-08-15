eletrodomesticos = {
    "Geladeira": 40,
    "Lâmpada": 15,
    "Micro-Ondas": 1000,
    "Chuveiro" : 6000,
    "Televisão" : 100,
    "Air-Fryer" : 1700,
    "Ar-condicionado" : 1000,
    "Computador" : 500, 
}

semTempo = ["Geladeira"]

consumoTotal = 0

for eletronico in eletrodomesticos:
    consumoEletronico = eletrodomesticos[eletronico]
    quantidadeEletronico = int(input(f"Quantos(as) {eletronico} tem na sua casa? "))
    if eletronico in semTempo:
        consumoTotal = consumoTotal + (consumoEletronico*quantidadeEletronico)
    else:
        tempoEletronico = int(input(f"Quantas horas você utiliza o(a) seu(sua) {eletronico} por mês? "))
        consumoTotal = consumoTotal + (consumoEletronico*quantidadeEletronico*tempoEletronico)

consumoTotal = consumoTotal/1000

print(f"Sua casa consome {consumoTotal:.2f} kWh/mês.")
    