while True:
    print("\n--- Menu Principal ---")
    print("1. Exibir Mensagem de Boas-Vindas")
    print("2. Calcular Quadrado de um Número")
    print("3. Sair do Programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        print("\nBem-vindo ao programa de demonstração!")
    elif opcao == '2':
        try:
            numero = float(input("Digite um número para calcular o quadrado: "))
            quadrado = numero ** 2
            print(f"O quadrado de {numero} é: {quadrado}")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    elif opcao == '3':
        print("Saindo do programa. Até logo!")
        break # Sai do loop while, encerrando o programa
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
