import random

#Etapa 0 - ASCII de estados da forca

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
  palavra = palavra.replace("\n", "")
  palavra = palavra.upper()
  
  for letra in palavra:
    if letra in letrasEspeciais:
      semAcento = letrasEspeciais[letra] #pega a letra sem acento
      palavra = palavra.replace(letra, semAcento)

  return palavra

#Etapa 2 - Sorteador

def sortearPalavra(palavras):
  palavra = random.choice(palavras)
  return palavra

def sortearTema(temas):
  tema = random.choice(temas)
  return tema

acertos = 0
erros = 0
letrasTentadas = []
letrasDescobertas = []

def printForca(erros):
  forca = estados(erros)
  for linha in forca:
    print(linha)

def printPlacar():
  print("Palavra secreta: ", letrasDescobertas)
  print("Letras tentadas: ", letrasTentadas)
  print("Acertos: ", acertos)
  print("Erros: ", erros)
  print()

def definirPlacar(a, e, lt, ld):
  global acertos, erros, letrasTentadas, letrasDescobertas
  acertos = a
  erros = e
  letrasTentadas = lt
  letrasDescobertas = " ".join(ld) #transforma em string

def start(tema, palavraSecreta):