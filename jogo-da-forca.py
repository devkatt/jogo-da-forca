import random
import os
import time

# Projeto - Jogo da Forca

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

animais = open("palavras/animais.txt", "r", encoding="utf8").readlines()
frutas = open("palavras/frutas.txt", "r", encoding="utf8").readlines()
objetos = open("palavras/objetos.txt", "r", encoding="utf8").readlines()
paises = open("palavras/paises.txt", "r", encoding="utf8").readlines()


# Temas
palavras = {
        'ANIMAL':animais,
        'FRUTA':frutas,
        'OBJETO': objetos,
        'PAÍS': paises
}

# Tratamento de caracteres especiais
letrasEspeciais = {
    "Á":"A", "À":"A", "Ã":"A", " ":"A",
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


#Sorteador
def sortearPalavra(palavras):
  palavra = random.choice(palavras)
  return palavra

def sortearTema(temas):
  tema = random.choice(temas)
  return tema
 
#Definindo o placar
acertos = 0
erros = 0
letrasTentadas = []
letrasDescobertas = []

#Função para imprimir forca
def printForca(erros):
  forca = estados[erros]
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

#Inicio do jogo
def start(tema, palavraSecreta):

  inicio = time.time()

  def printHeader(tema):
    print()
    print("********** JOGO DA FORCA **********")
    print()
    print("TEMA:", tema)

  def printResultado(palavraSecreta, acertos, erros):
    if acertos == len(palavraSecreta):
      print("PARABÉNS VOCÊ GANHOU!!")
     
    if erros == 6:
      print("GAME OVER!")
      print("A palavra era: ", palavraSecreta)

  def updateAcertadas(letraDigitada, letrasDescobertas, palavraSecreta):
    if letraDigitada in palavraSecreta:
      i = 0 #índice (posição da letra)
      for letra in palavraSecreta:
        if letra == letraDigitada:
          letrasDescobertas[i] = letraDigitada
        i += 1

  def clear():
    if os.name == "nt": #Se for Windows
        os.system("cls")

  clear() #Limpa a tela para iniciar o jogo #joão victor

  #Placar do jogo
  acertos = 0
  erros = 0
  letrasDigitadas = []
  letrasDescobertas = ["_"]*len(palavraSecreta)
  definirPlacar(acertos, erros, letrasDigitadas, letrasDescobertas)
  maximoAcertos = len(palavraSecreta) #Quantidade máxima de letras que é possível acertar
 
  while (erros < 6):
    printHeader(tema)
    printForca(erros)
    printPlacar()
    letraDigitada = pedirLetra(letrasDigitadas)
   
    if letraDigitada in palavraSecreta:
      #Substituindo traços pela letra descoberta
      updateAcertadas(letraDigitada, letrasDescobertas, palavraSecreta)
      acertos += palavraSecreta.count(letraDigitada)
      if acertos == maximoAcertos:
        definirPlacar(acertos, erros, letrasDigitadas, letrasDescobertas)
        clear()
        break

    else:
      erros += 1 
     
    #Atualizando os valores do placar
    definirPlacar(acertos, erros, letrasDigitadas, letrasDescobertas)
    clear() 

  fim = time.time()
  tempo_decorrido = round(fim - inicio, 2)
  minutos, segundos = divmod(tempo_decorrido, 60)

  #IMpressões finais do jogo
  printHeader(tema)
  printForca(erros)
  printPlacar()
  printResultado(palavraSecreta, acertos, erros)
  print()
  print("O TEMPO DECORRIDO FOI:", tempo_decorrido, "SEGUNDOS!")
  print()
  print("---------------FIM DE JOGO---------------")

#Criando o menu
def pedirLetra(letrasDigitadas):
  letraDigitada = input("Digite uma letra: ").upper()
  letraDigitada = validarLetra(letraDigitada, letrasDigitadas)
  
  #Adicionando entrada na lista:
  letrasDigitadas.append(letraDigitada)

  #Ordenando a lista:
  letrasDigitadas.sort()

  #Retornando a letra digitada:
  return letraDigitada 

def validarLetra(entrada, letrasDigitadas):
  entrada = convertPalavra(entrada)#Tira os acentos da palavra
 
  #Validando entrada
  teste1 = not entrada.isalpha() #Analisa se a entrada não é uma letra
  teste2 = len(entrada) > 1  #Analisa se foi digitada mais que uma letra
  teste3 = entrada in letrasDigitadas #Analisa se a letra já tinha sido inserida antes
 
  while teste1 or teste2 or teste3:
   
    if teste1:
      print("Digite apenas letras! Tente novamente.")
   
    elif teste2:
      print("Você inseriu mais de uma letra! Tente novamente.")
 
    elif teste3:
      print("Você já digitou essa letra...")
   
    entrada = input("Digite uma letra novamente: ").upper()
   
    entrada = convertPalavra(entrada)#Tira os acentos da palavra
    teste1 = not entrada.isalpha() #Analisa se a entrada não é uma letra
    teste2 = len(entrada) > 1  #Analisa se foi digitada mais que uma letra
    teste3 = entrada in letrasDigitadas #Analisa se a letra já tinha sido inserida antes
 
  return entrada #katarina


#Condição para continuar jogando
querJogar = True
while querJogar:
  #Sorteando tema
  listaTemas = list(palavras.keys()) #pega as chaves do dicionário palavras e adiciona elas numa lista
  tema = sortearTema(listaTemas) #samyra

  #Sorteando a plavra secreta
  listaPalavras = palavras[tema]
  palavraSecreta = sortearPalavra(listaPalavras) 
 
  #Removendo os acentos das palavras
  palavraSecreta = convertPalavra(palavraSecreta) 

  #Comecando o jogo
  start(tema, palavraSecreta) 

  #Decidindo se continua ou não
  continuar = input("Quer continuar jogando? (S/N): ").upper()
  querJogar = True if continuar == 'S' else False