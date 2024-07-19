# submission link: https://codeforces.com/contest/1243/submission/271339428

def solve():
    n = int(input())
    s = input()
    t = input()
    ci = 0
    flag = -1
    for i in range(n):
        if s[i] != t[i]:
            if flag == -1:
                flag = 0
                ci = i
            elif flag:
                flag = 0
                break
            elif s[i] == s[ci] and t[i] == t[ci]:
                flag = 1
            else:
                break
    print("Yes" if flag == 1 else "No")

check = int(input())
for _ in range(check):
    solve()
