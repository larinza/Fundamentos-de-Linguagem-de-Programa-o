# 12 - Programação Lógica

## 2. Conceitos da Programação Lógica

* **Fatos (Facts):** São declarações de verdades básicas sobre o mundo. Representam informações atômicas e são os dados sobre os quais o programa opera. Em Prolog, são geralmente representados por predicados com argumentos (ex: `homem(joao)`).
* **Regras (Rules):** São declarações de inferência que permitem derivar novos fatos a partir de fatos existentes. Definem relacionamentos que são verdadeiros se certas condições forem satisfeitas. Em Prolog, uma regra tem a forma `Cabeça :- Corpo.`, onde `Cabeça` é verdadeiro se `Corpo` for verdadeiro.
* **Consultas (Queries):** São perguntas feitas ao sistema lógico. O interpretador Prolog tenta provar a consulta usando os fatos e regras disponíveis, retornando as variáveis que tornam a consulta verdadeira.
* **Unificação (Unification):** O mecanismo fundamental pelo qual Prolog casa termos e atribui valores a variáveis para satisfazer uma consulta.
* **Retrocesso (Backtracking):** O processo pelo qual Prolog explora diferentes caminhos para satisfazer uma consulta, voltando atrás e tentando alternativas quando um caminho falha.

## Código Exemplo (Prolog)

* **Fatos:**
    * `homem(Nome)` e `mulher(Nome)`: Definem o gênero de um indivíduo.
    * `pai(Pai, Filho)`: Define que `Pai` é o pai de `Filho`.
    * `mae(Mae, Filho)`: Define que `Mae` é a mãe de `Filho`.
    * São as verdades básicas sobre os membros da família e seus parentescos diretos.

* **Regras:**
    * `genitor(Genitor, Filho)`: Uma regra que generaliza `pai` e `mae`. Um `Genitor` é genitor de `Filho` se for `pai` ou `mae` de `Filho`.
    * `filho(Filho, Genitor)` e `filha(Filha, Genitor)`: Regras que invertem a relação de genitor e especificam o gênero do descendente.
    * `irmao(Irmao1, Irmao2)` e `irma(Irma1, Irma2)`: Regras que definem irmãos e irmãs com base em genitores comuns e gênero, evitando a comparação de um indivíduo consigo mesmo.
    * `tio(Tio, Sobrinho)` e `tia(Tia, Sobrinho)`: Regras para definir tio/tia com base na relação de irmandade com um dos genitores.
    * `avo(Avo, Neto)`: Uma regra que define avô/avó através de uma relação de genitor de genitor.
