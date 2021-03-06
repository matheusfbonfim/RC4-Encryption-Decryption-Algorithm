import base64

class RC4:
    def __init__(self):
        pass

    # ------------------------------------
    # Verificar se a chave é menor ou igual a 128 bits (128/8)
    def check_key_size(self, key):
        if (len(key) > 16):
            print("\n !! O comprimento da chave não pode ser superior a 128 bits !!")
            raise

    # ------------------------------------
    # Encode - String para Hexa
    def b64e(self, s):
        return base64.b64encode(s.encode()).decode()

    # ------------------------------------
    # Decode - Hex para string
    def b64d(self, s):
        return base64.b64decode(s).decode()

    ## ------------------------------------
    # Conversão do texto simples ou chave em ASCII
    def convert_string_in_ascii(self, string):

        # Declaração - Vetor para armazenar a conversão do texto simples em ASCII
        text_in_asc = [i for i in range(0, len(string))]

        # Convertendo o texto simples na forma de ASCII
        for i in range(0, len(string)):
            text_in_asc[i] = ord(string[i])

        return text_in_asc

    ## ------------------------------------
    ## Inicializando vetor S e T
    def initial_S_T_vector(self, key):

        # Declaração - Vetor - S é preenchido com os valores de 0 a 255
        S = [i for i in range(0, 256)]  # Criando o vetor de estado de 256 bytes
        # print(f"S: {S}")

        # Declaração - Vetor - T
            # Se o comprimento da chave k é de 256 bytes, então k é atribuído a T.
            # Caso contrário, para uma chave com comprimento (k-len) bytes, os primeiros k-len
            # elementos de T são copiados de K e, em seguida, K é repetido como quantas vezes
            # forem necessárias para preencher T.
        T = [0 for i in range(0, 256)]  # Criando o vetor temporário t

        k = 0
        for i in range(0, 256):

            if (k == len(key)):
                k = 0

            # Atribuição do vetor T em relação a chave
            T[i] = (key[k])

            k = k + 1

        return S, T

    ## ------------------------------------
    ## Algoritmo KSA
    def KSA(self, S, T):
        # print("\nAlgoritmo KSA")

        # Primeira permutação do vetor S
            # Usamos T para produzir a permutação inicial de S. Começando com S [0] para S [255],
            # e para cada algoritmo S [i] trocá-lo por outro byte em S de acordo com um esquema
            # ditado por T [i], mas S ainda conterá valores de 0 a 255.

        j = 0
        for i in range(0, 256):
            j = (j + S[i] + T[i]) % 256
            S[i], S[j] = S[j], S[i]

            # print(f"{i} {S}")

        return S
        # print(f"\nA matriz de permutação inicial é: {S}")

    ## ------------------------------------
    ## Algoritmo de geração pseudoaleatória
    def PRGA(self, S):

        # print("\nAlgoritmo PRGA:")

        # Gerar novo fluxo aleatorio no vetor S
            # Uma vez que o vetor S é inicializado, a chave de entrada não será usada.
            # Nesta etapa, para cada algoritmo S [i], troque-o por outro byte em S de acordo
            # com um esquema ditado pela configuração atual de S. Após atingir S [255] o processo continua,
            # começando de S [0] novamente
        key_stream = [i for i in range(0, 256)]  # Criando vetor key_stream

        j = 0
        for i in range(0, 256):
            # print(f"{i} {S}")

            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]

            t = (S[i] + S[j]) % 256
            key_stream[i] = S[t]

        return key_stream
        # print(f"\nFluxo de chave: {key_stream}")

    ## ------------------------------------
    ## XOR - Entre um plain_text / chipher_text e key_stream
    def XOR(self, text, key_stream):
        result = [i for i in range(0, len(text))]

        for i in range(len(text)):
            result[i] = text[i] ^ key_stream[i]

        return result

    ## ------------------------------------
    ## Convertendo o texto decifrado em ascii para char
    def convert_ascii_in_string(self, text):
        text_encrypt = [chr(i) for i in text]
        text_encrypt = ''.join(text_encrypt)

        return text_encrypt

    ## ------------------------------------
    ## Criando arquivo com o texto cifrado
    def cria_arquivo_texto_cifrado(self, cipher_text):
        arquivo = open("text_cipher.txt", "w")
        arquivo.write(str(cipher_text))
        arquivo.close()

    ## ------------------------------------
    ## Leitura do arquivo com o texto cifrado
    def ler_arquivo_texto_cifrado(self):
        arquivo = open('text_cipher.txt', 'r')
        texto = arquivo.readlines()
        arquivo.close()
        return texto



