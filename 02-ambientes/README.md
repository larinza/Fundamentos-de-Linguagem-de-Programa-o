# 02 - Ambientes de Programação

## Métodos de Implementação

Quase todas as linguagens de programação de alto nível são implementadas de três maneiras gerais: por compiladores, por interpretadores puros ou por um sistema híbrido de implementação. As linguagens de programação de baixo nível, assembler e de máquina, são implementadas por um interpretador e um sistema de carregamento, respectivamente.

### Compiladores

Programas traduzidos por um compilador são tipicamente executados muito mais rapidamente que os programas interpretados. Isso se deve a diversas razões: A principal delas é que o processo de tradução (compilação) de um programa de linguagem de alto nível (o programa-fonte) em código de máquina (o programa-objeto) é bastante complexo. Um compilador é um programa que traduz programas escritos em uma linguagem de alto nível em código de máquina. A fase inicial de um compilador é a análise lexical, depois, há a análise sintática. Para linguagens compiladas, a otimização de código é uma fase importante. O ambiente de programação para uma linguagem compilada geralmente inclui um linker, que é um programa que coleta um ou mais programas objeto compilados separadamente e os liga a outras partes do código de máquina, como arquivos de biblioteca. Os compiladores podem levar muito tempo para traduzir o código-fonte em um programa executável, o que pode ser uma desvantagem significativa quando se está desenvolvendo e testando um novo programa.

### Interpretadores Puros

Interpretadores puros não são tão rápidos quanto os compiladores. Programas interpretados, no entanto, podem ser executados imediatamente, sem a demora da compilação. A grande vantagem da abordagem de interpretação pura é a sua flexibilidade. A depuração de programas é mais fácil com um interpretador puro, pois quando um erro é detectado, a execução pode ser interrompida, o programa modificado e a execução continuada imediatamente. A interpretação pura oferece um grau de portabilidade, mas geralmente é implementada sobre os códigos de máquina da arquitetura de hardware em que o interpretador está sendo executado.

### Sistemas Híbridos de Implementação

Sistemas de implementação híbridos são um compromisso entre compiladores e interpretadores puros. Eles traduzem programas de linguagem de alto nível para uma linguagem intermediária de baixo nível, que é então interpretada. Essa linguagem intermediária, geralmente chamada de pseudocódigo, tem várias características que o tornam mais fácil de interpretar que um programa de linguagem de alto nível, resultando em uma execução muito mais rápida que a interpretação pura, mas ainda não tão rápido quanto os programas compilados. Perl, JavaScript e PHP utilizam sistemas híbridos.

## Ambientes de Programação

Um ambiente de programação é a coleção de ferramentas de software usadas no desenvolvimento de software.

* Os sistemas UNIX ou Linux fornecem uma vasta coleção de ferramentas, incluindo um editor, um compilador e um depurador, que podem ser usados através de uma interface de linha de comando. A interface da linha de comando, no entanto, é o ambiente para todas essas ferramentas.
* O ambiente do Microsoft Visual Studio contém compiladores para C++, C#, Visual Basic .NET e J#), e inclui ferramentas para design gráfico de interfaces de usuário, depuração e conexão com bancos de dados. Ele oferece uma única interface de usuário para todos esses recursos.
* Ambientes de programação mais recentes fornecem um único programa, chamado ambiente de desenvolvimento integrado (IDE), com o qual o usuário interage através de uma interface gráfica do usuário. O Mac OS X da Apple tem o Xcode como seu ambiente. IDEs estão se tornando o padrão para o desenvolvimento de software em muitas linguagens.
* O ambiente de programação para Java, para seu desenvolvimento inicial, foi um sistema de programação completo. O Java Development Kit (JDK) é o ambiente de desenvolvimento padrão para Java.

### Máquinas Virtuais (Java Virtual Machine)

No caso do Java, o compilador Java, `javac`, traduz os programas Java para uma representação intermediária chamada *bytecode*. Esse "bytecode" é então interpretado pela JVM, o que permite que os programas Java sejam executados em qualquer máquina que tenha uma JVM instalada. Isso oferece uma solução para o problema de portabilidade: o bytecode Java pode ser enviado pela Internet e executado em qualquer máquina que tenha uma JVM instalada. A abordagem Java é um compromisso entre a compilação pura e a interpretação pura.
