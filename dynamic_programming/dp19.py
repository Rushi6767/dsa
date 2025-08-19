def lcs(i, j, s1, s2):
    if i < 0 or j < 0:
        return 0

    if s1[i] == s2[j]:
        return 1 + lcs(i-1, j-1, s1, s2)

    return max(
        lcs(i-1, j, s1, s2),
        lcs(i, j-1, s1, s2)
    )


s1 = "abcde"
s2 = "ace"
print(lcs(len(s1)-1, len(s2)-1, s1, s2))


def lcs(i, j, s1, s2, dp):
    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j]:
        dp[i][j] = 1 + lcs(i-1, j-1, s1, s2, dp)
    else:
        dp[i][j] = max(
            lcs(i-1, j, s1, s2, dp),
            lcs(i, j-1, s1, s2, dp)
        )

    return dp[i][j]


s1 = "abcde"
s2 = "ace"
n, m = len(s1), len(s2)
dp = [[-1]*m for _ in range(n)]
print(lcs(n-1, m-1, s1, s2, dp))


s1 = "abcde"
s2 = "ace"
n, m = len(s1), len(s2)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])


s1 = "abcde"
s2 = "ace"
n, m = len(s1), len(s2)

prev = [0]*(m+1)

for i in range(1, n+1):
    curr = [0]*(m+1)
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            curr[j] = 1 + prev[j-1]
        else:
            curr[j] = max(prev[j], curr[j-1])
    prev = curr

print(prev[m])
