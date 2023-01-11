import sys
import pygame


class Color:
    def __init__(self):
        self.index = 0

    def cycle(self) -> tuple:
        colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255))
        color = colors[self.index]
        if self.index + 1 == len(colors):
            self.index = 0
        else:
            self.index += 1
        return color


if __name__ == "__main__":
    try:
        w, n = [int(x) for x in list(map(str.strip, sys.stdin))[0].split()]
    except ValueError:
        print("Неправильный формат ввода")
    except IndexError:
        print("Неправильный формат ввода")
    else:
        pygame.init()
        pygame.display.set_caption("Мишень")
        WIDTH = HEIGHT = w * n * 2
        size = width, height = WIDTH, HEIGHT
        screen = pygame.display.set_mode(size)

        screen.fill((0, 0, 0))
        color = Color()
        pygame.draw.circle(screen, color.cycle(), (WIDTH // 2, HEIGHT // 2), w)
        for i in range(2, n + 1):
            pygame.draw.circle(screen, color.cycle(), (WIDTH // 2, HEIGHT // 2), w * i, w)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass

        pygame.quit()
