const salario = parseInt(prompt("Digite o valor do seu salário em reais: "));
const gasto1 = parseInt(prompt("Digite o valor médio da sua conta de luz: "));
const gasto2 = parseInt(prompt("Digite o valor médio da sua conta de água: "));
const gasto3 = parseInt(prompt("Digite o valor médio do seu aluguel (se tiver): "));
const gasto4 = parseInt(prompt("Digite o valor médio do seu supermercado: "));
const gasto5 = parseInt(prompt("Digite o valor médio do seu gás de cozinha: "));
const gasto6 = parseInt(prompt("Digite o valor da sua conta de internet: "));

const somagastos = gasto1 + gasto2 + gasto3 + gasto4 + gasto5 + gasto6;

const sobra = salario - somagastos;
const sobrapercentual = ((sobra * 100) / salario).toFixed(2);

if (sobra === 0) {
    console.log('Não terá sobra de dinheiro esse mês, cuidado para não extrapolar nos gastos.');
} else if (sobra < 0) {
    console.log('Seus gastos ultrapassaram o seu salário este mês, algo não poderá ser pago.');
} else if (sobra < salario * 0.3) {
    console.log(`Sobra ${sobrapercentual}% do seu salário (${sobra}), tente guardar uma parte desse dinheiro para emergências.`);
} else if (sobra < salario * 0.5) {
    console.log(`Parabéns, você tem ${sobrapercentual}% de seu dinheiro sobrando (${sobra}) para guardar e gastar com lazer.`);
} else if (sobra > salario * 0.5) {
    console.log(`Está sobrando ${sobrapercentual}% do seu salário (${sobra}), considere investir uma parte dessa sobra para gerar lucro para você.`);
}