import sys
import pygame


if __name__ == "__main__":
    try:
        w, h = [int(x) for x in list(map(str.strip, sys.stdin))[0].split()]
    except ValueError:
        print("Неправильный формат ввода")
    except IndexError:
        print("Неправильный формат ввода")
    else:
        pygame.init()
        pygame.display.set_caption("Прямоугольник")
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))
        screen.fill(pygame.Color("red"), (1, 1, w - 2, h - 2))
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
