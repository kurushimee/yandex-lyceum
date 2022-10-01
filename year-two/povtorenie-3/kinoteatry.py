from typing import List

import numpy as np


class Film:
    """Содержит имя фильма, длительность в минутах и время сеанса"""

    def __init__(self, name: str, duration: int, time: str):
        self.name = name
        self.duration = duration
        self.time = time


class Hall:
    """Содержит информацию о фильмах и конфигурации кресел"""

    def __init__(
        self, films: List[Film] = [], seats=np.zeros((8, 12), dtype=np.int_)
    ):
        self.films = films
        self.seats = seats

    def append_film(self, film: Film):
        self.films.append(film)

    def occupy_seat(self, seat: tuple = (0, 0)) -> bool:
        # Возвращает True если место не занято, иначе False
        if self.seats[seat[0]][seat[1]] == 0:
            self.seats[seat[0]][seat[1]] = 1
            return True
        else:
            return False

    def __str__(self) -> str:
        return "\n".join([" ".join([str(y) for y in x]) for x in self.seats])


class Cinema:
    """Содержит кинотеаторные залы и управляет ими"""

    def __init__(self, halls: List[Hall] = []):
        self.halls = halls

    def append_hall(self, hall: Hall):
        self.halls.append(hall)


class TicketSystem:
    """Содержит кинотеатры и управляет ими"""

    def __init__(self, cinemas: List[Cinema] = []):
        self.cinemas = cinemas

    def append_cinema(self, cinema: Cinema):
        self.cinemas.append(cinema)

    def get_session(self):
        pass


film1 = Film("Harry Potter", 90, "16:30")
hall1 = Hall()
cin1 = Cinema()
tsys1 = TicketSystem()

tsys1.append_cinema(cin1)
cin1.append_hall(hall1)
hall1.append_film(film1)
