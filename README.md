# 4-em-linha-jogo
Jogo criado para fins didáticos

# ♟️ Quatro em Linha

Um simples jogo de "Quatro em Linha" (Connect Four) criado em Python. O jogador pode escolher entre diferentes modos de jogo e testar suas habilidades contra uma IA ou contra um amigo.

## 🌟 Funcionalidades

-   **Modo Jogador vs. Jogador:** Desafie um amigo para uma partida no mesmo computador.
-   **Modo Jogador vs. IA:** Teste suas habilidades contra uma Inteligência Artificial estratégica. A IA tenta vencer, defender e, por último, joga aleatoriamente.
-   **Interface de Linha de Comando:** Totalmente jogável no terminal, mantendo o jogo leve e acessível.
-   **Validação de Jogadas:** O jogo valida a entrada de colunas, garantindo que apenas jogadas válidas sejam aceitas.
-   **Sair a Qualquer Momento:** Digite `--sair` para encerrar o programa a qualquer momento.

## 🚀 Como Jogar

Siga estes passos simples para rodar o jogo no seu computador.

### Requisitos

Você só precisa ter o Python 3 instalado no seu sistema.

### Executar o Script

1.  Abra seu terminal ou prompt de comando.
2.  Navegue até o diretório onde o arquivo do jogo está salvo.
3.  Execute o seguinte comando:

```bash
python seu_script.py

(Substitua seu_script.py pelo nome do arquivo principal do seu jogo).

Instruções do Jogo

Ao iniciar o jogo, você será perguntado qual modo de jogo deseja jogar. Depois, siga as instruções na tela para inserir os nomes e os símbolos dos jogadores. O objetivo é simples: ser o primeiro a conseguir quatro fichas em linha, seja na horizontal, vertical ou diagonal.

🛠️ Estrutura do Código

    encerra_jogo(): Uma função que encerra o programa caso o usuário digite --sair.

    limpa(): Uma função utilitária para limpar a tela do terminal e manter a interface organizada.

    Tabuleiro (Classe): A classe que representa o tabuleiro do jogo, gerenciando suas células, combinações vencedoras e o estado atual.

    Jogadores (Classe): A classe que lida com a criação e o gerenciamento dos jogadores, incluindo o modo IA e as jogadas humanas.

    Jogo (Classe): A classe principal que orquestra todo o fluxo do jogo, desde a seleção de modo até o loop da partida.

🤝 Contribuições

Sinta-se à vontade para abrir um issue para relatar bugs ou sugerir melhorias, ou submeter um pull request com suas próprias alterações. Toda contribuição é bem-vinda!
