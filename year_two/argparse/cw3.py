import os
import argparse


def count_lines(path: str) -> int:
    if os.path.isfile(path):
        with open(path) as f:
            return len(f.readlines())
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default="")
    args = parser.parse_args()
    print(count_lines(args.file))
