tc = int(input())
A = []
B = []
C = []
D = []
E = []
indx_cnt = []

for i in range(tc):
    N = int(input())
    numA = input()
    numB = input()
    A = [i for i in numA.split(" ")]
    B = [i for i in numB.split(" ")]

    for i in range(N):
        if A[i] != B[i]:
            indx_cnt.append(i)
            C.append(int(A[i]))
            D.append(int(B[i]))

    for i in range(len(C)):
        indxC = C.index(C[i])
        indxD = D.index(C[i])
        E.append(D[indxD])

    if C == E:
        len_idx = len(indx_cnt)
        print((indx_cnt[len_idx-1] - indx_cnt[0])+1)

    E.clear()
    C.clear()
    D.clear()
    indx_cnt.clear()
