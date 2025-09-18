import os
import random
import sys
import time


def encerra_jogo(comando):
    if comando == '--sair':
        print('Programa encerrado')
        sys.exit(0)


def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')


class Tabuleiro:
    __combinacoes: list[list[int]]
    __lista_de_celulas: list[str]

    def __init__(self):
        self.__combinacoes = []
        self.__gera_combinacoes()
        self.__lista_de_celulas = ['   '] * 42

    @property
    def combinacoes(self):
        """Retorna a lista de combinações (getter)"""
        return self.__combinacoes

    @property
    def lista_de_celulas(self):
        """Retorna a lista de células (getter)"""
        return self.__lista_de_celulas

    def __gera_combinacoes(self):
        """Gera uma lista contendo listas com combinações gangadoras"""

        # HORIZONTAIS 24 combinações
        for v in range(6):
            for h in range(4):
                primeira_celula = v * 7 + h + 1
                self.__combinacoes.append(
                    [primeira_celula, primeira_celula + 1, primeira_celula + 2, primeira_celula + 3])

        # VERTICAIS 21 combinações
        for h in range(7):
            for v in range(3):
                primeira_celula = v * 7 + h + 1
                self.__combinacoes.append(
                    [primeira_celula, primeira_celula + 7, primeira_celula + 14, primeira_celula + 21])

        # DIAGONAIS descentes 12 combinações
        for v in range(3):
            for h in range(4):
                primeira_celula = v * 7 + h + 1
                self.__combinacoes.append(
                    [primeira_celula, primeira_celula + 8, primeira_celula + 16, primeira_celula + 24])

        # DIAGONAIS ascendentes 12
        for v in range(3, 6):
            for h in range(4):
                primeira_celula = v * 7 + h + 1
                self.__combinacoes.append(
                    [primeira_celula, primeira_celula - 6, primeira_celula - 12, primeira_celula - 18])

    def imprime_tabuleiro(self, jogador_1, simbolo_1, jogador_2, simbolo_2):
        """Imprime o tabuleiro atualizado"""
        limpa()
        print('|---|--- 4 EM LINHA |---|---|\n')
        print(f'JOGADOR 1: {jogador_1} = {simbolo_1}')
        print(f'JOGADOR 2: {jogador_2} = {simbolo_2}')
        print('-----------------------------\n')
        print('  1   2   3   4   5   6   7')
        print('|---|---|---|---|---|---|---|')
        for vertical_index in range(6):
            linha = '|'
            for horizontal_index in range(7):
                celula_index = vertical_index * 7 + horizontal_index
                ficha = self.__lista_de_celulas[celula_index]
                linha += ficha + '|'
            print(linha)
            print('|---|---|---|---|---|---|---|')
        print()

    def adiciona_jogada(self, coluna, simbolo, lista_temp):
        """Coloca a ficha do jogador na coluna especificada e na primeira célula de baixo para cima"""

        for h in range(5, -1, -1):
            celula = h * 7 + coluna
            if lista_temp[celula] == '   ':
                lista_temp[celula] = ' ' + simbolo + ' '
                return True
        return False

    def verifica_vitoria(self, simbolo, lista_temp):
        """Verifica se o jogador conseguiu 4 em linha"""

        combinacoes = self.__combinacoes

        for combinacao in combinacoes:
            ficha1 = lista_temp[combinacao[0] - 1]
            ficha2 = lista_temp[combinacao[1] - 1]
            ficha3 = lista_temp[combinacao[2] - 1]
            ficha4 = lista_temp[combinacao[3] - 1]
            if (ficha1 == ' ' + simbolo + ' ' and
                    ficha2 == ' ' + simbolo + ' ' and
                    ficha3 == ' ' + simbolo + ' ' and
                    ficha4 == ' ' + simbolo + ' '):
                return True
        return False

    def verifica_empate(self):
        """Verifica se o tabuleiro está cheio (empate)"""
        return '   ' not in self.__lista_de_celulas

    @property
    def colunas_disponiveis(self):
        """Retorna uma lista com as colunas disponíveis,
        ou seja, colunas que, o seu menor índice ainda esteja vazio"""
        colunas_disponiveis = [i for i in range(7) if self.__lista_de_celulas[i] == '   ']
        return colunas_disponiveis


