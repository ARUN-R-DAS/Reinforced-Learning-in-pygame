import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Step 2: Movement")

#colors
RED = (255,0,0)
BLACK = (0,0,0)
GRID_COLOR = (120,120,120)

GRID = 40

#dot data
dot_pos = [GRID//2,GRID//2]
dot_radius = 10

can_move = True

clock = pygame.time.Clock()
running = True

#draw grid
def draw_grid():
    for x in range(0,800,GRID):
        pygame.draw.line(screen, GRID_COLOR,(x,0),(x,600))
    for y in range(0,600,GRID):
        pygame.draw.line(screen, GRID_COLOR,(0,y),(800,y))

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #keyboard input
    if event.type == pygame.KEYDOWN and can_move:
        if event.key == pygame.K_LEFT:
            dot_pos[0] -= GRID
        if event.key == pygame.K_RIGHT:
            dot_pos[0] += GRID
        if event.key == pygame.K_UP:
            dot_pos[1] -= GRID
        if event.key == pygame.K_DOWN:
            dot_pos[1] += GRID
        can_move = False

    if event.type == pygame.KEYUP:
        can_move = True
    
    screen.fill(BLACK)
    draw_grid()
    pygame.draw.circle(screen, RED, (dot_pos[0], dot_pos[1]), dot_radius)
    pygame.display.flip()

pygame.quit()