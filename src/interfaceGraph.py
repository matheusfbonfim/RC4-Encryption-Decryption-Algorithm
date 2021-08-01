from PySimpleGUI import PySimpleGUI as sg
from RC4 import RC4Encrypt, RC4Decrypt

class Tela:
    def __init__(self):
        # Tema - Tela
        sg.change_look_and_feel('DarkAmber')
        # Layout
        layout = [
            [sg.T(' '  * 50)],
            [sg.Text("Texto", size = (9,0), font=("Helvetica", 12, 'bold')), sg.Multiline(key='texto', size=(70, 10), font=("Helvetica", 12), no_scrollbar=True)],
            [sg.Text("Chave", size = (9,0), font=("Helvetica", 12, 'bold')), sg.Multiline(key='chave', size=(70, 2), font=("Helvetica", 12) , no_scrollbar=True)],
            [sg.T(' '  * 50) ,sg.Button("Encriptar", key ="Encriptar",size = (10,0), font=("Helvetica", 12, 'bold')), sg.Button("Decriptar", size = (10,0), font=("Helvetica", 12, 'bold'))],
            [sg.Text("Resultado", size = (9,0), font=("Helvetica", 12, 'bold')), sg.Output(key = 'Resultado', size=(70, 10), font=("Helvetica", 12))]
        ]
        # Janela
        self.janela = sg.Window('RC4 Encrypt and Decrypt', size = (650, 450)).layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            text = self.values['texto']
            key = self.values['chave']

            if self.button == sg.WINDOW_CLOSED:
                break

            if self.button == "Encriptar":
                print("OLA")





tela = Tela()
tela.Iniciar()

