import os
import shutil

def organizar_arquivos(diretorio_alvo):
    extensoes = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documentos': ['.doc', '.docx', '.txt', '.rtf', '.odt'],
        'PDFs': ['.pdf'],
        'Planilhas': ['.xls', '.xlsx', '.csv', '.ods'],
        'Apresentacoes': ['.ppt', '.pptx', '.odp'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Video': ['.mp4', '.mkv', '.avi', '.mov'],
        'Compactados': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Executaveis': ['.exe', '.msi', '.deb', '.rpm'],
        'Codigos': ['.py', '.java', '.c', '.cpp', '.html', '.css', '.js'],
        'Outros': []
    }

    print(f"Organizando arquivos em: {diretorio_alvo}")

    for pasta in extensoes.keys():
        caminho_pasta = os.path.join(diretorio_alvo, pasta)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)
            print(f"Criada pasta: {pasta}")

    for nome_arquivo in os.listdir(diretorio_alvo):
        if os.path.isfile(os.path.join(diretorio_alvo, nome_arquivo)):
            extensao_arquivo = os.path.splitext(nome_arquivo)[1].lower()
            destino = "Outros"

            for pasta, lista_extensoes in extensoes.items():
                if extensao_arquivo in lista_extensoes:
                    destino = pasta
                    break
            
            caminho_origem = os.path.join(diretorio_alvo, nome_arquivo)
            caminho_destino = os.path.join(diretorio_alvo, destino, nome_arquivo)

            if caminho_origem != caminho_destino:
                try:
                    shutil.move(caminho_origem, caminho_destino)
                    print(f"Movido: '{nome_arquivo}' para '{destino}/'")
                except shutil.Error as e:
                    print(f"Erro ao mover '{nome_arquivo}': {e}")
                except Exception as e:
                    print(f"Erro inesperado ao mover '{nome_arquivo}': {e}")
            else:
                print(f"Arquivo já na pasta correta ou é o proprio script: '{nome_arquivo}'")

if __name__ == "__main__":
    diretorio_para_organizar = os.getcwd()
    organizar_arquivos(diretorio_para_organizar)
    print("\nOrganizacao concluida!")
