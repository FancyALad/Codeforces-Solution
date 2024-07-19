# submission link: https://codeforces.com/contest/1243/submission/271325761

def solve():
    n = int(input())
    s = input()
    t = input()
    ci = -1
    flag = False
    for i in range(n):
        if s[i] != t[i]:
            if ci == -1:
                ci = i
            elif flag:
                flag = False
                break
            elif s[i] == s[ci] and t[i] == t[ci]:
                flag = True
            else:
                break
    print("Yes" if flag else "No")

check = int(input())
for _ in range(check):
    solve()
