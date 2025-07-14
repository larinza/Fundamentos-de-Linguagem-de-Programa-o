# 04 - Tipos de Dados

## Tipos de Dados e Sistemas de Tipagem

* **Tipagem Estática vs. Dinâmica:**
    * **Estática:** Tipos são verificados em tempo de **compilação**. Variáveis têm um tipo fixo definido antes da execução.
    * **Dinâmica:** Tipos são verificados em tempo de **execução**. O tipo de uma variável é associado ao valor que ela contém e pode mudar ao longo do programa.
* **Tipagem Forte vs. Fraca (ou Flexível):**
    * **Forte:** A linguagem é rigorosa com conversões de tipo. Conversões entre tipos incompatíveis geralmente requerem explicitação ou resultam em erro.
    * **Fraca/Flexível:** A linguagem tenta realizar conversões implícitas (coerção) automaticamente em muitas situações, o que pode levar a comportamentos menos previsíveis, mas mais "flexíveis".

## Comparativo Detalhado

### Declaração e Atribuição de Variáveis

* **C (Estática e Explícita):**
    * No `imc.c`, as variáveis são **declaradas com seu tipo fixo** antes de serem usadas: `float peso;`, `float altura;`, `float imc;`. O compilador exige essa declaração.
    * Ex: `float peso;` define `peso` como um número de ponto flutuante para toda a vida útil da variável. Tentar atribuir uma string a `peso` após sua declaração resultaria em um erro de compilação.
* **Python (Dinâmica e Implícita):**
    * No `imc.py`, não há declaração de tipo. O tipo da variável é **inferido dinamicamente** em tempo de execução com base no valor atribuído.
    * Ex: `peso = float(input(...))` — `peso` torna-se `float` porque `float()` retornou um float. Se depois fizéssemos `peso = "texto"`, `peso` se tornaria `string` sem erro.
* **JavaScript (Dinâmica e Implícita):**
    * Similar a Python, no `imc.js`, as variáveis são declaradas com `let` ou `const`, mas **sem tipo explícito**: `let pesoStr;`, `let alturaStr;`. O tipo também é inferido em tempo de execução.
    * Ex: `let peso = +pesoStr;` — `peso` é um `Number` após a conversão, mas poderia ser uma `String` se tivéssemos feito `peso = "abc";` sem erro.

**Resumo:** C exige a definição prévia do "molde" (tipo) da variável, enquanto Python e JavaScript moldam a variável de acordo com o que é colocado nela em tempo real.

### Entrada de Dados e Coerção de Tipos

* **C (Forte):**
    * No `imc.c`, a função `scanf()` exige um **especificador de formato** (`%f` para float) para ler a entrada do usuário e colocá-la no tipo correto da variável. Há uma expectativa explícita de tipo na leitura. Se o usuário digitar algo não numérico, o `scanf` falhará na conversão, mas não haverá coerção.
* **Python (Forte):**
    * No `imc.py`, `input()` sempre retorna uma `string`. Para usar a entrada como número no cálculo, a **conversão explícita** com `float()` é **obrigatória**: `peso = float(input(...))`. Tentar usar a `string` diretamente em operações numéricas causaria um `TypeError`.
* **JavaScript (Fraca/Flexível):**
    * No `imc.js`, a função `prompt()` (se usada) também retorna uma `string`. No entanto, a conversão para número pode ser feita de forma mais **implícita (coerção)**, como usando o operador unário `+`: `let peso = +pesoStr;`. JavaScript tenta "adivinhar" o tipo necessário na operação.
    * Essa flexibilidade pode levar a resultados inesperados, como `10 + "5"` resultando em `"105"` (concatenação de strings) em vez de `15` (soma numérica), porque o `+` opera como concatenação quando uma string está presente. No entanto, `10 - "5"` resultaria em `5`, pois o `-` força a conversão para número.

**Resumo:** C e Python exigem que você "diga" qual tipo você espera ou para qual tipo você quer converter. JavaScript, muitas vezes, "decide" por você, o que pode ser conveniente mas menos previsível.

### Operações Aritméticas e Detecção de Erros

* **C (Estática):**
    * Se você tentasse, por exemplo, somar uma `char` com um `struct` (tipos incompatíveis) em C, o **compilador apontaria o erro antes mesmo do programa rodar**. Isso garante que o programa só seja executado se as operações de tipo forem válidas.
    * Ex: `imc = peso / (altura * altura);` — todas as variáveis já foram verificadas como `float` pelo compilador.
* **Python (Dinâmica):**
    * No `imc.py`, se acidentalmente `peso` fosse uma `string` e `altura` um `float`, a operação `peso / (altura ** 2)` **só falharia em tempo de execução**, resultando em um `TypeError`.
    * Apesar de dinâmico, Python é forte; ele *não* tenta operações sem sentido.
* **JavaScript (Dinâmica e Fraca):**
    * No `imc.js`, a detecção de erros de tipo também ocorre em **tempo de execução**. No entanto, devido à coerção, JavaScript pode "tentar" uma operação mesmo com tipos diferentes. `let result = "abc" / 2;` não causaria um erro, mas sim `result` seria `NaN` (Not a Number), um valor que indica uma operação numérica inválida. Isso pode ser mais difícil de depurar do que um `TypeError` explícito.

**Resumo:** C detecta problemas de tipo cedo (compilação), enquanto Python e JavaScript detectam em tempo de execução. JavaScript é mais "permissivo" na execução, podendo resultar em `NaN` ou conversões inesperadas em vez de erros imediatos.
