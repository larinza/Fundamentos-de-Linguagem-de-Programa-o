# Tópico 5: Estruturas de Controle

## 1. Introdução às Estruturas de Controle

As estruturas de controle são construções da linguagem que permitem desviar o fluxo sequencial de execução de um programa, possibilitando a tomada de decisões, a repetição de blocos de código e a manipulação do fluxo de um loop. Elas são categorizadas principalmente em:

* **Estruturas de Seleção (ou Condicionais):** Permitem que um bloco de código seja executado (ou não) com base em uma condição. As mais comuns são `if`, `else if`/`elif` e `else`.
* **Estruturas de Repetição (ou Laços/Loops):** Permitem que um bloco de código seja executado múltiplas vezes, enquanto uma condição for verdadeira ou para cada item em uma sequência. Exemplos incluem `while` e `for`.
* **Estruturas de Controle de Fluxo (ou Saltos):** Alteram o fluxo normal de execução dentro de um loop ou de uma função. Exemplos incluem `break` (para sair de um loop) e `continue` (para pular para a próxima iteração do loop).

## 2. Implementação em Python: Menu Interativo Simples

O programa desenvolvido em Python (disponível em `05-estruturas-de-controle/menu_interativo.py`) oferece um menu com opções básicas. Ele ilustra como as diferentes estruturas de controle podem ser combinadas para criar uma aplicação funcional e interativa.

```python
while True:
    print("\n--- Menu Principal ---")
    print("1. Exibir Mensagem de Boas-Vindas")
    print("2. Calcular Quadrado de um Número")
    print("3. Sair do Programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        print("\nBem-vindo ao programa de demonstração!")
    elif opcao == '2':
        try:
            numero = float(input("Digite um número para calcular o quadrado: "))
            quadrado = numero ** 2
            print(f"O quadrado de {numero} é: {quadrado}")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    elif opcao == '3':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
