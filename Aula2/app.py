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

print(para_one_hot("abc"))