class Velha:
    def __init__(self):
        del self.placar
        self.inicio()



    @property
    def ganhador(self):
        return self.__ganhador, self.__linha, # self.__ultimo_ganhador

    @ganhador.setter
    def ganhador(self, variavel):
        self.set_placar = variavel[0]
        self.__ganhador = variavel[0]
        # self.__ultimo_ganhador = variavel[0]
        self.__linha = variavel[1]

    @ganhador.deleter
    def ganhador(self):
        self.__ganhador = None
        self.__linha = ""
        
    @property
    def tabuleiro(self):
        return self.__tabuleiro

    @tabuleiro.setter
    def tabuleiro(self, lista):
        self.__tabuleiro = lista

    @property
    def pecas(self):
        return self.__pecas

    @pecas.setter
    def pecas(self, lista):
        self.__pecas = lista

    @property
    def resultado_jogo(self):
        if self.is_jogo_play:
            if len(self.pecas) >= 0 and len(self.pecas) <= 4:
                # Verificando por linha
                for i in range(3):
                    if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != None:
                        self.ganhador = (self.tabuleiro[i][0], f"L{i}")
                        self.fim_do_jogo()
                        return self.ganhador
                # Verificando por coluna
                for i in range(3):
                    if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != None:
                        self.ganhador = (self.tabuleiro[0][i], f"C{i}")
                        self.fim_do_jogo()
                        return self.ganhador
                # Verificando por diagonal
                if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != None or \
                   self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != None:
                    self.ganhador = (self.tabuleiro[1][1],
                                "D0" if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] else "D2")
                    self.fim_do_jogo()
                    return self.ganhador
            if len(self.pecas) == 0:
                self.ganhador = ("Empate", "  ")
                self.fim_do_jogo()
                return self.ganhador
        return self.ganhador

    @property
    def is_jogo_play(self):
        return self.__is_jogo_play

    @is_jogo_play.setter
    def is_jogo_play(self, variavel):
        self.__is_jogo_play = variavel

    @is_jogo_play.deleter
    def is_jogo_play(self):
        self.is_jogo_play = True
    
    @property
    def placar(self):
        return self.__placar

    @placar.setter
    def placar(self, dicionario):
        self.__placar = dicionario

    @placar.setter
    def set_placar(self, ganhador):        
        if ganhador == "Empate":
            self.__placar["X"] += 0.5
            self.__placar["O"] += 0.5
            self.__placar[ganhador] += 1
            self.__placar["Inicio Partida"] = "X" if self.__placar["Inicio Partida"] == "O" else "O"
        else:
            self.__placar[ganhador] += 1
            self.__placar["Inicio Partida"] = ganhador

    @placar.deleter
    def placar(self):
        self.__placar = {"Empate" : 0,
                         "X" : 0,
                         "O" : 0,
                         "Inicio Partida" : "X"}
    
    
    def inicio(self):
        del self.is_jogo_play
        del self.ganhador
        parinpar = 0 if self.placar["Inicio Partida"] == "X" else 1
        self.tabuleiro = [ [None for _ in range(3)] for _ in range(3)]
        self.pecas = ["X" if (i + parinpar) % 2 == 0 else "O" for i in range(9)]

    def fim_do_jogo(self):
        self.is_jogo_play = False    

    def jogo(self,x,y):
        if self.is_jogo_play and not self.tabuleiro[x][y]:
            self.tabuleiro[x][y] = self.pecas.pop()
            self.resultado_jogo
    
    def __str__(self):
        texto = f"""
{'-'*10}

Ganahdor: {self.ganhador}
Placar: {self.placar}
"""
        for i in self.tabuleiro:
            for j in i:
                texto = texto + f'{j if j else "."} '
            texto = texto + "\n"
        return texto.strip()


if __name__ == "__main__":
    import random
    v = Velha()
   # listas_jogos = [
   #     [["X","X","X"],[None, None, None],[None, None, None]],
   #     [[None, None, None],["X","X","X"],[None, None, None]],
   #     [[None, None, None],[None, None, None],["X","X","X"]],
   #
   #     [["X", None, None],["X", None, None],["X", None, None]],
   #     [[None, "X", None],[None, "X", None],[None, "X", None]],
   #     [[None, None, "X"],[None, None, "X"],[None, None, "X"]],
   #
   #     [["X", None, None],[None, "X", None],[None, None, "X"]],
   #     [[None, None, "X"],[None, "X", None],["X", None, None]],
   #
   #     [["O","O","O"],[None, None, None],[None, None, None]],
   #     [[None, None, None],["O","O","O"],[None, None, None]],
   #     [[None, None, None],[None, None, None],["O","O","O"]],
   #
   #     [["O", None, None],["O", None, None],["O", None, None]],
   #     [[None, "O", None],[None, "O", None],[None, "O", None]],
   #     [[None, None, "O"],[None, None, "O"],[None, None, "O"]],
   #
   #     [["O", None, None],[None, "O", None],[None, None, "O"]],
   #     [[None, None, "O"],[None, "O", None],["O", None, None]]
   #     ]
   # for jogos in listas_jogos:
   #     v.tabuleiro = jogos
   #     print("-"*10)
   #     print(f"Ganhador: {v.ganhador}\n")
   #     print(v)
   #     print("-"*10)
   #     print("\n"*2)
        
    

    for i in range(5000):
        v.inicio()
        jogo = [[x,y] for x in range(3) for y in range(3)]
        random.shuffle(jogo)
        while v.is_jogo_play:
            v.jogo(*jogo.pop())
        
       # print("-"*10)
       # print(f"jogo Numero: {i+1}")
       # print(f"Ganhador: {v.ganhador}\n")
       # print(v)
       # print(f"\n{v.placar}")
       #
       # print("-"*10+"\n"*2)
       # if v.ganhador == "Empate":
       #     pass
       #     #input()
        
    print(v)        
    
    
