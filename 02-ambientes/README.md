# Trabalho de Fundamentos de Linguagens de Programação

## Tópico 2: Ambientes de Programação

Este documento aborda o segundo tópico do trabalho de Fundamentos de Linguagens de Programação, focando nos conceitos de ambientes de programação, compiladores, interpretadores e máquinas virtuais, conforme a obra "Conceitos de Linguagens de Programação" de Robert W. Sebesta.

### 1.7 Métodos de Implementação

"Quase todas as linguagens de programação de alto nível são implementadas de três maneiras gerais: por compiladores, por interpretadores puros ou por um sistema híbrido de implementação" (Sebesta, p. 19). "As linguagens de programação de baixo nível, assembler e de máquina, são implementadas por um interpretador e um sistema de carregamento, respectivamente" (Sebesta, p. 19).

#### Compiladores

"Programas traduzidos por um compilador são tipicamente executados muito mais rapidamente que os programas interpretados" (Sebesta, p. 19). Isso se deve a diversas razões. "A principal delas é que o processo de tradução (compilação) de um programa de linguagem de alto nível (o programa-fonte) em código de máquina (o programa-objeto) é bastante complexo" (Sebesta, p. 19). "Um compilador é um programa que traduz programas escritos em uma linguagem de alto nível em código de máquina" (Sebesta, p. 19).

O processo de compilação envolve várias fases. Por exemplo, a "fase inicial de um compilador é a análise lexical" (Sebesta, p. 25). Depois, há a "análise sintática" (Sebesta, p. 26). "Para linguagens compiladas, a otimização de código é uma fase importante" (Sebesta, p. 27). O "ambiente de programação para uma linguagem compilada geralmente inclui um linker" (Sebesta, p. 19). O "linker é um programa que coleta um ou mais programas objeto compilados separadamente e os liga a outras partes do código de máquina, como arquivos de biblioteca" (Sebesta, p. 19-20). Os "compiladores podem levar muito tempo para traduzir o código-fonte em um programa executável" (Sebesta, p. 20), o que "pode ser uma desvantagem significativa quando se está desenvolvendo e testando um novo programa" (Sebesta, p. 20).

#### Interpretadores Puros

"Interpretadores puros não são tão rápidos quanto os compiladores" (Sebesta, p. 20). Programas interpretados, no entanto, "podem ser executados imediatamente" (Sebesta, p. 20), "sem a demora da compilação" (Sebesta, p. 20). "A grande vantagem da abordagem de interpretação pura é a sua flexibilidade" (Sebesta, p. 20). "A depuração de programas é mais fácil com um interpretador puro" (Sebesta, p. 20), pois "quando um erro é detectado, a execução pode ser interrompida, o programa modificado e a execução continuada imediatamente" (Sebesta, p. 20). A "interpretação pura oferece um grau de portabilidade, mas geralmente é implementada sobre os códigos de máquina da arquitetura de hardware em que o interpretador está sendo executado" (Sebesta, p. 20).

#### Sistemas Híbridos de Implementação

"Sistemas de implementação híbridos são um compromisso entre compiladores e interpretadores puros" (Sebesta, p. 20). Eles "traduzem programas de linguagem de alto nível para uma linguagem intermediária de baixo nível, que é então interpretada" (Sebesta, p. 20). Essa linguagem intermediária, "geralmente chamada de pseudocódigo" (Sebesta, p. 20), "tem várias características que o tornam mais fácil de interpretar que um programa de linguagem de alto nível" (Sebesta, p. 20), resultando em uma "execução muito mais rápida que a interpretação pura" (Sebesta, p. 20), mas "ainda não tão rápido quanto os programas compilados" (Sebesta, p. 20).

Como exemplos, "Perl, JavaScript e PHP utilizam sistemas híbridos" (Sebesta, p. 20).

### 1.8 Ambientes de Programação

"Um ambiente de programação é a coleção de ferramentas de software usadas no desenvolvimento de software" (Sebesta, p. 21).

* "Os sistemas UNIX ou Linux fornecem uma vasta coleção de ferramentas, incluindo um editor, um compilador e um depurador, que podem ser usados através de uma interface de linha de comando" (Sebesta, p. 21). "A interface da linha de comando, no entanto, é o ambiente para todas essas ferramentas" (Sebesta, p. 21).
* "O ambiente do Microsoft Visual Studio contém compiladores para C++, C#, Visual Basic .NET e J#" (Sebesta, p. 21), e "inclui ferramentas para design gráfico de interfaces de usuário, depuração e conexão com bancos de dados" (Sebesta, p. 21). Ele "oferece uma única interface de usuário para todos esses recursos" (Sebesta, p. 21).
* "Ambientes de programação mais recentes fornecem um único programa, chamado ambiente de desenvolvimento integrado (IDE), com o qual o usuário interage através de uma interface gráfica do usuário" (Sebesta, p. 21). "O Mac OS X da Apple tem o Xcode como seu ambiente" (Sebesta, p. 21). "IDEs estão se tornando o padrão para o desenvolvimento de software em muitas linguagens" (Sebesta, p. 22).
* "O ambiente de programação para Java, para seu desenvolvimento inicial, foi um sistema de programação completo" (Sebesta, p. 22). "O Java Development Kit (JDK) é o ambiente de desenvolvimento padrão para Java" (Sebesta, p. 22).

#### Máquinas Virtuais (Contexto da Java Virtual Machine)

O conceito de máquina virtual é exemplificado no livro pela "Máquina Virtual Java (JVM)" (Sebesta, p. 20). No caso do Java, o "compilador Java, `javac`, traduz os programas Java para uma representação intermediária chamada *bytecode*" (Sebesta, p. 20). Esse "bytecode" é então "interpretado pela JVM" (Sebesta, p. 20), o que "permite que os programas Java sejam executados em qualquer máquina que tenha uma JVM instalada" (Sebesta, p. 20). Isso "oferece uma solução para o problema de portabilidade: o bytecode Java pode ser enviado pela Internet e executado em qualquer máquina que tenha uma JVM instalada" (Sebesta, p. 20). A "abordagem Java é um compromisso entre a compilação pura e a interpretação pura" (Sebesta, p. 20).

---
*Referências:*
* Sebesta, Robert W. *Conceitos de Linguagens de Programação*. 9. ed. Porto Alegre: Bookman, 2011.
