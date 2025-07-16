import functools

def aplicar_funcao_a_lista(funcao, lista):
    return list(map(funcao, lista))

def somar_lista_recursivamente(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somar_lista_recursivamente(lista[1:])

def quadrado(numero):
    return numero * numero

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    print(f"Lista original: {numeros}")

    quadrados = aplicar_funcao_a_lista(quadrado, numeros)
    print(f"Quadrados dos numeros: {quadrados}")

    soma_dos_quadrados = somar_lista_recursivamente(quadrados)
    print(f"Soma dos quadrados (recursivamente): {soma_dos_quadrados}")
