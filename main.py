import PySimpleGUI as sg
from jogo import Velha

CORES_BUTTON = {
    'X': ("#8B0000", '#FFC0AC'),
    'O': ('#006400', '#BFFFAB'),
    None : ('#FFFFFF', '#283b5b')
}
CORES_BUTTON_WINNER ={
    'X': ("#FFFFFF", '#FF0000'),
    'O': ('#000000', '#008000'),
    None : ('#FFFFFF', '#283b5b')
}

def main():
    layout = [
        [sg.Text("Jogador da Vez: "), sg.Text("X", key="Jogador_Vez",font=(None,20))],
        [sg.Text("       Ganhador:"), sg.Text("",key="peca_ganhador")],
        [sg.Text("X: 0",key="X"),sg.Text(" "*10),sg.Text("O: 0",key="O")]]
    layout.append([[sg.Button(f"   ",key=f"{x}:{y}") for y in range(3)] for x in range(3)])
    layout.append([sg.Text(" "*6), sg.Button("Limpar")])
    return sg.Window("Inicio", layout=layout, finalize=True)

def atualizar():
    lista_janelas[0]["Jogador_Vez"].update(
        f'{jogo_velha.pecas[-1] if jogo_velha.pecas and jogo_velha.is_jogo_play else "-"}')
    lista_janelas[0]["X"].update(f'X: {jogo_velha.placar["X"]}')
    lista_janelas[0]["O"].update(f'O: {jogo_velha.placar["O"]}')
    lista_janelas[0]["peca_ganhador"].update(jogo_velha.ganhador[0] if jogo_velha.ganhador[0] else "")

    for x in range(3):
        for y in range(3):
            lista_janelas[0][f"{x}:{y}"].update(jogo_velha.tabuleiro[x][y] if jogo_velha.tabuleiro[x][y] else "  ")
            lista_janelas[0][f"{x}:{y}"].update(jogo_velha.tabuleiro[x][y] if jogo_velha.tabuleiro[x][y] else "  ",
                                                button_color=CORES_BUTTON[jogo_velha.tabuleiro[x][y]])

    if not jogo_velha.is_jogo_play:
        if jogo_velha.ganhador[1][0] == "L":
            for i in range(3):
                lista_janelas[0][f"{jogo_velha.ganhador[1][1]}:{i}"].update(
                    button_color=CORES_BUTTON_WINNER[jogo_velha.ganhador[0]])

        if jogo_velha.ganhador[1][0] == "C":
            for i in range(3):
                lista_janelas[0][f"{i}:{jogo_velha.ganhador[1][1]}"].update(
                    button_color=CORES_BUTTON_WINNER[jogo_velha.ganhador[0]])

        if jogo_velha.ganhador[1][0] == "D":
            if jogo_velha.ganhador[1][1] == "0":
                for x,y in zip(range(3),range(3)):
                    lista_janelas[0][f"{x}:{y}"].update(
                        button_color=CORES_BUTTON_WINNER[jogo_velha.ganhador[0]])
            else:
                for x,y in zip(range(2,-1,-1),range(3)):
                    lista_janelas[0][f"{x}:{y}"].update(
                        button_color=CORES_BUTTON_WINNER[jogo_velha.ganhador[0]])

jogo_velha = Velha()
lista_janelas = [main()]

while True:
    janela, evento, valores = sg.read_all_windows()

    atualizar()

    if janela == lista_janelas[0] and evento == sg.WIN_CLOSED:
        lista_janelas[0].close()
        break

    for x in range(3):
        for y in range(3):
            if janela == lista_janelas[0] and evento == f"{x}:{y}":
                jogo_velha.jogo(x,y)
                atualizar()

    if janela == lista_janelas[0] and evento == "Limpar":
        jogo_velha.inicio()
        atualizar()
        continue


