def rot90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

Inp = open("Input.txt")
n, m = map(int, Inp.readline().split())
x, y, z = map(int, Inp.readline().split())
i = 0
while i < m:
    i += 1
    a, k, s = Inp.readline().split()
    k = int(k)
    s = int(s)
    if (a == "X") and (x == k):
        mas = [0] * n
        for j in range(n):
            mas[j] = [0] * n
        mas[y - 1][z - 1] = 1
        if s == 1:
            mas = rot90(mas)
        else:
            mas = rot90(rot90(rot90(mas)))
        for j in range(n):
            for l in range(n):
                if mas[j][l] == 1:
                    y = j + 1
                    z = l + 1

    if (a == "Y") and (y == k):
        mas = [0] * n
        for j in range(n):
            mas[j] = [0] * n
        mas[x - 1][z - 1] = 1
        if s == 1:
            mas = rot90(mas)
        else:
            mas = rot90(rot90(rot90(mas)))
        for j in range(n):
            for l in range(n):
                if mas[j][l] == 1:
                    x = j + 1
                    z = l + 1

    if (a == "Z") and (z == k):
        mas = [0] * n
        for j in range(n):
            mas[j] = [0] * n
        mas[x - 1][y - 1] = 1
        if s == 1:
            mas = rot90(mas)
        else:
            mas = rot90(rot90(rot90(mas)))
        for j in range(n):
            for l in range(n):
                if mas[j][l] == 1:
                    x = j + 1
                    y = l + 1

with open('Output.txt', 'w') as Outp:
    Outp.write(f'{x} {y} {z}')

