# 03 - Descrições Sintáticas e Semânticas

## 1. Sintaxe e Semântica

A **sintaxe** de uma linguagem de programação refere-se à sua forma, ou seja, as regras que determinam como os programas são estruturados. A **semântica**, por sua vez, diz respeito ao significado das construções da linguagem, ou seja, o que os programas realizam. A descrição precisa de ambos é crucial para o projeto, implementação e compreensão de qualquer linguagem.

## 2. Gramáticas e Análise Léxica

Linguagens de programação possuem uma estrutura hierárquica, que pode ser formalmente definida por **gramáticas**. Uma gramática especifica as regras para formar sentenças válidas. O processo de entender um programa começa com a **análise léxica**, que identifica os **lexemas** (unidades básicas como palavras-chave, identificadores, operadores) e os classifica em **tokens** (categorias dos lexemas). Em seguida, a **análise sintática** verifica se a sequência de tokens segue as regras gramaticais da linguagem.

## Minha Linguagem Fictícia: ShopScript

**Propósito:** `ShopScript` é uma linguagem de programação simplificada, projetada especificamente para auxiliar no gerenciamento de listas de compras e inventários domésticos. Ela permite ao usuário adicionar, remover, atualizar e visualizar itens, tanto na lista de compras ativa quanto em um inventário de itens da casa.

## Vocabulário (Lexemas e Tokens)

Os **lexemas** são as unidades sintáticas básicas de `ShopScript`, e os **tokens** são as categorias a que cada lexema pertence.

| Lexema            | Token                       | Categoria             |
| :---------------- | :-------------------------- | :-------------------- |
| `INICIO`          | `PALAVRA_CHAVE_INICIO`      | Palavra-chave         |
| `FIM`             | `PALAVRA_CHAVE_FIM`         | Palavra-chave         |
| `lista_compras`   | `PALAVRA_CHAVE_LISTA_COMPRAS`| Palavra-chave         |
| `adicionar_item`  | `PALAVRA_CHAVE_ADICIONAR_ITEM`| Palavra-chave         |
| `remover_item`    | `PALAVRA_CHAVE_REMOVER_ITEM`| Palavra-chave         |
| `adicionar_unidade`| `PALAVRA_CHAVE_ADICIONAR_UNIDADE`| Palavra-chave      |
| `decrementar_unidade`| `PALAVRA_CHAVE_DECREMENTAR_UNIDADE`| Palavra-chave   |
| `marcar_pronto`   | `PALAVRA_CHAVE_MARCAR_PRONTO`| Palavra-chave         |
| `desmarcar_pronto`| `PALAVRA_CHAVE_DESMARCAR_PRONTO`| Palavra-chave       |
| `lista_total_itens`| `PALAVRA_CHAVE_LISTA_TOTAL_ITENS`| Palavra-chave      |
| `exibir_lista_compras`| `PALAVRA_CHAVE_EXIBIR_LISTA_COMPRAS`| Palavra-chave |
| `exibir_lista_total_itens`|`PALAVRA_CHAVE_EXIBIR_LISTA_TOTAL_ITENS`| Palavra-chave|
| `marcar_esgotado` | `PALAVRA_CHAVE_MARCAR_ESGOTADO`| Palavra-chave       |
| `desmarcar_esgotado`| `PALAVRA_CHAVE_DESMARCAR_ESGOTADO`| Palavra-chave   |
| `(`             | `DELIMITADOR_ABRE_PARENTESES` | Delimitador           |
| `)`             | `DELIMITADOR_FECHA_PARENTESES`| Delimitador           |
| `,`             | `DELIMITADOR_VIRGULA`         | Delimitador           |
| `;`             | `DELIMITADOR_PONTO_E_VIRGULA` | Delimitador           |
| Qualquer texto entre aspas|"LITERAL_TEXTO"        | Literal               |
| Qualquer sequência de dígitos|"NUMERO_INTEIRO"       | Literal               |
| Uma sequência de letras/dígitos que não seja palavra-chave | `IDENTIFICADOR`| Identificador         |

