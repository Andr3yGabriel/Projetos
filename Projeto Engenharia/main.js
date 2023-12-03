const contas = [];

    function adicionarConta() {
      const nomeConta = document.getElementById('nomeConta').value;
      const valorConta = parseFloat(document.getElementById('valorConta').value);
      const tipoConta = document.getElementById('tipoConta').value;
      const valorSalario = parseFloat(document.getElementById('valorSalario').value);

      if (isNaN(valorSalario) ||!nomeConta || isNaN(valorConta) || valorConta <= 0 || !tipoConta) {
        alert('Por favor, insira um nome de conta válido e um valor positivo.');
        return;
      }

      contas.push({ nome: nomeConta, valor: valorConta, tipo: tipoConta, salario: valorSalario});
      atualizarListaContas();
      document.getElementById('nomeConta').value = '';
      document.getElementById('valorConta').value = '';
      document.getElementById('tipoConta').value = 'formaPagamento';
    }

    function atualizarListaContas() {
      const valorSalario = parseFloat(document.getElementById('valorSalario').value);
      const totalContas = contas.reduce((total, conta) => total + conta.valor, 0);
      if (totalContas >= valorSalario*0.8 && totalContas <= valorSalario){
        alert('O seu total de contas está tomando 80% do seu salário, cuidado!');
      } else if (valorSalario < totalContas) {
        alert('O total de contas excede o valor do seu salário');
      };
      
      const listaContas = document.getElementById('listaContas');
      listaContas.innerHTML = '';
      contas.forEach(conta => {
        const listItem = document.createElement('li');
        listItem.textContent = `${conta.nome}: R$ ${conta.valor} (${conta.tipo})`;
        listaContas.appendChild(listItem);
      });
      alert('Conta adicionada à lista.');
    }

    function calcularPorcentagem() {
      const salario = parseFloat(document.getElementById('valorSalario').value);
      const totalContas = contas.reduce((total, conta) => total + conta.valor, 0);
      const porcentagem = ((totalContas * 100) / salario).toFixed(2);
      document.getElementById('porcentagem').textContent = `As contas representam ${porcentagem}% do seu salário.`;
    }

    
    const wrapper = document.querySelector('.wrapper');
    const listaLink = document.querySelector('.listaLink');
    const analiseLink = document.querySelector('.analiseLink');
    const btnStart = document.querySelector('.btn-start');
    const inicioLink = document.querySelectorAll('.inicioLink');

    listaLink.addEventListener('click', ()=> {
      wrapper.classList.remove('analise');
      wrapper.classList.add('lista');
    });

    analiseLink.addEventListener('click', ()=> {
      wrapper.classList.remove('lista');
      wrapper.classList.add('analise');
    });

    function voltarInicio() {
      wrapper.classList.remove('analise');
      wrapper.classList.remove('lista');
    }

    inicioLink.forEach(function(start) {
      start.addEventListener('click', voltarInicio)
    })