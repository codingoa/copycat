import csv
from collections import defaultdict

vanilla = [1,2,3,5,7,9,12,10,7]

scores = defaultdict(float)

with open("playrates.txt", "r") as fp:
    reader = csv.reader(fp)

    for name, cost, power, playrate in reader:
        diff = vanilla[int(cost)] - int(power)

        if diff <= -3.5:
            scores["very_bad"] += float(playrate)
        elif diff <= -1.5:
            scores["bad"] += float(playrate)
        elif diff <= 1.5:
            scores["neutral"] += float(playrate)
        elif diff <= 3.5:
            scores["good"] += float(playrate)
        else:
            scores["very_good"] += float(playrate)

total = sum(scores.values())
pretty = lambda key:print(f"{key.replace('_',' ')} {scores[key] / total:.2%}")
pretty("very_good")
pretty("good")
pretty("neutral")
pretty("bad")
pretty("very_bad")

