empl = dict()
names = dict()
with open('Input.txt', 'r') as Inp:
    for count, line in enumerate(iter(Inp.readline, 'END\n')):
        if count % 2 == 0:
            boss = line.strip().split(' ', 1)
        else:
            sub = line.strip().split(' ', 1)
            try:
                empl[boss[0]].append(sub[0])
            except KeyError:
                empl[boss[0]] = [sub[0]]
    BOSS = [Inp.readline()]
ans = []
while set(BOSS) & set(empl.keys()):
    res = []
    for i in BOSS:
        try:
            ans.extend(empl[i])
            res.extend(empl[i])
        except KeyError:
            pass
    BOSS = res
print(ans)
with open('Output.txt', 'w') as Outp:
    Outp.write('\n'.join(ans))
    Outp.close()
