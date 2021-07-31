from PySimpleGUI import PySimpleGUI as sg

class Tela:
    def __init__(self):
        sg.change_look_and_feel('DarkAmber')
        # Layout
        layout = [
            [sg.T(' '  * 50)],
            [sg.Text("Texto", size = (9,0), font=("Helvetica", 12, 'bold')), sg.Multiline(key='texto', size=(70, 10), font=("Helvetica", 12), no_scrollbar=True)],
            [sg.Text("Chave", size = (9,0), font=("Helvetica", 12, 'bold')), sg.Multiline(key='chave', size=(70, 2), font=("Helvetica", 12) , no_scrollbar=True)],
            [sg.T(' '  * 50) ,sg.Button("Encriptar",size = (10,0), font=("Helvetica", 12, 'bold')), sg.Button("Decriptar", size = (10,0), font=("Helvetica", 12, 'bold'))],
            [sg.Text("Resultado", size = (9,0), font=("Helvetica", 12, 'bold')), sg.Output(key = 'Resultado', size=(70, 10), font=("Helvetica", 12))]
        ]
        # Janela
        self.janela = sg.Window('RC4 Encrypt and Decrypt', size = (650, 450)).layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            plain_text = self.values['texto']
            key = self.values['chave']

            # print(f"Texto: {plain_text} e chave: {key}")

            if self.button == sg.WINDOW_CLOSED:
                break



tela = Tela()
tela.Iniciar()

