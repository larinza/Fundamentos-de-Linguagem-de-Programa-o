#include <stdio.h>

void dobrar_por_valor(int valor) {
    valor = valor * 2;
    printf("Dentro da funcao (por valor): o valor agora e %d\n", valor);
}

void dobrar_por_referencia(int *ponteiro_para_valor) {
    *ponteiro_para_valor = *ponteiro_para_valor * 2;
    printf("Dentro da funcao (por referencia): o valor agora e %d\n", *ponteiro_para_valor);
}

int somar(int a, int b) {
    int resultado = a + b;
    return resultado;
}

int main() {
    int meu_numero = 10;
    int outro_numero = 5;
    int resultado_soma;

    printf("--- Demonstracao Passagem por Valor ---\n");
    printf("Antes da funcao (por valor): meu_numero = %d\n", meu_numero);
    dobrar_por_valor(meu_numero);
    printf("Depois da funcao (por valor): meu_numero = %d (nao mudou)\n\n", meu_numero);

    printf("--- Demonstracao Passagem por Referencia ---\n");
    printf("Antes da funcao (por referencia): meu_numero = %d\n", meu_numero);
    dobrar_por_referencia(&meu_numero);
    printf("Depois da funcao (por referencia): meu_numero = %d (mudou)\n\n", meu_numero);

    printf("--- Demonstracao Funcao com Retorno ---\n");
    resultado_soma = somar(meu_numero, outro_numero);
    printf("%d + %d = %d\n", meu_numero, outro_numero, resultado_soma);

    return 0;
}
