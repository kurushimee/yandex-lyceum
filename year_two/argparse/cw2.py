import argparse

movies = {"melodrama": 0, "football": 100, "other": 50}

parser = argparse.ArgumentParser()
parser.add_argument("--barbie", type=int, default=50)
parser.add_argument("--cars", type=int, default=50)
parser.add_argument("--movie", choices=movies, type=str, default="other")
args = parser.parse_args()

acceptable_numbers = range(101)
barbie = args.barbie if args.barbie in acceptable_numbers else 50
cars = args.cars if args.cars in acceptable_numbers else 50
movie = movies[args.movie]

boy = int((100 - barbie + cars + movie) / 3)
girl = (100 - boy)

print(f"boy: {boy}\ngirl: {girl}")
