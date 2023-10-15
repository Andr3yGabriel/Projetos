salario = int(input("Digite o valor do seu salário em reais: "))
gasto1 = int(input("Digite o valor médio da sua conta de luz: "))
gasto2 = int(input("Digite o valor médio da sua conta de água: "))
gasto3 = int(input("Digite o valor médio do seu aluguel (se tiver): "))
gasto4 = int(input("Digite o valor médio do seu supermercado: "))
gasto5 = int(input("Digite o valor médio do seu gás de cozinha: "))
gasto6 = int(input("Digite o valor da sua conta de internet: "))

somagastos = gasto1 + gasto2 + gasto3 + gasto4 + gasto5 + gasto6

sobra = salario-somagastos
sobrapercentual = (sobra*100)//salario

if sobra == 0:
    print('Não terá sobra de dinheiro esse mês, cuidado para não extrapolar nos gastos.')

elif sobra < 0:
    print('Seus gastos ultrapassaram os gastos esse mês, algo não poderá ser pago.')

elif sobra < (salario*0.3):
    print(f'Sobra {sobrapercentual}% do seu salário ({sobra}), tente guardar uma parte desse dinheiro para emergências.')

elif sobra < (salario*0.5):
    print(f'Parabéns, você tem {sobrapercentual}% de seu dinheiro sobrando ({sobra}) para guardar e gastar com lazer.')

else:
    print(f'Está sobrando {sobrapercentual}% do seu salário ({sobra}), considere investir uma parte dessa sobra para gerar lucro pra você.')