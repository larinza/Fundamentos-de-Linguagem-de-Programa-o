#include <stdio.h>

int fatorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } 
    else {
        return n * fatorial(n - 1);
    }
}

int main() {
    int numero_teste = 5;
    int resultado;

    printf("--- Implementacao de Subprograma Recursivo (Fatorial) ---\n");

    resultado = fatorial(numero_teste);
    printf("O fatorial de %d e: %d\n", numero_teste, resultado);

    numero_teste = 0;
    resultado = fatorial(numero_teste);
    printf("O fatorial de %d e: %d\n", numero_teste, resultado);

    numero_teste = 7;
    resultado = fatorial(numero_teste);
    printf("O fatorial de %d e: %d\n", numero_teste, resultado);

    return 0;
}
