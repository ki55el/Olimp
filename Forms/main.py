full = dict()
half = dict()
with open('Input.txt', 'r') as Inp:
    N = int(Inp.readline())
    for i in range(1, N + 1):
        a = Inp.readline().replace(' ', '')
        full[i] = {a[:5], a[5:10], a[10:15], a[15:20],
                   a[19:14:-1], a[14:9:-1], a[9:4:-1], a[4::-1]}
    for j in range(1, 2 * N + 1):
        b = Inp.readline().replace(' ', '')
        half[j] = {b[:5], b[5:10], b[10:15]}
ans = [''] * N
for f in full.items():
    for h in half.items():
        if not h[1] - f[1]:
            ans[f[0]-1] += f'{h[0]} '
with open('Output.txt', 'w') as Outp:
    Outp.write('\n'.join(ans))
