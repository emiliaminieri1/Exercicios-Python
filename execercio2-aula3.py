entrada1 =float(input("Digite Salário:"))
entrada2 = float(input("Outras entradas"))
renda = entrada1 + entrada2

filhos= int(input("Digite o número de filhos"))
desp_aluguel = float(input("Aluguel:"))
desp_agua = float(input("Conta de água:"))
desp_luz = float(input("Conta de luz:"))
desp_escola = float(input("Escola:"))
desp_saude = float(input("Plano de Saúde:"))
desp_mercado = float(input("Supermercado:"))
saldo = renda - desp_aluguel-desp_agua-desp_luz-desp_escola-desp_saude-desp_mercado-desp_saude

print("Renda:",renda)
print("Total de despesas:",desp_aluguel+desp_agua+desp_luz+desp_escola+desp_saude+desp_mercado+desp_saude)
print("Despesa com escola por filho:",desp_escola/filhos)
print("Saldo:",saldo)
saldo = saldo<1
print("Saldo negativo:",saldo)

