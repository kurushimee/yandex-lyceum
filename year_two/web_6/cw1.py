import requests


address = input()
port = input()
a = int(input())
b = int(input())

response = requests.get(f"{address}:{port}?a={a}&b={b}")
if response:
    json = response.json()
    result = " ".join(str(x) for x in sorted(json["result"]))
    check = json["check"]
    print(f"{result}\n{check}")
