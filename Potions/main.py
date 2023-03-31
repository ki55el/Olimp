with open('Input.txt', 'r') as Inp:
    data = [line.split() for line in Inp.read().split('\n')]

for i in range(len(data)):
    if data[i][0] == 'MIX':
        data[i][0] = 'MX'
        data[i] += ['XM']
    elif data[i][0] == 'WATER':
        data[i][0] = 'WT'
        data[i] += ['TW']
    elif data[i][0] == 'DUST':
        data[i][0] = 'DT'
        data[i] += ['TD']
    elif data[i][0] == 'FIRE':
        data[i][0] = 'FR'
        data[i] += ['RF']
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            data[i][j] = ''.join(data[int(data[i][j]) - 1])

with open('Output.txt', 'w') as Outp:
    Outp.write(''.join(data[i]))
