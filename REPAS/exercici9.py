'''
Demanar a l’usuari que posi dues paraules. Al executar el programa, mostrarà per pantalla les dues paraules 
amb els dos primers caràcters de cada paraula intercanviats. Exemple: Quatre Camins passaria a Caatre Qumins.
'''
word = input('Introdueix una paraula: ')
word2 = input('Introdueix altre paraula: ')
print(f'Paraules: {word} {word2}')
print(f'{word.replace(word[0:2], word2[0:2])} {word2.replace(word2[0:2], word[0:2])}')