with open('Input.txt', 'r') as Inp:
    C, A, D, B, E = [list(map(int, Inp.readline().split())) for _ in range(5)]
    C.extend((1, 1))
    A = [A[0]] + sorted(A[1:], reverse=True)
    D.insert(1, 151863)
    B = [B[0]] + sorted(B[1:])

for e in range(C[0]):
    for a in range(A[0]):
        if E[e] >= A[a+1]:
            E[e] -= 1

res = 0
for i in reversed(range(C[0])):
    C[i+1] *= C[i + 2]
    res += C[i+1] * E[i]

ans = [0] * D[0]
for i in reversed(range(D[0])):
    ans[i] = res % D[i + 1]
    res //= D[i+1]

for s in range(D[0]):
    for b in range(B[0]):
        if ans[s] >= B[b + 1]:
            ans[s] += 1

with open('Output.txt', 'w') as Outp:
    Outp.write(' '.join(map(str, ans)))
