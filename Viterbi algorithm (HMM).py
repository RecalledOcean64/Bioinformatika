from math import log,exp

ev=[]   # emisijske vrijednosti
with open("kocke_e.txt", "r") as f1:
    for line in f1.readlines():
        ev.append(list(map(float, line.split())))

tv=[]   # tranzicijske vrijednosti
with open("kocke_t.txt", "r") as f1:
    for line in f1.readlines():
        tv.append(list(map(float, line.split())))

pi_l = pi_f = 0.5


def decode(x):
    x = list(map(lambda c: int(c)-1, x))
    dp = [[None] * len(x) for _ in range(2)]
    dp[0][0] = log(ev[0][x[0]]) + log(pi_f)
    dp[1][0] = log(ev[1][x[0]]) + log(pi_l)
    for i in range(1, len(x)):
        for j in range(2):
            dp[j][i] = log(ev[j][x[i]]) + max(dp[0][i-1] + log(tv[0][j]),
                                              dp[1][i-1] + log(tv[1][j]))
    if dp[0][len(x) - 1] > dp[1][len(x) - 1]:
        pos = [len(x) - 1, 0]
    else:
        pos = [len(x) - 1, 1]

    res = ''

    while pos[0]:
        res += 'FL'[pos[1]]
        if dp[0][pos[0]-1] + log(tv[0][pos[1]]) > dp[1][pos[0]-1] + log(tv[1][pos[1]]):
            pos[1] = 0
        else:
            pos[1] = 1
        pos[0] -= 1
    res += 'FL'[pos[1]]

    return res[::-1]


x = '12345666612345'
print(decode(x), sep='\n')
