const contas = [];

    function adicionarConta() {
      const nomeConta = document.getElementById('nomeConta').value;
      const valorConta = parseFloat(document.getElementById('valorConta').value);

      if (!nomeConta || isNaN(valorConta) || valorConta <= 0) {
        alert('Por favor, insira um nome de conta válido e um valor positivo.');
        return;
      }

      contas.push({ nome: nomeConta, valor: valorConta });
      atualizarListaContas();
      document.getElementById('nomeConta').value = '';
      document.getElementById('valorConta').value = '';
    }

    function atualizarListaContas() {
      const listaContas = document.getElementById('listaContas');
      listaContas.innerHTML = '';
      contas.forEach(conta => {
        const listItem = document.createElement('li');
        listItem.textContent = `${conta.nome}: R$ ${conta.valor}`;
        listaContas.appendChild(listItem);
      });
    }

    function calcularPorcentagem() {
      const salario = parseFloat(document.getElementById('salario').value);

      if (isNaN(salario) || salario <= 0) {
        alert('Por favor, insira um valor de salário válido e positivo.');
        return;
      }

      const totalContas = contas.reduce((total, conta) => total + conta.valor, 0);
      const porcentagem = ((totalContas * 100) / salario).toFixed(2);
      document.getElementById('porcentagem').textContent = `As contas representam ${porcentagem}% do seu salário.`;
    }