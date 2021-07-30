## RC4 - chaves de 12256 bits

###########################
# Entradas - Texto e chave
plain_text = input("Entre com o texto a ser cifrado: ")
key = input("Entre com a chave K: ")

# ------------------------------------
# Verificar se a chave é menor ou igual a 12256 bits
if (len(key) > 12256):
    print("O comprimento da chave não pode ser superior a 12256 bits")
    exit()


###########################
# ENCRIPTANDO
print("\n###########################")
print("ENCRIPTANDO\n")

# ------------------------------------
# Imprimindo texto simples
print(f"Texto Simples: {plain_text}")

# Imprimindo chave
print(f"Chave K: {key}")

# ------------------------------------
# Declaração - Vetor para armazenar a conversão do texto simples em ASCII e encriptado
text_in_asc = [i for i in range(0, len(plain_text))]

# ------------------------------------
# Declaração - Vetor para armazenar o texto encriptado
chipher_text = [i for i in range(0, len(plain_text))]

# ------------------------------------
# Convertendo o texto simples na forma de ASCII
for i in range(len(plain_text)):
    text_in_asc[i] = ord(plain_text[i])
    i = i + 1;

# ------------------------------------
# Imprimindo texto em ASCII
print(f"Texto em ASCII: {text_in_asc}\n")


###########################
## INICIALIZANDO S e T

# Declaração - Vetor - S é preenchido com os valores de 0 a 255
S = [i for i in range(0, 256)]    # Criando o vetor de estado de 256 bytes
print(f"S: {S}")

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
    T[i] = ord(key[k])

    k = k + 1

print(f"T: {T}")


###########################
## ALGORITMO KSA
print("\nAlgoritmo KSA")

# Primeira permutação do vetor S
    # Usamos T para produzir a permutação inicial de S. Começando com S [0] para S [255],
    # e para cada algoritmo S [i] trocá-lo por outro byte em S de acordo com um esquema
    # ditado por T [i], mas S ainda conterá valores de 0 a 255.

j = 0
for i in range(0, 256):
    j = (j + S[i] + T[i]) % 256
    S[i], S[j] = S[j], S[i]

    print(f"{i} {S}")

print(f"\nA matriz de permutação inicial é: {S}")


###########################
## ALGORITMO DE GERAÇÃO PSEUDOALEATÓRIA
print("\nAlgoritmo PGRA:")

# Gerar novo fluxo aleatorio no vetor S
    # Uma vez que o vetor S é inicializado, a chave de entrada não será usada.
    # Nesta etapa, para cada algoritmo S [i], troque-o por outro byte em S de acordo
    # com um esquema ditado pela configuração atual de S. Após atingir S [255] o processo continua,
    # começando de S [0] novamente
key_stream = [i for i in range(0, 256)] # Criando vetor key_stream

j = 0
for i in range(0, 256):
    print(f"{i} {S}")

    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]

    t = (S[i] + S[j]) % 256
    key_stream[i] = S[t]


print(f"\nFluxo de chave: {key_stream}")

###########################
## ENCRIPTANDO
    # Faça o XOR do valor k com o próximo byte do texto claro.
    # Este keystream agora é XOR com o texto simples, este XORing é feito byte a byte para
    # produzir o texto criptografado.
for i in range(len(text_in_asc)):
    chipher_text[i] = text_in_asc[i] ^ key_stream[i]

print(f"\nTexto encriptado com RS4: {chipher_text}")

text_encrypt = [chr(i) for i in chipher_text]
text_encrypt = ''.join(text_encrypt)
print(f"Texto encriptado: {text_encrypt}\n")


###########################
## DESCRIPTANDO

# Para decriptar, faça o XOR do valor k com o próximo byte do texto cifrado

plain_text_decrypt = []

for i in range(len(plain_text)):
    chipher_text[i] = chipher_text[i] ^ key_stream[i]
    plain_text_decrypt.append(chr(chipher_text[i]))

print(f"Texto descriptado - Lista: {plain_text_decrypt}")

plain_text_decrypt = "".join(plain_text_decrypt)
print(f"Texto descriptado: {plain_text_decrypt}")
