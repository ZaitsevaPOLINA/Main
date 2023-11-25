
# TODO решите задачу
import json

with open('input.json') as f:
    data = json.load(f)

def task(data) -> float:

    sum=0
    for item in data:
        sum+=item["score"]*item["weight"]

    return sum

print(format(task(data), ".3f"))



