class TarefaConcorrente implements Runnable {
    private String nomeTarefa;
    private int limiteContagem;

    public TarefaConcorrente(String nomeTarefa, int limiteContagem) {
        this.nomeTarefa = nomeTarefa;
        this.limiteContagem = limiteContagem;
    }

    @Override
    public void run() {
        System.out.println("Tarefa " + nomeTarefa + " iniciada.");
        for (int i = 1; i <= limiteContagem; i++) {
            System.out.println("Tarefa " + nomeTarefa + ": Contagem " + i);
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                System.out.println("Tarefa " + nomeTarefa + " foi interrompida.");
                Thread.currentThread().interrupt();
                return;
            }
        }
        System.out.println("Tarefa " + nomeTarefa + " concluída.");
    }
}

public class ExemploConcorrencia {
    public static void main(String[] args) {
        System.out.println("--- Exemplo de Concorrencia com Threads em Java ---");

        Thread thread1 = new Thread(new TarefaConcorrente("A", 5));
        Thread thread2 = new Thread(new TarefaConcorrente("B", 7));
        Thread thread3 = new Thread(new TarefaConcorrente("C", 4));

        thread1.start();
        thread2.start();
        thread3.start();

        try {
            thread1.join();
            thread2.join();
            thread3.join();
        } catch (InterruptedException e) {
            System.out.println("Thread principal interrompida enquanto esperava.");
            Thread.currentThread().interrupt();
        }

        System.out.println("Todas as tarefas foram concluidas na thread principal.");
    }
}
