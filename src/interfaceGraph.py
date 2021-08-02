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
            [sg.T(' '  * 50) ,sg.Button("Encriptar", key ="Encriptar",size = (10,0), font=("Helvetica", 12, 'bold')), sg.Button("Decriptar", key ="Decriptar",size = (10,0), font=("Helvetica", 12, 'bold'))],
            [sg.Text("Resultado", size = (9,0), font=("Helvetica", 12, 'bold')), sg.Output(key = 'Resultado', size=(70, 10), font=("Helvetica", 12))]
        ]
        # Janela
        self.janela = sg.Window('RC4 Encrypt and Decrypt', size = (650, 450)).layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            if self.button == sg.WINDOW_CLOSED:
                break

            if self.button == "Encriptar":
                # Limpar a tela
                self.janela.FindElement('Resultado').Update('')

                # Recebendo valor do texto escrito
                text_aux = self.values['texto']
                text = text_aux[:-1] # Removendo o '\n'

                # Recebendo valor da chave
                key_aux = self.values['chave']
                key = key_aux[:-1] # Removendo o '\n'

                # print(f"Tipo: {type(text)} e texto: {text} ")
                rc4 = RC4Encrypt(text, key)
                cipher_text = rc4.encrypt()

                cipher_list = str(cipher_text)  # Transforma para string
                cipher_string = cipher_list[2:len(cipher_list) - 2:1]  # Retira os ['']

                # Imprimir resultado - Texto encriptado
                print(cipher_string, end='')

            if self.button == "Decriptar":
                # Limpar a tela
                self.janela.FindElement('Resultado').Update('')

                # Recebendo valor do texto escrito
                text_aux = self.values['texto']
                text = text_aux[:-1]  # Removendo o '\n'

                # Recebendo valor da chave
                key_aux = self.values['chave']
                key = key_aux[:-1]  # Removendo o '\n'

                print(f"Decifrar: {text} com chave: {key}")

                rc4 = RC4Decrypt(f"{text}", f"{key}")
                plain_text = rc4.decrypt()

                # Imprimir resultado - Texto encriptado
                print(plain_text, end='')


tela = Tela()
tela.Iniciar()

