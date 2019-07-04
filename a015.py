from sys import stdin

for line in stdin:
    i, j = line.split()
    i, j = int(i), int(j)
    matrix = list()
    for row in range(i):
        l = list(input().replace(' ', ''))
        matrix.append(l)
    
    for row in range(j):
        for col in range(i):
            print(matrix[col][row], '', end='')
        print()
        