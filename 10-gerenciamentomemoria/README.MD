# 10 - Gerenciamento de Memória

## 2. Gerenciamento de Memória em C

Em C, o gerenciamento de memória é predominantemente **manual**. O programador tem controle direto e total sobre a alocação e desalocação de recursos na memória.

* **Alocação:** É realizada explicitamente por funções da biblioteca padrão, como `malloc()`, `calloc()` e `realloc()`, que reservam blocos de memória no `heap` (monte).
* **Desalocação:** Da mesma forma, a liberação da memória alocada no `heap` é responsabilidade exclusiva do programador, através da função `free()`.
* **Riscos:** Essa abordagem oferece alta performance e controle, mas é suscetível a erros comuns como vazamentos de memória (esquecer de liberar memória) e `dangling pointers` (acessar memória já liberada).

## 3. Gerenciamento de Memória em Java

Em Java, o gerenciamento de memória é em grande parte **automático**, abstraindo o desenvolvedor da complexidade de alocar e desalocar memória diretamente.

* **Alocação:** A alocação de objetos no `heap` é implícita e automática, ocorrendo sempre que um novo objeto é criado (usando a palavra-chave `new`).
* **Desalocação (Garbage Collection - GC):** A desalocação é feita por um processo automatizado conhecido como **Garbage Collector (GC)**. O GC identifica objetos que não são mais referenciados (inacessíveis pelo programa) e libera a memória que eles ocupam.
* **Benefícios:** Reduz significativamente o risco de vazamentos de memória e erros de acesso, simplificando o desenvolvimento.
* **Considerações:** Embora automático, o GC pode introduzir pausas (curtas, na maioria dos GCs modernos) na execução do programa para realizar a coleta de lixo.

## 4. Quadro Comparativo


| Característica              | C (Gerenciamento Manual: malloc/free)                                      | Java (Gerenciamento Automático: Garbage Collection)                                 |
| :-------------------------- | :---------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| **Método Principal de Alocação** |                                                                               |                                                                                      |
| **Método Principal de Desalocação** |                                                                               |                                                                                      |
| **Responsabilidade da Alocação/Desalocação** |                                                                               |                                                                                      |
| **Risco de Vazamentos de Memória** |                                                                               |                                                                                      |
| **Risco de Erros de Ponteiro/Acesso** |                                                                               |                                                                                      |
| **Controle do Programador** |                                                                               |                                                                                      |
| **Complexidade para o Desenvolvedor** |                                                                               |                                                                                      |
| **Impacto na Performance (Geral)** |                                                                               |                                                                                      |
| **Pausas na Execução** |                                                                               |                                                                                      |

## 5. Conclusão

A gestão de memória é uma área crítica em linguagens de programação, com abordagens que variam significativamente entre paradigmas e linguagens. A escolha entre o controle explícito de C e a automação de Java impacta diretamente a complexidade do código, a prevenção de erros e as características de desempenho do software. Compreender essas diferenças é essencial para tomar decisões de design e otimização eficazes.
