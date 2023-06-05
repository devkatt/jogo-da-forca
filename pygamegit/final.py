import pygame
import random
import os
import time
import string
# Inicialização do Pygame
pygame.init()
# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (17, 103, 177)
GRAY = (80, 80, 80)
# Configurações da janela
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Forca")
# Redimensionar as imagens, se necessário
largura_desejada = 200
altura_desejada = 200
# Carregar imagens da forca
estados = [
    pygame.transform.scale(pygame.image.load("estado0.png"), (largura_desejada, altura_desejada)),
    pygame.transform.scale(pygame.image.load("estado1.png"), (largura_desejada, altura_desejada)),
    pygame.transform.scale(pygame.image.load("estado2.png"), (largura_desejada, altura_desejada)),
    pygame.transform.scale(pygame.image.load("estado3.png"), (largura_desejada, altura_desejada)),
    pygame.transform.scale(pygame.image.load("estado4.png"), (largura_desejada, altura_desejada)),
    pygame.transform.scale(pygame.image.load("estado5.png"), (largura_desejada, altura_desejada)),
    pygame.transform.scale(pygame.image.load("estado6.png"), (largura_desejada, altura_desejada))
]
imagens_redimensionadas = [
    pygame.transform.scale(imagem, (largura_desejada, altura_desejada))
    for imagem in estados
]
# Variáveis do jogo
palavras = ['GATO', 'CACHORRO', 'GIRAFA', 'ELEFANTE']
palavra_secreta = ""
letras_descobertas = []
letras_tentadas = []
erros = 0
acertos = 0
temporizado = False
# Função para sortear uma palavra
def sortear_palavra():
    return random.choice(palavras)
# Função para desenhar a forca na janela
def desenhar_forca():
    window.blit(estados[erros], (200, 100))
# Função para desenhar as letras tentadas na janela
def desenhar_letras_tentadas():
    fonte = pygame.font.Font(None, 25)
    texto = fonte.render("Letras tentadas: " + " ".join(letras_tentadas), True, WHITE)
    window.blit(texto, (20, 20))
# Função para desenhar o placar na janela
def placar_acerto():
    fonte = pygame.font.Font(None, 20)
    texto = fonte.render(f"Acertos: {acertos}", True, WHITE)
    window.blit(texto, (20, 40))
def placar_erro():
    fonte = pygame.font.Font(None, 20)
    texto = fonte.render(f"Erros: {erros}", True, WHITE)
    window.blit(texto, (20, 60))
# Função para desenhar a palavra descoberta na janela
def desenhar_palavra_descoberta():
    fonte = pygame.font.Font(None, 40)
    texto = fonte.render(" ".join(letras_descobertas), True, WHITE)
    window.blit(texto, (300, 320))

    # Função para atualizar a palavra descoberta com a letra correta
def atualizar_palavra_descoberta(letra):
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            letras_descobertas[i] = letra
# Função para verificar se a letra já foi tentada
def letra_ja_tentada(letra):
    return letra in letras_tentadas
# Função para verificar se o jogador venceu o jogo
def jogador_venceu():
    return "_" not in letras_descobertas
# Função principal do jogo
def jogar(temporizado):
    global palavra_secreta, letras_descobertas, letras_tentadas, erros, acertos, mensagem_erro
    jogando = True
    while jogando:
        # Sortear uma nova palavra
        palavra_secreta = sortear_palavra()
        letras_descobertas = ["_"] * len(palavra_secreta)
        letras_tentadas = []
        erros = 0
        acertos = 0
        mensagem_erro = ""
        # Variável de controle do tempo
        tempo_inicial = time.time()
        # Loop principal
        while True:
            # Tratar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    if erros < 6 and not jogador_venceu():
                        if event.unicode.isalpha():
                            letra = event.unicode.upper()
                        else:
                            mensagem_erro = "Digite apenas letras! Tente novamente."
                            continue
                        if letra_ja_tentada(letra):
                            mensagem_erro = "Você já tentou essa letra! Tente novamente."
                            continue
                        letras_tentadas.append(letra)
                        if letra in palavra_secreta:
                            acertos += palavra_secreta.count(letra)
                            atualizar_palavra_descoberta(letra)
                        else:
                            erros += 1
                            mensagem_erro = "Letra incorreta! Tente novamente."
            # Calcular o tempo decorrido
            tempo_decorrido = int(time.time() - tempo_inicial)
            # Renderizar a janela
            window.fill(GRAY)
            desenhar_forca()
            placar_erro()
            placar_acerto()
            desenhar_palavra_descoberta()
            desenhar_letras_tentadas()
            
            # Renderizar a mensagem de erro
            if mensagem_erro:
                fonte_erro = pygame.font.Font(None, 20)
                texto_erro = fonte_erro.render(mensagem_erro, True, WHITE)
                window.blit(texto_erro, (20, 100))
            # Verificar condições de vitória ou derrota
            if jogador_venceu():
                fonte = pygame.font.Font(None, 72)
                texto = fonte.render("Você venceu!", True, BLACK)
                window.blit(texto, (240, 400))
            elif erros >= 6:
                fonte = pygame.font.Font(None, 72)
                texto = fonte.render("Você perdeu!", True, BLACK)
                window.blit(texto, (240, 400))
                fonte = pygame.font.Font(None, 48)
                texto = fonte.render(f"A palavra era: {palavra_secreta}", True, BLACK)
                window.blit(texto, (225, 450))

        # Mostrar o tempo decorrido, se o modo for dinâmico
            if temporizado:
                fonte = pygame.font.Font(None, 20)
                texto = fonte.render(f"Tempo: {tempo_decorrido}s", True, WHITE)
                window.blit(texto, (20, 80))
            pygame.display.update()
            # Verificar condições de vitória ou derrota
            if jogador_venceu() or erros >= 6:
                pygame.time.wait(2000)
                break

        # Perguntar se o jogador deseja jogar novamente
        fonte = pygame.font.Font(None, 30)
        texto = fonte.render("Começar uma nova rodada? (S ou N)", True, BLACK)
        window.blit(texto, (240, 500))
        pygame.display.update()

        jogando = None
        while jogando is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        jogando = True
                    elif event.key == pygame.K_n:
                        jogando = False
# Função para exibir o menu de seleção do modo de jogo
def exibir_menu():
    modo = None
    fonte = pygame.font.Font(None, 36)
    texto_modo = fonte.render("Escolha o modo de jogo:", True, WHITE)
    texto_modo1 = fonte.render("1 - Modo Normal", True, WHITE)
    texto_modo2 = fonte.render("2 - Modo Dinâmico", True, WHITE)
    while modo not in ['1', '2']:
        window.fill(BLACK)
        window.blit(texto_modo, (240, 200))
        window.blit(texto_modo1, (300, 300))
        window.blit(texto_modo2, (300, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.unicode in ['1', '2']:
                    modo = event.unicode
    return modo
# Executar o jogo
modo_jogo = exibir_menu()
if modo_jogo == '1':
    jogar(temporizado=False)
elif modo_jogo == '2':
    jogar(temporizado=True)