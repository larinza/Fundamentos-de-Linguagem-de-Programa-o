# Tópico 5: Estruturas de Controle

## Estruturas de Controle

* **Estruturas de Seleção (ou Condicionais):** Permitem que um bloco de código seja executado (ou não) com base em uma condição. As mais comuns são `if`, `else if`/`elif` e `else`.
* **Estruturas de Repetição (ou Laços/Loops):** Permitem que um bloco de código seja executado múltiplas vezes, enquanto uma condição for verdadeira ou para cada item em uma sequência. Exemplos incluem `while` e `for`.
* **Estruturas de Controle de Fluxo (ou Saltos):** Alteram o fluxo normal de execução dentro de um loop ou de uma função. Exemplos incluem `break` (para sair de um loop) e `continue` (para pular para a próxima iteração do loop).

### Estruturas de Controle no Código

* **Estrutura de Repetição (`while`):**
    * A linha `while True:` estabelece um loop infinito, garantindo que o menu seja exibido repetidamente e o programa continue a interagir com o usuário até que uma condição específica seja atendida para encerrá-lo.
* **Estruturas de Seleção (`if`, `elif`, `else`):**
    * Após o usuário digitar uma opção, uma série de instruções `if`, `elif` e `else` é utilizada para **selecionar qual bloco de código será executado** com base na `opcao` digitada.
    * `if opcao == '1':` : Executa o código para a Opção 1.
    * `elif opcao == '2':` : Se a primeira condição for falsa, verifica a Opção 2.
    * `elif opcao == '3':` : Se as anteriores forem falsas, verifica a Opção 3.
    * `else:` : Captura qualquer entrada que não corresponda às opções válidas.
* **Estrutura de Controle de Fluxo (`break`):**
    * Quando o usuário escolhe a opção '3' (`elif opcao == '3':`), a instrução `break` é utilizada. Esta instrução **interrompe imediatamente o loop `while`**, encerrando a execução do programa de forma controlada.
* **Tratamento de Exceções (`try`/`except`):**
    * Embora não seja uma estrutura de controle primária no sentido de seleção/repetição, o bloco `try-except` na opção '2' é um mecanismo de **controle de fluxo de erro**. Ele tenta executar um bloco de código e, se um `ValueError` ocorrer (por exemplo, se o usuário digitar texto em vez de um número), o fluxo é desviado para o bloco `except`, evitando que o programa trave.
