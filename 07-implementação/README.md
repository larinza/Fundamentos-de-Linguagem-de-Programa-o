# 07 - Implementação de Subprogramas

## Recursão

A recursão é uma técnica onde uma função resolve um problema chamando a si mesma com instâncias menores do problema. É essencial que toda função recursiva possua:

* **Caso Base:** A condição de parada que encerra as chamadas recursivas.
* **Passo Recursivo:** Onde a função chama a si mesma com um argumento modificado, aproximando-se do caso base.

## Implementação em C: Fatorial Recursivo

Para ilustrar a recursão, foi implementado um subprograma em C para calcular o fatorial de um número.

O código de exemplo para este tópico está no arquivo: `07-implementacao-subprogramas/codigo_c.c`

A função `fatorial` em C demonstra:
* O **caso base** quando o número é 0 ou 1, retornando `1`.
* O **passo recursivo** calculando `n * fatorial(n - 1)`.
