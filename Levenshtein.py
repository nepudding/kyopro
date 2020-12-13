def Levenshtein(str1,str2):
    N,M = len(str1), len(str2)
    DP = [[0]*(M+1) for i in range(N+1)]
    for i in range(N):
        DP[i][0] = i
    for i in range(M):
        DP[0][i] = i
    for i in range(1,N):
        for j in range(1,M):
            DP[i][j] = min(DP[i][j-1],DP[i-1][j])
            if str1[i-1] != str2[j-1]:
                DP[i][j] += 1
    return DP[-1][-1]