import numpy as np

def para_one_hot(msg): 
    '''
    Para codificar mensagens como uma matriz usando one-hot encoding
    '''
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    matrix = np.zeros((len(alfabeto),len(msg)))
    for i in range(len(msg)):
        # i - Coluna que preciso colocar
        for j in range(len(alfabeto)):
            if alfabeto[j] == msg[i]:
                # j - Linha que preciso colocar
                matrix[j,i] = 1
    return matrix

def para_string(M):
    '''
    Da matriz para letrinha.
    Para converter mensagens da representação one-hot encoding para uma string legível.
    '''
    msg = ""
    matrix = np.array(M)
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for i in range(M.shape[1]):
        msg += alfabeto[np.argmax(M[:, i])] #argmax retorna o indice do maior valor e uso para encontrar a letra correspondente
    return msg

# string_matriz = para_one_hot("jonas")
# matriz_string = para_string(string_matriz)

def cifrar(msg,P):
    '''
    Uma função que aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. `P` é a matriz de permutação que realiza a cifra.
    '''
    matrix_base = para_one_hot(msg)
    matrix_cifrada = P @ matrix_base
    string_cifrada = para_string(matrix_cifrada)
    return string_cifrada

def de_cifrar(msg,P):
    '''
    Uma função que recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. `P` é a matriz de permutação que realiza a cifra.
    '''
    matrix_base = para_one_hot(msg)
    inverso_permutacao = np.linalg.inv(P)
    matrix_decifrada = inverso_permutacao @ matrix_base
    string_decifrada = para_string(matrix_decifrada)
    return string_decifrada

def enigma(msg,P,E):
    '''
    Uma função que faz a cifra enigma na mensagem de entrada usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.
    '''
    matrix_base = para_one_hot(msg)
    matrix_permuta = E @ P
    matrix_cifrada = matrix_permuta @ matrix_base
    string_cifrada = para_string(matrix_cifrada)
    return string_cifrada

def de_enigma(msg,P,E):
    '''
    Uma função que recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.
    '''

    matrix_base = para_one_hot(msg)
    matrix_permuta = E @ P
    inverso_permutacao = np.linalg.inv(matrix_permuta)
    matrix_decifrada = inverso_permutacao @ matrix_base
    string_decifrada = para_string(matrix_decifrada)
    return string_decifrada



# TESTA CIFRAR
alfabeto = "abcdefghijklmnopqrstuvwxyz"
matrix_permutacao = np.eye(len(alfabeto))
#Permuta as linhas da matriz identidade P;
np.random.shuffle(matrix_permutacao)

cifrado = cifrar("novidade",matrix_permutacao)
print(de_cifrar(cifrado,matrix_permutacao))

# TESTA ENIGMA
alfabeto = "abcdefghijklmnopqrstuvwxyz"
matrix_permutacao = np.eye(len(alfabeto))
matrix_permutacao_e = np.eye(len(alfabeto))
#Permuta as linhas da matriz identidade P;
np.random.shuffle(matrix_permutacao)

enigma = enigma("novidadejonas",matrix_permutacao,matrix_permutacao_e)
print(enigma)
print(de_enigma(enigma,matrix_permutacao,matrix_permutacao_e))