class Jogadores:
    __jogador_1: str
    __jogador_2: str
    __simbolo_1: str
    __simbolo_2: str

    def __init__(self):
        pass

    @property
    def jogador_1(self):
        return self.__jogador_1

    @jogador_1.setter
    def jogador_1(self, nome):
        self.__jogador_1 = nome

    @property
    def simbolo_1(self):
        return self.__simbolo_1

    @simbolo_1.setter
    def simbolo_1(self, simbolo):
        self.__simbolo_1 = simbolo

    @property
    def jogador_2(self):
        return self.__jogador_2

    @jogador_2.setter
    def jogador_2(self, nome):
        self.__jogador_2 = nome

    @property
    def simbolo_2(self):
        return self.__simbolo_2

    @simbolo_2.setter
    def simbolo_2(self, simbolo):
        self.__simbolo_2 = simbolo

    def gera_jogadores(self, quantidade):
        jogadores = []
        simbolos = []
        for i in range(quantidade):
            limpa()
            jogadores.append(input(f'Nome do jogador {i + 1}\n>>>  '))
            encerra_jogo(jogadores[i])
            while True:
                simbolos.append(input(f'Símbolo de {jogadores[i]}\n>>> '))
                encerra_jogo(simbolos[i])
                if len(simbolos[i]) == 1 and simbolos[i] != ' ':
                    if quantidade == 2 and simbolos[1] == simbolos[0]:
                        print(f'{jogadores[1]} o caractere {simbolos[1]} já está em uso, digite outro')
                        continue
                    break
                print('Digite apenas 1 caractere')

        if quantidade == 1:
            self.__jogador_1 = jogadores[0]
            self.__simbolo_1 = simbolos[0]
            self.__jogador_2 = 'IA'
            lista_simbolo_ia = ['@', '#', '$', '&', '?']
            while True:
                simbolo_ia = random.choice(lista_simbolo_ia)
                if simbolo_ia != self.__simbolo_1:
                    self.__simbolo_2 = simbolo_ia
                    break
        if quantidade == 2:
            self.__jogador_1 = jogadores[0]
            self.__simbolo_1 = simbolos[0]
            self.__jogador_2 = jogadores[1]
            self.__simbolo_2 = simbolos[1]

    def jogada_humana(self, jogador, simbolo, colunas_disponiveis):
        """Gera uma jogada humana, testa se a entrada é integer e se é uma coluna válida"""

        while True:
            coluna = input(f'{jogador} --> ({simbolo}) escolha uma coluna\n>>> ')
            encerra_jogo(coluna)
            try:
                coluna = int(coluna)
                if 1 <= coluna <= 7 and coluna in colunas_disponiveis:
                    return coluna - 1
                else:
                    print('\aJogada inválida')
            except KeyboardInterrupt:
                print('\aDigite --sair para encerrar o jogo')
            except ValueError:
                print('\aDigite um número')

    def jogada_ia(self, tabuleiro, colunas_disponiveis):
        """Gera a jogada da IA. Prioridades: Ganhar ⇛ Defender ⇛ Aleatório"""

        # Simula um "pensamento" durante a jogada da IA
        # Caso não queira, pode ser comentada a póxima linha ou alterado o valor
        time.sleep(1)

        # Tenta ganhar
        for coluna in colunas_disponiveis:
            list_temp = list(tabuleiro.lista_de_celulas)
            if tabuleiro.adiciona_jogada(coluna, self.__simbolo_2, list_temp):
                if tabuleiro.verifica_vitoria(self.__simbolo_2, list_temp):
                    return coluna

        # Tenta defender
        for coluna in colunas_disponiveis:
            list_temp = list(tabuleiro.lista_de_celulas)
            if tabuleiro.adiciona_jogada(coluna, self.__simbolo_1, list_temp):
                if tabuleiro.verifica_vitoria(self.__simbolo_1, list_temp):
                    return coluna

        # JOgada aleatória
        return random.choice(colunas_disponiveis)


