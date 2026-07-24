with open("acids.txt", "r") as f:
    acids = f.readline().strip()

blosum50=[]
with open("blosum50.txt", "r") as f:
    for i in range(20):
        blosum50.append(list(map(int, f.readline().split())))

gp = -8

def distance(i, j):
    if i == '_' or j == '_':
        return gp
    return blosum50[acids.index(i)][acids.index(j)]

def MaxScore(x, y):
    maxdp, mxi, mxj = 0, 0, 0
    dp = [[None]*(len(y)+1) for i in range(len(x)+1)]
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = max(0,
                               dp[i-1][j-1]+distance(x[i-1], y[j-1]),
                               dp[i][j-1]+gp,
                               dp[i-1][j]+gp)
            if dp[i][j] > maxdp:
                maxdp = dp[i][j]
                mxi, mxj = i, j
    i, j = mxi, mxj
    x_align = []
    y_align = []
    while dp[i][j]:
        if dp[i][j] == dp[i-1][j]+gp:
            x_align.append(x[i-1])
            y_align.append('_')
            i -= 1
        elif dp[i][j] == dp[i][j-1]+gp:
            x_align.append('_')
            y_align.append(y[j-1])
            j -= 1
        elif dp[i][j] == dp[i-1][j-1]+distance(x[i-1], y[j-1]):
            x_align.append(x[i-1])
            y_align.append(y[j-1])
            i -= 1
            j -= 1
    return maxdp, ''.join(x_align[::-1]), ''.join(y_align[::-1])


if __name__ == '__main__':
    x = 'PAHPEWA'
    y = 'PWQ'
    score,str1,str2 = MaxScore(x, y)
    print(str1,str2,sep='\n')
