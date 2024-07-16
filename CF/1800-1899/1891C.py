def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    s = s_2 = (sum(nums) + 1) // 2
    nums.sort()
    i = 0
    while i < n and s_2 - nums[i] >= 0:
        s_2 -= nums[i]
        i += 1
    ans = n - i + s
    print(ans)

check = int(input())
for _ in range(check):
    solve()
