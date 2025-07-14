# 06 - Subprogramas

## Subprogramas e Passagem de Parâmetros

Subprogramas são unidades de código que realizam tarefas específicas, promovendo reusabilidade. Eles interagem com o restante do programa através de:

* **Parâmetros (ou Argumentos):** Dados passados para o subprograma no momento da chamada.
* **Valor de Retorno:** O resultado que o subprograma pode enviar de volta ao chamador.

A **passagem de parâmetros** é crucial:
* **Por Valor:** Uma cópia do valor do argumento é usada. Alterações no parâmetro dentro do subprograma não afetam a variável original.
* **Por Referência:** O endereço de memória da variável original é passado. Isso permite que o subprograma modifique diretamente a variável original.

## Demonstração em C: 

A linguagem C permite uma distinção clara entre a passagem por valor e por referência, usando ponteiros.

### Funções e Passagem de Parâmetros em C

* **Passagem por Valor (`dobrar_por_valor`):** Uma função como `void dobrar_por_valor(int valor)` recebe uma **cópia** do argumento. Se a função alterar `valor`, a variável original no `main` permanece inalterada.
* **Passagem por Referência (`dobrar_por_referencia`):** Uma função como `void dobrar_por_referencia(int *ponteiro_para_valor)` recebe o **endereço de memória** da variável original (passado com `&` na chamada). Ao usar o operador de desreferência (`*`), a função modifica diretamente o conteúdo da variável original.
* **Valor de Retorno (`somar`):** A função `int somar(int a, int b)` realiza uma operação e usa `return resultado;` para enviar o resultado de volta ao chamador, que pode então armazená-lo em uma variável.

## 3. Demonstração em Python:

Python não tem passagem por valor ou por referência no mesmo sentido explícito de C. Ele usa um modelo de **"passagem por referência de objeto"** ou "passagem por atribuição de objeto". Uma referência ao objeto é sempre passada, e o comportamento (se o original é afetado ou não) depende da **mutabilidade** do objeto.

### Funções e Passagem de Parâmetros em Python

* **Tipos Imutáveis (e.g., números, strings - `incrementar_numero`):** Quando um objeto imutável é passado, se o subprograma tentar "alterá-lo" (e.g., `num += 1`), na verdade um *novo* objeto é criado, e a variável dentro da função passa a referenciar esse novo objeto. A variável original fora da função permanece inalterada, a menos que o valor retornado seja explicitamente reatribuído a ela.
* **Tipos Mutáveis (e.g., listas, dicionários - `adicionar_item_lista`):** Quando um objeto mutável é passado, o subprograma recebe uma referência para o *mesmo objeto*. Operações que modificam o objeto (e.g., `lista_param.append(item)`) afetam diretamente o objeto original, e as mudanças são visíveis fora da função.
* **Valor de Retorno (`multiplicar`):** A função `def multiplicar(a, b):` calcula um valor e usa `return resultado` para enviá-lo de volta ao chamador.
