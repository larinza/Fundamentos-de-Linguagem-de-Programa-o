def analisar_lexicamente_shopsript(comando_shopsript):
    palavras_chave = [
        "INICIO", "FIM", "lista_compras", "adicionar_item", "remover_item",
        "adicionar_unidade", "decrementar_unidade", "marcar_pronto",
        "desmarcar_pronto", "lista_total_itens", "exibir_lista_compras",
        "exibir_lista_total_itens", "marcar_esgotado", "desmarcar_esgotado"
    ]
    delimitadores = ['(', ')', ',', ';']
    
    tokens_mapeados = {
        '(': 'DELIMITADOR_ABRE_PARENTESES',
        ')': 'DELIMITADOR_FECHA_PARENTESES',
        ',': 'DELIMITADOR_VIRGULA',
        ';': 'DELIMITADOR_PONTO_E_VIRGULA'
    }

    tokens = []
    
    for delim in delimitadores:
        comando_shopsript = comando_shopsript.replace(delim, f' {delim} ')
    
    partes = comando_shopsript.split()

    for parte in partes:
        if parte in palavras_chave:
            tokens.append((parte, f'PALAVRA_CHAVE_{parte.upper()}'))
        elif parte in tokens_mapeados:
            tokens.append((parte, tokens_mapeados[parte]))
        elif parte.startswith('"') and parte.endswith('"'):
            tokens.append((parte, 'LITERAL_TEXTO'))
        elif parte.isdigit():
            tokens.append((parte, 'NUMERO_INTEIRO'))
        else:
            tokens.append((parte, 'IDENTIFICADOR'))
            
    return tokens

comando_exemplo = 'adicionar_item ( "Pão", 1 ) ;'
tokens_analisados = analisar_lexicamente_shopsript(comando_exemplo)

print(f"Comando ShopScript: {comando_exemplo}")
print("Tokens Gerados:")
for lexema, token_tipo in tokens_analisados:
    print(f"  Lexema: '{lexema}' -> Token: '{token_tipo}'")

print("\n--- Outro exemplo ---")
comando_exemplo_2 = 'marcar_esgotado ( "Sabão" ) ;'
tokens_analisados_2 = analisar_lexicamente_shopsript(comando_exemplo_2)

print(f"Comando ShopScript: {comando_exemplo_2}")
print("Tokens Gerados:")
for lexema, token_tipo in tokens_analisados_2:
    print(f"  Lexema: '{lexema}' -> Token: '{token_tipo}'")
