check = int(input())
for _ in range(check):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    left = [0] * (n + 1)
    left[2] = 1
    x = nums[2] - nums[1]
    for i in range(3, n + 1):
        y = nums[i] - nums[i - 1]
        left[i] = left[i - 1] + (1 if y < x else y)
        x = y
    right = [0] * (n + 1)
    right[n - 1] = 1
    x = nums[n] - nums[n - 1]
    for i in range(n - 2, 0, -1):
        y = nums[i + 1] - nums[i]
        right[i] = right[i + 1] + (1 if y < x else y)
        x = y
    # print(nums)
    # print(left, right)

    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split(' '))
        if x < y:
            print(left[y] - left[x])
        else:
            print(right[y] - right[x])
