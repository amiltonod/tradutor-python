# pip install tranlate
from translate import Translator

# inglês para portugês
ingles = 1
# espanhol para português
espanhol = 2
# português para inglês
portugues = 3
# português para espanhol
portugues1 = 4

print('[1] = Inglês p/ Português \n[2] = Espanhol p/ Português'
      ' \n[3] = Português p/ Inglês \n[4] = Português p/ Espanhol')

# escolha da lingua sugerida no cabeçalho
choice = int(input('Escolha a língua: '))
# condicional para escolha da linguagem em inglês para portugues
if choice == 1:
    frase = input('Frase em inglês: ')
# configura a tradução
    i = Translator(from_lang='english', to_lang='pt-br')
    tri = i.translate(frase)
    print(tri)
# condicional para escolha da linguagem em espanhol para portugues
elif choice == 2:
    frase = input('Frase em espanhol: ')
    e = Translator(from_lang='spanish', to_lang='pt-br')
    tre = e.translate(frase)
    print(tre)
# condicional para escolha da linguagem em portugues para ingles
elif choice == 3:
    frase = input('Frase em português: ')
    pt = Translator(from_lang='pt-br', to_lang='english')
    trp = pt.translate(frase)
    print(trp)
# condicional para escolha da linguagem portugues para espanhol
elif choice == 4:
    frase = input('Frase em português: ')
    pt = Translator(from_lang='pt-br', to_lang='spanish')
    trp = pt.translate(frase)
    print(trp)
else:
    print('Tradução incexistente no sistema.')
