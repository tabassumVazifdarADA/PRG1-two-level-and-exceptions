scores = [[78, 81, 84],
          [55, 54, 62],
          [89, 71, 90]]

print(scores[1])
print(len(scores))
print(len(scores[0]))

print("---")

for row in scores:
    print(row)

print("---")

for row in scores:
    for mark in row:
        print(mark)
