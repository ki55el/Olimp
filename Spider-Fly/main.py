def shift(a, b, c):
    if b[2] == b[1] or a[2] == 0 or a[2] == a[0]:
        return rect(c, a, b)
    elif c[2] == 0 or c[2] == c[0]:
        return rect(a, b, c)
    else:
        if a[1] + a[2] > a[0] or b[1] + b[2] > b[0]:
            return coun_rev(c, b, a)
        else:
            return rev(c, b, a)

def rect(a, b, c):
    return (pow(a[1] - a[2], 2) + pow(abs(b[1] - b[2]) + abs(c[1] - c[2]), 2)) ** 0.5

def coun_rev(a, b, c):
    return (pow(a[1] - a[2], 2) + pow((b[0] - b[1]) + (b[0] - b[2]) + (c[0] - c[1]) + (c[0] - c[2]), 2)) ** 0.5

def rev(a, b, c):
    return (pow(a[1] - a[2], 2) + pow((b[1] + b[2]) + (c[1] + c[2]), 2)) ** 0.5


x, y, z = [0] * 3, [0] * 3, [0] * 3
with open('Input.txt', 'r') as Inp:
    for i in range(3):
        x[i], y[i], z[i] = map(int, Inp.readline().split())

if x[1] == 0 or x[1] == x[0]:
    ans = shift(y, x, z)
elif y[1] == 0 or y[1] == y[0]:
    ans = shift(x, y, z)
elif z[1] == 0 or z[1] == z[0]:
    ans = shift(y, z, x)

with open('Output.txt', 'w') as Outp:
    Outp.write(str(round(ans, 3)))
