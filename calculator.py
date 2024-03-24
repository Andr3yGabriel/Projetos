from functools import reduce

def somar():
    numeros = []
    num_soma = int(input("Digite quantos números você deseja somar: "))
    
    for numero in range(num_soma):
        numero = int(input("Digite um número para a soma: "))
        numeros.append(numero)
    
    resultado = sum(numeros)
    print(f"O resultado da adição é: {resultado}")
    
    return 

def subtrair():
    numeros = []
    num_subt = int(input("Digite quantos números você deseja subtrair: "))
    
    for numero in range(num_subt):
        numero = int(input("Digite um número para a subtração: "))
        numeros.append(numero)
    
    resultado = reduce(lambda x,y: x - y, numeros)
    print(f"O resultado da subtração é: {resultado}")
    
    return 
        
def multiplicar():
    numeros = []
    num_prod = int(input("Digite quantos números você deseja multiplicar: "))
    
    for numero in range(num_prod):
        numero = int(input("Digite um número para a multiplicação: "))
        numeros.append(numero)
        
    resultado = reduce(lambda x,y: x * y, numeros)
    print(f"O resultado da multiplicação é: {resultado}")
        
    return

def dividir():
    numeros = []
    num_div = int(input("Digite quantos números você deseja dividir: "))
    
    for numero in range(num_div):
        numero = int(input("Digite um número para a divisão: "))
        numeros.append(numero)
        
    resultado = reduce(lambda x,y: x / y, numeros)
    print(f"O resultado da divisão é: {resultado}")
        
    return

def main():
    while True:
        menu = """
        ----- Calculadora -----
        [+] Somar
        [-] Subtrair
        [/] Dividir
        [*] Multiplicar
        [s] Sair 
        
        Selecione qual operação deseja realizar
        ->
        """
        opcao = input(menu)
        
        if opcao == "+":
            somar()
            
        elif opcao == "-":
            subtrair()
            
        elif opcao == "*":
            multiplicar()
            
        elif opcao == "/":
            dividir()
            
        elif opcao == "s":
            print("Obrigado por usar a calculadora!")
            break
        
        else:
            print("Opção inválida!")

main()
