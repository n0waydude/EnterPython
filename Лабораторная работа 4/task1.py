import json

INPUT = 'input.json'


def task() -> float:
    with open(INPUT) as f:
        object_python = json.load(f)

    multiply = [dict_['score'] * dict_['weight'] for dict_ in object_python]
    sum_of_results = round(sum(multiply), 3)

    return sum_of_results


print(task())
