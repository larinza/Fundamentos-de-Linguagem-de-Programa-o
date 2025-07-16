
# 09 - Concorrência

## Threads e Processos

Embora ambos permitam a execução de tarefas independentes, threads e processos operam em níveis distintos:

* **Processo:** Uma instância independente de um programa em execução. Cada processo tem seu próprio espaço de memória isolado, recursos (como arquivos abertos, descritores de rede) e estado. A comunicação entre processos (IPC - Inter-Process Communication) é mais complexa e lenta.
* **Thread:** Uma unidade de execução dentro de um processo. Todas as threads de um mesmo processo compartilham o mesmo espaço de memória e a maioria dos recursos do processo. Isso torna a comunicação e a troca de dados entre threads mais rápidas e fáceis (mas também exige maior cuidado com sincronização para evitar problemas).

Processos oferecem isolamento total, enquanto threads oferecem maior eficiência para tarefas que precisam compartilhar dados e recursos dentro do mesmo programa.

## Implementação de Exemplo de Concorrência (Java)

Para demonstrar a concorrência, foi implementado um exemplo em Java utilizando **threads**. O código ilustra como múltiplas tarefas podem ser executadas concorrentemente.
