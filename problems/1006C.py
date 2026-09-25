_, nums = input(), tuple(map(int, input().split()))

max_sum = 0
sum1, sum2 = nums[0], nums[-1]
l, r = 0, len(nums) - 1
while l < r:
    if sum1 == sum2:
        max_sum = sum1

        l += 1
        sum1 += nums[l]
    elif sum1 < sum2:
        l += 1
        sum1 += nums[l]
    elif sum2 < sum1:
        r -= 1
        sum2 += nums[r]
print(max_sum)