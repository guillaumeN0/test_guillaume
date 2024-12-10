import csv
import re
import numpy as np

with open("input.txt", "r", encoding="utf-8") as f:
    matrix = np.array([list(line.strip()) for line in f.readlines()])


total = 0
n = matrix.shape[0]

for i in range(n):
    cadena = "".join(matrix[i, :])
    total += len(re.findall("(?=(XMAS|SAMX))", cadena))
    cadena = "".join(matrix[:, i])
    total += len(re.findall("(?=(XMAS|SAMX))", cadena))
    cadena = "".join(np.diag(matrix, k=i + 1))
    total += len(re.findall("(?=(XMAS|SAMX))", cadena))
    cadena = "".join(np.diag(matrix, k=-i - 1))
    total += len(re.findall("(?=(XMAS|SAMX))", cadena))
cadena = "".join(np.diag(matrix))
total += len(re.findall("(?=(XMAS|SAMX))", cadena))

matrix = np.fliplr(matrix)
for i in range(n):
    cadena = "".join(np.diag(matrix, k=i + 1))
    total += len(re.findall("(?=(XMAS|SAMX))", cadena))
    cadena = "".join(np.diag(matrix, k=-i - 1))
    total += len(re.findall("(?=(XMAS|SAMX))", cadena))
cadena = "".join(np.diag(matrix))
total += len(re.findall("(?=(XMAS|SAMX))", cadena))

print(total)


def is_xmas(i, j):
    if (matrix[i - 1, j - 1] == "M" and matrix[i + 1, j + 1] == "S") or (
        matrix[i - 1, j - 1] == "S" and matrix[i + 1, j + 1] == "M"
    ):
        if (matrix[i - 1, j + 1] == "M" and matrix[i + 1, j - 1] == "S") or (
            matrix[i - 1, j + 1] == "S" and matrix[i + 1, j - 1] == "M"
        ):
            return 1
    return 0


total_mas = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if matrix[i, j] == "A":
            total_mas += is_xmas(i, j)

print(total_mas)