class RC4Encrypt(RC4):
    def __init__(self, text, key):
        self.plain_text = text
        self.key = key
        self.S = None
        self.T = None
        self.text_in_asc = None
        self.key_stream = None
        self.cipher_text = None
        self.text_in_base64 = None

    def encrypt(self):
        # Verificar se a chave é menor ou igual a 128 bits (128/8)
        super().check_key_size(self.key)

        self.key = super().convert_string_in_ascii(self.key)

        # Inicializando o vetor S e T
        self.S, self.T = super().initial_S_T_vector(self.key)

        # Conversão do texto simples ou chave em ASCII
        self.text_in_asc = super().convert_string_in_ascii(self.plain_text)

        ## Algoritmo KSA
        self.S = super().KSA(self.S, self.T)

        ## Algoritmo de geração pseudoaleatória
        self.key_stream = super().PRGA(self.S)

        ## XOR - Entre um plain_text e key_stream
        self.cipher_text = super().XOR(self.text_in_asc, self.key_stream)

        ## Convertendo o texto cifrado em ascii para char
        self.cipher_text_user = super().convert_ascii_in_string(self.cipher_text)

        ## Codificando em hexadecimal
        self.text_in_base64 = super().b64e(self.cipher_text_user)

        ### Manipulando arquivo

        ## Criação de arquivo com o texto cifrado
        super().cria_arquivo_texto_cifrado(self.text_in_base64)

        ## Ler arquivo e retorna o texto cifrado
        self.cipher_text = super().ler_arquivo_texto_cifrado()

        # print(self.text_in_base64)
        return self.text_in_base64


class RC4Decrypt(RC4):
    def __init__(self, text, key):
        self.cipher_text = super().b64d(text)
        self.key = key
        self.S = None
        self.T = None
        self.text_in_asc = None
        self.key_stream = None
        self.texto_simples = None

    def decrypt(self):
        # Verificar se a chave é menor ou igual a 128 bits (128/8)
        super().check_key_size(self.key)

        self.key = super().convert_string_in_ascii(self.key)

        # Inicializando o vetor S e T
        self.S, self.T = super().initial_S_T_vector(self.key)

        # Conversão do texto simples ou chave em ASCII
        self.text_in_asc = super().convert_string_in_ascii(self.cipher_text)

        #print(self.text_in_asc)
        ## Algoritmo KSA
        self.S = super().KSA(self.S, self.T)

        ## Algoritmo de geração pseudoaleatória
        self.key_stream = super().PRGA(self.S)

        ## XOR - Entre um cipher_text e key_stream
        self.texto_simples= super().XOR(self.text_in_asc, self.key_stream)

        ## Convertendo o texto decifrado em ascii para char
        self.texto_simples = super().convert_ascii_in_string(self.texto_simples)

        return self.texto_simples
        # print(f"Texto decifrado: {self.texto_simples}")


def main():
    while(True):
        print("=================")
        print("====== RC4 ======")
        print("=================\n")
        print("Opcoes: ")
        print("\tE - Encriptar")
        print("\tD - Decriptar")
        print("\tS - Sair\n")

        case = input("Digite a opcao desejada: ")

        if(case=='E'):
            try:
                ## ENCRYPT
                plain_text = input("\nInforme o texto a ser encriptado: ")
                key = input("\nInforme a chave para o processo de encriptacao: ")
                rc4 = RC4Encrypt(plain_text, key)
                chipher_text = rc4.encrypt()

                print(f"\nTexto Encriptado: {chipher_text}\n\n")
            except:
                print("!! Tente novamente !!\n ")

        elif(case=='D'):
            try:
                cipher_text = input("\nInforme o texto a ser decriptado: ")
                key = input("\nInforme a chave para o processo de decriptacao: ")
                rc4_1 = RC4Decrypt(cipher_text, key)
                plain_text = rc4_1.decrypt()

                print(f"\nTexto Decriptado: {plain_text}\n\n")
            except:
                print("\nNão é possível decriptar a mensagem - Formato incorreto")
                print("!! Tente novamente !!\n")

        elif(case == 'S'):
            break

        else:
            print("\n!! Comando inválido. Tente novamente !!\n\n")


if __name__ == "__main__":
    main()