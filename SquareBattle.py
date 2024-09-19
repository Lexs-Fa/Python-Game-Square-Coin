#Muito obrigado por baixar meu codigo, lembrando, instale a biblioteca pygame usando ''pip install pygame''

import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo feito por Pedro em PYTHON")

#score
score_atual = 0
font = pygame.font.Font(None, 24)


#cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 127, 80)


#player
player_width = 25
player_height = 25
player_x = random.randint(0, SCREEN_WIDTH // 2 - player_width // 2)
player_y = random.randint(0, SCREEN_HEIGHT - player_height - 10)
player_speed = 0.25
player_color = BLACK

#gold
gold_width = 10
gold_height = 10
gold_x = random.randint(0, SCREEN_WIDTH - gold_width)
gold_y = random.randint(0, SCREEN_HEIGHT - gold_height)

#inimigo
enemy_width = 20
enemy_height = 20
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
enemy_y = random.randint(0, SCREEN_HEIGHT - enemy_height)
enemy_speed = 0.3
enemy_color = RED
enemy_qnt = 4
enemies = []

fonte_cor = BLACK

#desenha o jogador
def draw_player(x, y):
    pygame.draw.rect(screen, player_color, (x, y, player_width, player_height))

def draw_gold(x, y):
    pygame.draw.rect(screen, ORANGE, (x, y, gold_width, gold_height))

def detect_player_gold(player_rect, obstacle_rect):
    return player_rect.colliderect(obstacle_rect)

#desenha o inimigo
def draw_enemy(x, y):
    pygame.draw.rect(screen, enemy_color, (x, y, enemy_width, enemy_height))

for _ in range(enemy_qnt):
    enemies.append({
        'x': random.randint(0, SCREEN_WIDTH - enemy_width),
        'y': random.randint(0, SCREEN_HEIGHT - enemy_height)
    })

#cria o looping principal
Running = True
while Running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x + player_speed + player_width < SCREEN_WIDTH:
        player_x += player_speed
    if keys[pygame.K_w] and player_y - player_speed > 0:  # Movimento para cima
        player_y -= player_speed
    if keys[pygame.K_s] and player_y + player_speed + player_height < SCREEN_HEIGHT:  # Movimento para baixo
        player_y += player_speed
    if keys[pygame.K_LALT]:
        pygame.quit()


    #detectar colisão
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    gold_rect = pygame.Rect(gold_x, gold_y, gold_width, gold_height)
    if detect_player_gold(player_rect, gold_rect):
        score_atual += 1
        gold_x = random.randint(0, SCREEN_WIDTH - gold_width)
        gold_y = random.randint(0, SCREEN_HEIGHT - gold_height)
    


    if score_atual >= 10:
        screen.fill(BLACK)
        player_color = WHITE
        fonte_cor = WHITE

    # movimento inimigo
    for enemy in enemies:
        enemy['x'] -= enemy_speed
        if enemy['x'] < 0:
            enemy['x'] = SCREEN_WIDTH
            enemy['y'] = random.randint(0, SCREEN_HEIGHT - enemy_height)

    
    # desenhar na tela
    draw_player(player_x, player_y)
    draw_gold(gold_x, gold_y)
    for enemy in enemies:
        draw_enemy(enemy['x'], enemy['y'])
        enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy_width, enemy_height)
        if detect_player_gold(player_rect, enemy_rect):
            pygame.quit()
        if score_atual >= 20:
            enemy_speed = 0.4
        if score_atual >= 30:
            enemy_speed = 0.5
        

    text = font.render(f'Seu score atual é: {score_atual}', True, (fonte_cor))
    screen.blit(text, (50, 25)) 

    pygame.display.update()

pygame.quit()
