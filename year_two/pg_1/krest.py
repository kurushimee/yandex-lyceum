import sys
import pygame


def draw(surface):
    surface.fill((0, 0, 0))
    color = pygame.Color(255, 255, 255)
    pygame.draw.line(surface, color, (0, 0), (w, h), 5)
    pygame.draw.line(surface, color, (w, 0), (0, h), 5)


if __name__ == '__main__':
    try:
        w, h = [int(x) for x in list(map(str.strip, sys.stdin))[0].split()]
    except ValueError:
        print("Неправильный формат ввода")
    except IndexError:
        print("Неправильный формат ввода")
    else:
        pygame.init()
        pygame.display.set_caption("Крест")
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
