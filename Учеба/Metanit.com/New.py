people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]

for person in people:
    for item in person:
        print(item, end=" | ")
    print()
print(abs(float(input())))