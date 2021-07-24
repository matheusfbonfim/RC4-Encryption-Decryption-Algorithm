import numpy as np
import copy

## rc4 tamanho da chave de 128 bits

vetor_s = np.array([])
vetor_s = list(range(0,256)) ##criando o vetor S
vetor_t = np.array([])
vetor_t = list(range(0,256))
chave_k = input("entre com a chave ")
text = input("entre com o texto a ser cifrado ")
valor = np.array([])
valor = list(range(0,len(text)))
cripto_saida = np.array([])
cripto_saida = list(range(0,256))
i=0
for i in range(len(text)):
    valor[i] = ord(text[i])
    i=i+1;

#print(valor)
#print(chave_k)

if(len(chave_k)>128):
    print("tamanho da chave deve ser < 128bits")
    exit()
i=0
k=0 

while (i < len(vetor_s)): ###atribuição do vetor T em relação a chave
    
    if (k == len(chave_k)):
            k = 0

    vetor_t[i] = ord(chave_k[k])
    k = k+1
    i = i+1

######################## primeira permutação do vetor S

i=0
j=0

for i in  range(256):
    j = (j+vetor_s[i]+ vetor_t[i]) % 256

    vetor_s[i],vetor_s[j] = vetor_s[j],vetor_s[i]

############## gerar novo fluxo aleatorio no vetor S
i=0
j=0

for i in  range(256):
    i = (i+1) % 256
    j = (j + vetor_s[i]) % 256
    vetor_s[i],vetor_s[j] = vetor_s[j],vetor_s[i]
    auxcrip = (vetor_s[i]+vetor_s[j]) % 256

    cripto_saida[i] = vetor_s[auxcrip]

i=0

for i in range(len(text)):    
    valor[i] = valor[i] ^ cripto_saida[i]

print(valor)

saidadecripitada = []

for i in range(len(text)):    
    valor[i] = valor[i] ^ cripto_saida[i]
    saidadecripitada.append(chr(valor[i]))
print(saidadecripitada)