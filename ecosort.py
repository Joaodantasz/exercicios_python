faturamento = 0
ticketmedio = 0
leves = 0
padrao = 0
pesados = 0
internacionais = 0
nacionais = 0
contador = 0
while contador <= 9:
    contador = contador + 1

    print("-----------------------------------")
    print("PACOTE N°: " + str(contador))
    print("Digite o peso do pacote:")

    peso = float(input())

    print("O frete é internacional? (sim/não)")
    internacional = input()

    if peso <= 2:
        valor = 10
        leves = leves + 1
        print("Peso: Leve")
        print("Taxa base: R$ 10")
    else:
        if peso > 2 and peso <= 10:
            valor = 20
            padrao = padrao + 1
            print("Peso: Padrão")
            print("Taxa base: R$ 20")
        else:
            valor = 30
            pesados = pesados + 1
            print("Peso: Pesado")
            print("Taxa base: R$ 30")
    if internacional == "sim":
        taxa = 0.2
        internacionais = internacionais + 1
        print("Acréscimo internacional: 20%")
    else:
        taxa = 0
        nacionais = nacionais + 1
        print("Sem acréscimo internacional")

    valorfinal = valor + valor * taxa
    faturamento = faturamento + valorfinal
    print("Valor final do frete: R$ " + str(valorfinal))
ticketmedio = faturamento / 10

print("-----------------------------------")
print("RELATÓRIO FINAL")
print("-----------------------------------")
print("Pacotes processados: 10")
print("Pacotes leves: " + str(leves))
print("Pacotes padrão: " + str(padrao))
print("Pacotes pesados: " + str(pesados))
print("-----------------------------------")
print("Fretes internacionais: " + str(internacionais))
print("Fretes nacionais: " + str(nacionais))
print("-----------------------------------")
print("Faturamento total: R$ " + str(faturamento))
print("Ticket médio por pacote: R$ " + str(ticketmedio))
print("-----------------------------------")
