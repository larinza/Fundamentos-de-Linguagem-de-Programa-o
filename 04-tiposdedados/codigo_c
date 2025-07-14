#include <stdio.h>

int main() {
    float peso;
    float altura;
    float imc;

    printf("Digite seu peso em kg (ex: 70.5): ");
    scanf("%f", &peso);

    printf("Digite sua altura em metros (ex: 1.75): ");
    scanf("%f", &altura);

    imc = peso / (altura * altura);

    printf("Seu IMC é: %.2f\n", imc);

    if (imc < 18.5) {
        printf("Classificação: Abaixo do peso\n");
    } else if (imc < 24.9) {
        printf("Classificação: Peso normal\n");
    } else if (imc < 29.9) {
        printf("Classificação: Sobrepeso\n");
    } else {
        printf("Classificação: Obesidade\
");
    }

    return 0;
}