## Mini-Gramática em BNF

```bnf
<programa>          ::= INICIO <lista_comandos> FIM

<lista_comandos>    ::= <comando> {<comando>}

<comando>           ::= <comando_lista_compras> ;
                      | <comando_lista_total_itens> ;
                      | <comando_exibicao> ;

<comando_lista_compras> ::= adicionar_item ( <literal_texto> , <numero_inteiro> )
                          | remover_item ( <literal_texto> )
                          | adicionar_unidade ( <literal_texto> , <numero_inteiro> )
                          | decrementar_unidade ( <literal_texto> , <numero_inteiro> )
                          | marcar_pronto ( <literal_texto> )
                          | desmarcar_pronto ( <literal_texto> )

<comando_lista_total_itens> ::= marcar_esgotado ( <literal_texto> )
                              | desmarcar_esgotado ( <literal_texto> )

<comando_exibicao>  ::= exibir_lista_compras ( )
                      | exibir_lista_total_itens ( )

## Pequeno exemplo para análise léxica

INICIO
  adicionar_item ( "Leite", 2 ) ;
  adicionar_item ( "Pão", 1 ) ;
  exibir_lista_compras ( ) ;
  marcar_pronto ( "Leite" ) ;
  marcar_esgotado ( "Sabão" ) ;
  exibir_lista_total_itens ( ) ;
FIM
 
## Análise Léxica

**Lexema**			**Token**
INICIO				PALAVRA_CHAVE_INICIO
adicionar_item			PALAVRA_CHAVE_ADICIONAR_ITEM
(				DELIMITADOR_ABRE_PARENTESES
"Leite"				LITERAL_TEXTO
,				DELIMITADOR_VIRGULA
2				NUMERO_INTEIRO
)				DELIMITADOR_FECHA_PARENTESES
;				DELIMITADOR_PONTO_E_VIRGULA
adicionar_item			PALAVRA_CHAVE_ADICIONAR_ITEM
(				DELIMITADOR_ABRE_PARENTESES
"Pão"				LITERAL_TEXTO
,				DELIMITADOR_VIRGULA
1				NUMERO_INTEIRO
)				DELIMITADOR_FECHA_PARENTESES
;				DELIMITADOR_PONTO_E_VIRGULA
exibir_lista_compras		PALAVRA_CHAVE_EXIBIR_LISTA_COMPRAS
(				DELIMITADOR_ABRE_PARENTESES
)				DELIMITADOR_FECHA_PARENTESES
;				DELIMITADOR_PONTO_E_VIRGULA
marcar_pronto			PALAVRA_CHAVE_MARCAR_PRONTO
(				DELIMITADOR_ABRE_PARENTESES
"Leite"				LITERAL_TEXTO
)				DELIMITADOR_FECHA_PARENTESES
;				DELIMITADOR_PONTO_E_VIRGULA
marcar_esgotado			PALAVRA_CHAVE_MARCAR_ESGOTADO
(				DELIMITADOR_ABRE_PARENTESES
"Sabão"				LITERAL_TEXTO
)				DELIMITADOR_FECHA_PARENTESES
;				DELIMITADOR_PONTO_E_VIRGULA
exibir_lista_total_itens	PALAVRA_CHAVE_EXIBIR_LISTA_TOTAL_ITENS
(				DELIMITADOR_ABRE_PARENTESES
)				DELIMITADOR_FECHA_PARENTESES
;				DELIMITADOR_PONTO_E_VIRGULA
FIM				PALAVRA_CHAVE_FIM

// Definições de terminais (não expandidos em BNF, definidos na análise lexical)
<literal_texto>     ::= "qualquer sequência de caracteres entre aspas duplas"
<numero_inteiro>    ::= digito {digito} // onde digito = 0 | 1 | ... | 9
