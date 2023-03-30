with open('Input.txt', 'r') as Inp:
    tk = Inp.readline().split()
Ans = [''] * len(tk)

Start = int(len(tk)/2)
for I in range(len(tk)):
    if I % 2 == 0:
        Dif = I
    else:
        Dif = -I
    Start += Dif

    start = int(len(tk[Start])/2)
    for i in range(len(tk[Start])):
        if i % 2 == 0:
            dif = i
        else:
            dif = -i
        start += dif

        Ans[I] += tk[Start][start]

with open('Output.txt', 'w') as Outp:
    Outp.write(' '.join(Ans))
    Outp.close()
