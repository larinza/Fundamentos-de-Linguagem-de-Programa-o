const prompt = require('prompt-sync')();

let pesoStr = prompt("Digite seu peso em kg (ex: 70.5): ");
let alturaStr = prompt("Digite sua altura em metros (ex: 1.75): ");

let peso = +pesoStr;
let altura = +alturaStr;

let imc = peso / (altura * altura);

console.log(`Seu IMC é: ${imc.toFixed(2)}`);

if (imc < 18.5) {
    console.log("Classificação: Abaixo do peso");
} else if (imc < 24.9) {
    console.log("Classificação: Peso normal");
} else if (imc < 29.9) {
    console.log("Classificação: Sobrepeso");
} else {
    console.log("Classificação: Obesidade");
}