class Jogo:
    __tabuleiro: Tabuleiro
    __jogadores: Jogadores

    def __init__(self):
        self.__tabuleiro = Tabuleiro()
        self.__jogadores = Jogadores()

    def jogar(self):
        limpa()

        modo_ia = False
        while True: # "Loop" para iniciar os jogadores
            try:
                modo = input('Escolha o modo de jogo:\n1 - Jogador vs Jogador\n2 - Jogador vs IA\nSair = --sair\n>>> ')
                encerra_jogo(modo)
                if modo == '1': # Se o usuário escolhe a primeira opção, criamse 2 jogadores
                    self.__jogadores.gera_jogadores(2)
                    break
                if modo == '2': # Se o usuário escolhe a segunda opção, se cria 1 jogador e uma IA
                    self.__jogadores.gera_jogadores(1)
                    modo_ia = True
                    break
                else:
                    print('\nOpção inválida')
            except KeyboardInterrupt:
                print('\a\n--sair para sair')

        jogadores = [
            {'nome': self.__jogadores.jogador_1, 'simbolo': self.__jogadores.simbolo_1},
            {'nome': self.__jogadores.jogador_2, 'simbolo': self.__jogadores.simbolo_2}
        ]
        # Sorteio para escolher quem começa
        jogador_que_comeca = random.choice(jogadores)

        jogador_atual_nome = jogador_que_comeca['nome']
        jogador_atual_simbolo = jogador_que_comeca['simbolo']

        if jogador_atual_nome == self.__jogadores.jogador_1:
            jogador_oponente_nome = self.__jogadores.jogador_2
            jogador_oponente_simbolo = self.__jogadores.simbolo_2
        else:
            jogador_oponente_nome = self.__jogadores.jogador_1
            jogador_oponente_simbolo = self.__jogadores.simbolo_1

        print(f'{jogador_atual_nome} começa com {jogador_atual_simbolo}')

        time.sleep(2)

        while True:
            limpa()
            # Cria uma lista temporária do tabuleiro
            lista_temp = self.__tabuleiro.lista_de_celulas
            # Pasa os dados dos jogadores e imprime o tabuleiro
            self.__tabuleiro.imprime_tabuleiro(jogador_atual_nome, jogador_atual_simbolo, jogador_oponente_nome,
                                               jogador_oponente_simbolo)
            # Se a iA está a jogar e ela foi sorteada para começar a jogar, inicia
            if modo_ia and jogador_atual_nome == 'IA':
                print(f"Turno da {jogador_atual_nome} ({jogador_atual_simbolo})...")
                coluna_escolhida = self.__jogadores.jogada_ia(self.__tabuleiro, self.__tabuleiro.colunas_disponiveis)
            else:
                coluna_escolhida = self.__jogadores.jogada_humana(jogador_atual_nome, jogador_atual_simbolo,
                                                                  self.__tabuleiro.colunas_disponiveis)
                encerra_jogo(coluna_escolhida)
            # Temta adicionar uma jogada
            if self.__tabuleiro.adiciona_jogada(coluna_escolhida, jogador_atual_simbolo, lista_temp):
                # Se a jogada foi adicionada, verifica se o jogador venceu o jogo
                if self.__tabuleiro.verifica_vitoria(jogador_atual_simbolo, lista_temp):
                    self.__tabuleiro.imprime_tabuleiro(jogador_atual_nome, jogador_atual_simbolo, jogador_oponente_nome,
                                                       jogador_oponente_simbolo)
                    print(f'O jogador {jogador_atual_nome} ganhou!!!')
                    break
                # Verifica se ocorreu um empate
                elif self.__tabuleiro.verifica_empate():
                    self.__tabuleiro.imprime_tabuleiro(jogador_atual_nome, jogador_atual_simbolo, jogador_oponente_nome,
                                                       jogador_oponente_simbolo)
                    print('O jogo terminou em empate!!!')
                    break
                else:
                    # Troca de jogador
                    jogador_atual_nome, jogador_oponente_nome = jogador_oponente_nome, jogador_atual_nome
                    jogador_atual_simbolo, jogador_oponente_simbolo = jogador_oponente_simbolo, jogador_atual_simbolo

        print('\nFim do jogo!')
        input('Presione ENTER para sair...')


if __name__ == '__main__':
    jogo = Jogo()
    jogo.jogar()
