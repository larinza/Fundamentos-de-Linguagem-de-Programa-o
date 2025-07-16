class Livro {
    String titulo;
    String autor;
    int anoPublicacao;

    public Livro(String titulo, String autor, int anoPublicacao) {
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    public void exibirDetalhes() {
        System.out.println("--- Detalhes do Livro ---");
        System.out.println("Titulo: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Ano de Publicacao: " + anoPublicacao);
    }
}

class LivroFisico extends Livro {
    int numeroPaginas;
    double pesoKG;

    public LivroFisico(String titulo, String autor, int anoPublicacao, int numeroPaginas, double pesoKG) {
        super(titulo, autor, anoPublicacao);
        this.numeroPaginas = numeroPaginas;
        this.pesoKG = pesoKG;
    }

    public int getNumeroPaginas() {
        return numeroPaginas;
    }

    public double getPesoKG() {
        return pesoKG;
    }

    @Override
    public void exibirDetalhes() {
        super.exibirDetalhes();
        System.out.println("Tipo: Fisico");
        System.out.println("Numero de Paginas: " + numeroPaginas);
        System.out.println("Peso: " + pesoKG + " KG");
    }
}

class LivroDigital extends Livro {
    double tamanhoArquivoMB;
    String formato;

    public LivroDigital(String titulo, String autor, int anoPublicacao, double tamanhoArquivoMB, String formato) {
        super(titulo, autor, anoPublicacao);
        this.tamanhoArquivoMB = tamanhoArquivoMB;
        this.formato = formato;
    }

    public double getTamanhoArquivoMB() {
        return tamanhoArquivoMB;
    }

    public String getFormato() {
        return formato;
    }

    @Override
    public void exibirDetalhes() {
        super.exibirDetalhes();
        System.out.println("Tipo: Digital");
        System.out.println("Tamanho do Arquivo: " + tamanhoArquivoMB + " MB");
        System.out.println("Formato: " + formato);
    }
}

public class GerenciadorLivros {
    public static void main(String[] args) {
        Livro livroGenerico = new Livro("Aventuras de um Programador", "Ada Lovelace", 2023);
        LivroFisico livroFisico = new LivroFisico("O Código Limpo", "Robert C. Martin", 2008, 464, 0.7);
        LivroDigital livroDigital = new LivroDigital("Design Patterns", "Erich Gamma et al.", 1994, 25.5, "PDF");

        System.out.println("--- Livro Generico ---");
        livroGenerico.exibirDetalhes();
        System.out.println("\n");

        System.out.println("--- Livro Fisico ---");
        livroFisico.exibirDetalhes();
        System.out.println("\n");

        System.out.println("--- Livro Digital ---");
        livroDigital.exibirDetalhes();
        System.out.println("\n");
    }
}
