def Shift(A, B, C):
    if B[2] == B[1] or A[2] == 0 or A[2] == A[0]:
        return Rect(C, A, B)
    elif C[2] == 0 or C[2] == C[0]:
        return Rect(A, B, C)
    else:
        if A[1] + A[2] > A[0] or B[1] + B[2] > B[0]:
            return CounRev(C, B, A)
        else:
            return Rev(C, B, A)

def Rect(I, J, K):
    return (pow(I[1] - I[2], 2) + pow(abs(J[1] - J[2]) + abs(K[1] - K[2]), 2)) ** 0.5

def CounRev(I, J, K):
    return (pow(I[1] - I[2], 2) + pow((J[0] - J[1]) + (J[0] - J[2]) + (K[0] - K[1]) + (K[0] - K[2]), 2)) ** 0.5

def Rev(I, J, K):
    return (pow(I[1] - I[2], 2) + pow((J[1] + J[2]) + (K[1] + K[2]), 2)) ** 0.5


X = [0] * 3
Y = [0] * 3
Z = [0] * 3
with open('Input.txt', 'r') as Inp:
    for i in range(3):
        X[i], Y[i], Z[i] = map(int, Inp.readline().split())

if X[1] == 0 or X[1] == X[0]:
    ans = Shift(Y, X, Z)
elif Y[1] == 0 or Y[1] == Y[0]:
    ans = Shift(X, Y, Z)
elif Z[1] == 0 or Z[1] == Z[0]:
    ans = Shift(Y, Z, X)
print(round(ans, 3))
with open('Output.txt', 'w') as Outp:
    Outp.write(str(round(ans, 3)))
    Outp.close()