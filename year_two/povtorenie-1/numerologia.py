hours = [int(x) for x in input().split()]
hours.sort()
minutes = [int(x) for x in input().split()]
minutes.sort()

for h in hours:
    sum_h = sum([int(x) for x in str(h)])
    if h < 10:
        h = f"0{h}"
    for m in minutes:
        sum_m = sum([int(x) for x in str(m)])
        if m < 10:
            m = f"0{m}"
        if sum_m != sum_h:
            print(f"{h}:{m}")
