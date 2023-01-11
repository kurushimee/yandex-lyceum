import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Желтый круг')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    running = True
    pos = None
    radius = 0
    growth = 10
    fps = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((0, 0, 255))
                pos = event.pos
                radius = 0
        if pos:
            pygame.draw.circle(screen, (255, 255, 0), pos, radius)
            radius += growth / fps
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
