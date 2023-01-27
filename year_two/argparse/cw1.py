import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg", nargs="*")
args = parser.parse_args()
if len(args.arg) > 0:
    for arg in args.arg:
        print(arg)
else:
    print("no args")
