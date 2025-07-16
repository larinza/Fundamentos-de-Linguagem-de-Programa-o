# 08 - Programação Orientada a Objetos

## Conceitos da POO

* **Encapsulamento:** O agrupamento de dados (atributos) e os métodos que operam sobre esses dados em uma única unidade (a classe), escondendo os detalhes internos da implementação e expondo apenas o necessário.
* **Herança:** Permite que uma classe (subclasse ou classe derivada) herde atributos e métodos de outra classe (superclasse ou classe base), promovendo a reutilização de código e a criação de hierarquias lógicas.
* **Polimorfismo:** A capacidade de objetos de diferentes classes responderem ao mesmo método de maneiras distintas, baseado em sua própria implementação. Isso é geralmente alcançado através da sobrescrita de métodos em classes derivadas.

## Modelagem da Hierarquia de Classes: Livros (Java)

Para este desafio, foi modelada uma hierarquia de classes no domínio de **Livros** utilizando Java, conforme a stack sugerida.

A hierarquia é composta por:

* **Classe Base: `Livro`**
    * Representa um livro genérico com atributos comuns a todos os livros: `titulo`, `autor` e `anoPublicacao`.
    * Possui um método `exibirDetalhes()` que mostra as informações básicas.

* **Classes Derivadas: `LivroFisico` e `LivroDigital`**
    * Ambas **herdam** de `Livro`, reutilizando seus atributos e comportamentos.
    * `LivroFisico` adiciona atributos específicos como `numeroPaginas` e `pesoKG`.
    * `LivroDigital` adiciona atributos específicos como `tamanhoArquivoMB` e `formato`.
    * Ambas **sobrescrevem** o método `exibirDetalhes()`, adicionando suas informações específicas ao que já é exibido pela classe `Livro`, demonstrando o **polimorfismo**.
