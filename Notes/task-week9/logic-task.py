#Escribir una funcion que va recibir un string como parametro
#La funcion va retormar un diccionario donde cada una de sus letras dentro del parametro van a ser sus KEYS y el valor de cada una de ellas va ser la 
# de veces que esa letra se repite en la palabra
def getRepeatedChars(word):
    newWord = {}
    for i in word:
        if i in newWord:
            newWord[i] = newWord[i] + 1
        else:
            newWord[i] = 1
        
    return newWord

user = input("Digite la palabra: ")
print(getRepeatedChars(user))