from typing import List, Tuple


class Film:
    """Содержит имя фильма, длительность в минутах и время сеанса"""

    def __init__(self, name: str, duration: str, time: str):
        self.name = name
        self.duration = duration
        self.time = time

    def time_in_minutes(self):
        return self.time[:2] * 60 + self.time[-2:]

    def __str__(self) -> str:
        return self.name


class Hall:
    """Содержит информацию о проходящем фильме и занятых местах"""

    def __init__(self, id=0, film: Film = None, seat_rows=1, seatspr=1):
        self.id = id
        self.film = film
        self.seat_rows = seat_rows
        self.seatspr = seatspr
        self.init_seats()

    def init_seats(self):
        self.seats = [
            [0 for _ in range(self.seatspr)] for _ in range(self.seat_rows)
        ]

    def change_film(self, film: Film):
        self.film = film
        self.init_seats()

    def occupy_seat(self, seat=(0, 0)) -> bool:
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

    def __init__(self, name: str, halls: List[Hall] = []):
        self.name = name
        self.halls = halls

    def append_hall(self, hall: Hall):
        self.halls.append(hall)

    def __str__(self) -> str:
        return self.name


class TicketSystem:
    """Содержит кинотеатры и управляет ими"""

    def __init__(self, cinemas: List[Cinema] = []):
        self.cinemas = cinemas

    def append_cinema(self, cinema: Cinema):
        self.cinemas.append(cinema)

    def get_session(
        self, film: str, required_spots=1
    ) -> Tuple[Hall, List[Tuple[int, int]]]:
        nearest = tuple()
        for cinema in self.cinemas:
            for hall in cinema.halls:
                if str(hall.film) == str(film) and (
                    nearest == tuple()
                    or hall.film.time_in_minutes()
                    < nearest[1].film.time_in_minutes()
                ):
                    in_a_row = 0
                    available_seats = []
                    for row in range(len(hall.seats)):
                        if in_a_row == required_spots:
                            nearest = (cinema, hall, available_seats)
                            break
                        for col in range(len(hall.seats[row])):
                            if in_a_row == required_spots:
                                nearest = (cinema, hall, available_seats)
                                break
                            if hall.seats[row][col] == 0:
                                in_a_row += 1
                                available_seats.append((row, col))
                            else:
                                in_a_row = 0
                                available_seats.clear()
        if nearest != tuple():
            print(
                f'Нашлась сессия на фильм\
 "{film}" в "{nearest[0]}," {nearest[1].id}-й зал.'
            )
            return (nearest[1], nearest[2])
        print("Нет сессии на данный фильм.")

    def buy_ticket(self, hall: Hall, seats: List[Tuple[int, int]]) -> bool:
        for seat in seats:
            if hall.occupy_seat(seat) is False:
                print(f"Ошибка! {seat[1]} место в {seat[0]} ряду занято.")
                return False
        print(f'Приобретён билет на фильм "{hall.film}".')
        return True


# Создание фильма с названием "Harry Potter" длительностью 1:30 в 16:30
film1 = Film("Harry Potter", "1:30", "16:30")
# Создание зала с 6 рядами по 10 кресел в каждом
hall1 = Hall(seat_rows=6, seatspr=10)
# Создание пустого кинотеатра
cin1 = Cinema("Кинотеатр имени Ленина")
# Создание пустой системы билетов
tsys1 = TicketSystem()

# Добавление кинотеатра cin1 в систему билетов tsys1
tsys1.append_cinema(cin1)
# Добавление зала hall1 в кинотеатр cin1
cin1.append_hall(hall1)
# Изменение следующего фильма в зале hall1 на фильм film1
hall1.change_film(film1)

print("Конфигурация кресел hall1:")
print(hall1)

print(f"Длительность фильма: {film1.duration}")
print()

# Поиск ближайшей сессии фильма film1 с тремя местами рядом
# в системе билетов tsys1
session = tsys1.get_session(film1, 3)
# Покупка билета на ближайшую сессию фильма film1 в билетной системе tsys1
tsys1.buy_ticket(*session)
print()

print("Конфигурация кресел hall1 после покупки билета:")
print(hall1)
