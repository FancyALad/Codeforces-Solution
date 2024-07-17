def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort(reverse=True)
    j = 0
    for x in a:
        while j < m and b[j] >= x:
            print(b[j], end=' ')
            j += 1
        print(x, end=' ')
    while j < m:
        print(b[j], end=' ')
        j += 1
    print()

check = int(input())
for _ in range(check):
    solve()
