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


#Cria a matriz identidade P;
alfabeto = "abcdefghijklmnopqrstuvwxyz"
matrix_permutacao = np.eye(len(alfabeto))
#Permuta as linhas da matriz identidade P;
np.random.shuffle(matrix_permutacao)

print(cifrar("jonass",matrix_permutacao))