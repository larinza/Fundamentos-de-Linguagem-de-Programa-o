# 13 - Linguagens para Scripts e Web

## Linguagens de Script

Linguagens de script, como Python, JavaScript, Ruby e Bash, são ferramentas poderosas que oferecem flexibilidade e rapidez no desenvolvimento. Suas principais aplicações incluem:

* **Automação de Tarefas:** Automatizar processos repetitivos em sistemas operacionais, como gerenciamento de arquivos, backups, instalação de softwares.
* **Desenvolvimento Web:** JavaScript (com Node.js para backend e diretamente no navegador para frontend) é a base da web moderna. Python com frameworks como Django/Flask também é popular para backend.
* **Manipulação de Dados:** Processamento de texto, análise de logs, conversão de formatos de dados.
* **Administração de Sistemas:** Criação de scripts para gerenciar servidores e redes.

## 3. Código Exemplo (Python)

Para demonstrar a capacidade de automação de scripts, foi desenvolvido um roteiro em Python que **organiza arquivos em um diretório**, movendo-os para subpastas baseadas em suas extensões de arquivo.

O script funciona da seguinte forma:

* Ele define um mapeamento de extensões de arquivo para categorias (ex: `.jpg` para `Imagens`, `.pdf` para `PDFs`).
* Percorre todos os arquivos no diretório alvo (definido para ser o diretório atual do script, mas pode ser configurado).
* Para cada arquivo, determina sua extensão e identifica a categoria correspondente.
* Cria as subpastas de categoria (se ainda não existirem).
* Move o arquivo para a subpasta apropriada. Arquivos com extensões desconhecidas são movidos para uma pasta "Outros".

Este script faz uso dos módulos embutidos do Python:
* `os`: Para interagir com o sistema operacional, como listar o conteúdo de diretórios e manipular caminhos de arquivos.
* `shutil`: Para operações de alto nível com arquivos, como mover (`shutil.move`) arquivos de um local para outro.
