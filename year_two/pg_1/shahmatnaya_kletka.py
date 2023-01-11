import sys
import pygame


def invert(colour: tuple) -> tuple:
    white = (255, 255, 255)
    black = (0, 0, 0)
    if not colour or colour == white:
        colour = black
    else:
        colour = white
    return colour


if __name__ == "__main__":
    try:
        a, n = [int(x) for x in list(map(str.strip, sys.stdin))[0].split()]
    except ValueError:
        print("Неправильный формат ввода")
    except IndexError:
        print("Неправильный формат ввода")
    else:
        pygame.init()
        pygame.display.set_caption("Шахматная клетка")
        size = width, height = a, a
        screen = pygame.display.set_mode(size)

        screen.fill((0, 0, 0))
        cell_size = a // n
        colour = None
        for y in range(0, a, cell_size):
            if (a / n) % 2 != 0:
                colour = invert(colour)
            for x in range(0, a, cell_size):
                colour = invert(colour)
                pygame.draw.rect(screen, colour, (x, y, cell_size, cell_size))
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass

        pygame.quit()
