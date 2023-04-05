empl = dict()
names = dict()
nums = dict()
with open('Input.txt', 'r') as Inp:
    for count, line in enumerate(iter(Inp.readline, 'END\n')):
        if count % 2 == 0:
            try:
                boss, bossname = line.strip().split(' ', 1)
                names[boss] = bossname
                nums[bossname] = boss
            except ValueError:
                boss = line.strip()
                if not(boss in names.keys()):
                    names[boss] = 'Unknown Name'
        else:
            try:
                sub, subname = line.strip().split(' ', 1)
                names[sub] = subname
            except ValueError:
                sub = line.strip()
                if not(sub in names.keys()):
                    names[sub] = 'Unknown Name'
            if boss in empl.keys():
                empl[boss].append(sub)
            else:
                empl[boss] = [sub]
    BOSS = [Inp.readline()]
if BOSS[0] in nums.keys():
    BOSS = [nums[BOSS[0]]]

ans = []
while set(BOSS) & set(empl.keys()):
    res = []
    for t in BOSS:
        if t in empl.keys():
            ans.extend(empl[t])
            res.extend(empl[t])
    BOSS = res
ans = sorted([f'{n} {names[n]}' for n in ans])
if not ans:
    ans = ['NO']
with open('Output.txt', 'w') as Outp:
    Outp.write('\n'.join(ans))
