import random

#Etapa 0 - ASCII de estados da forca

'''A forca possui 7 estados que vão desde o estado 0 (forca sem o corpo), 
até o estado 6 (totalmente enforcado)'''

#Estados da Forca:
estado0 = [
"╔════════╗",
"║        ¥",
"║", 
"║", 
"║", 
"║"
]

estado1 = [
"╔════════╗",
"║        ¥",
"║        O", 
"║", 
"║", 
"║"
]

estado2 = [
"╔════════╗",
"║        ¥",
"║        O",
"║        |",
"║", 
"║"
]

estado3 = [
"╔════════╗",
"║        ¥",
"║        O",
"║       /|",
"║",
"║"
]

estado4 = [
"╔════════╗",
"║        ¥",
"║        O",
"║       /|\ ",
"║", 
"║"
]

estado5 = [
"╔════════╗",
"║        ¥",
"║        O",
"║       /|\ ",
"║       /",
"║"
]

estado6 = [
"╔════════╗",
"║        ¥",
"║        O",
"║       /|\ ",
"║       / \ ",
"║"
]

estados = {
  0:estado0, 
  1:estado1, 
  2:estado2,
  3:estado3,
  4:estado4,
  5:estado5,
  6:estado6
}


#Etapa 1 - Listas de Palavras
animais = open("palavras/animais.txt", "r", encoding="utf8").readlines()
frutas = open("palavras/frutas.txt", "r", encoding="utf8").readlines()
objetos = open("palavras/objetos.txt", "r", encoding="utf8").readlines()
paises = open("palavras/paises.txt", "r", encoding="utf8").readlines()

#Temas
palavras = {
        'ANIMAL': animais,
        'FRUTA': frutas,
        'OBJETO': objetos,
        'PAÍS': paises
}

#Tratamento de caracteres especiais
letrasEspeciais = {
    "Á":"A", "À":"A", "Ã":"A", "Â":"A",
    "É":"E", "È":"E", "Ê":"E",
    "Í":"I", "Ì":"I", "Î":"I",
    "Ó":"O", "Õ":"O", "Ò":"O",
    "Ú":"U", "Ù":"U", "Û":"U",
    "Ç":"C",
    "-":"",
    " ":"",
  }

def convertPalavra(palavra):
  """
  palavra --> string contendo uma palavra

  ________________
  Retorna a palavra sem 'acentos', sem hifens e em CAIXA ALTA.
  Também tira espaços e quebra de linha da palavra, se houver.
  """
  palavra = palavra.replace("\n", "")
  palavra = palavra.upper()
  
  for letra in palavra:
    if letra in letrasEspeciais:
      semAcento = letrasEspeciais[letra] #pega a letra sem acento
      palavra = palavra.replace(letra, semAcento)

  return palavra

#Etapa 2 - Sorteador

def sortearPalavra(palavras):
  """
  palavras --> uma lista contendo palavras;
  ---------------
  Dada uma lista de palavras, sorteia e retorna uma palavra da lista.
  """
  palavra = random.choice(palavras)
  return palavra

def sortearTema(temas):
  """
  temas --> uma lista contendo temas;
  ---------------
  Dada uma lista de temas, sorteia e retorna um tema da lista.
  """
  tema = random.choice(temas)
  return tema