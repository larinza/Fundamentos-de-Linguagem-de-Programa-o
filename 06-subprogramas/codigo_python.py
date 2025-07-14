def incrementar_numero(num):
    num += 1
    print(f"Dentro da funcao (numero): valor de num = {num}")
    return num

def adicionar_item_lista(lista_param, item):
    lista_param.append(item)
    print(f"Dentro da funcao (lista): lista_param = {lista_param}")

def multiplicar(a, b):
    resultado = a * b
    return resultado

meu_valor_int = 10
minha_lista = [1, 2, 3]
valor_multiplicacao = 5
outro_valor_multiplicacao = 4
resultado_multiplicacao = 0

print("--- Demonstracao Passagem de Imutavel (Numero) ---")
print(f"Antes da funcao: meu_valor_int = {meu_valor_int}")
meu_valor_int = incrementar_numero(meu_valor_int)
print(f"Depois da funcao (reatribuido): meu_valor_int = {meu_valor_int}\n")

print("--- Demonstracao Passagem de Mutavel (Lista) ---")
print(f"Antes da funcao: minha_lista = {minha_lista}")
adicionar_item_lista(minha_lista, 4)
print(f"Depois da funcao: minha_lista = {minha_lista} (mudou)\n")

print("--- Demonstracao Funcao com Retorno ---")
resultado_multiplicacao = multiplicar(valor_multiplicacao, outro_valor_multiplicacao)
print(f"{valor_multiplicacao} * {outro_valor_multiplicacao} = {resultado_multiplicacao}")
