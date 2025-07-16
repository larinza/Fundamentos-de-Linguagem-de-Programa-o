# 11 - Programação Funcional

## 2. Conceitos da Programação Funcional

* **Funções de Alta Ordem:** São funções que podem receber outras funções como argumentos, retornar funções como resultado, ou ambas. Elas são um pilar da programação funcional, permitindo a criação de abstrações poderosas e código mais flexível. Exemplos comuns incluem `map`, `filter` e `reduce`.
* **Recursão:** Na programação funcional, a recursão é a abordagem preferida para iteração, em vez de loops imperativos. Uma função recursiva resolve um problema chamando a si mesma com uma versão menor do problema até que um caso base seja atingido.
* **Imutabilidade:** O ideal é que os dados não sejam alterados após sua criação. Em vez de modificar uma estrutura de dados existente, funções funcionais geralmente retornam uma nova estrutura de dados com as modificações desejadas.
* **Funções Puras:** Funções que, dados os mesmos argumentos, sempre retornam o mesmo resultado e não produzem efeitos colaterais (não modificam estados fora de seu escopo).

## Implementação de Exemplo (Python)

Para demonstrar a Programação Funcional, foi implementado um exemplo em Python para calcular a **soma dos quadrados de uma lista de números inteiros**.

* **Função de Alta Ordem (`aplicar_funcao_a_lista` com `map`):** A função `aplicar_funcao_a_lista` recebe uma função (`quadrado`) e uma lista como argumentos, aplicando a função `quadrado` a cada elemento da lista `numeros` e retornando uma nova lista de quadrados. Isso demonstra o uso de `map`, uma função de alta ordem em Python, encapsulada para clareza.
* **Recursão (`somar_lista_recursivamente`):** A soma dos elementos da lista de quadrados é realizada por uma função recursiva `somar_lista_recursivamente`. Ela verifica se a lista está vazia (caso base) e, caso contrário, soma o primeiro elemento ao resultado da chamada recursiva com o restante da lista.
