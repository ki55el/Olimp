def counter(pos):
    I = int(Inp.readline())
    edge = dict()
    for _ in range(I):
        b, k = Inp.readline().split()
        edge[b] = [b for _ in range(int(k))]
    coll = []
    for w in range(len(words)):
        for e in edge.keys():
            if words[w][pos] == e and edge[e]:
                coll.append(edge[e].pop())
                break
    return len(coll)


with open('Input.txt', 'r') as Inp:
    N = int(Inp.readline())
    words = [Inp.readline().strip() for _ in range(N)]
    f = counter(0)
    l = counter(-1)
with open('Output.txt', 'w') as Outp:
    Outp.write(str(min(f, l)))
