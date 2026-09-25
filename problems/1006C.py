_, nums = input(), tuple(map(int, input().split()))

# question amounts to just sliding inwards, and chequing equality.
# the 2nd part is mostly unimportant, but it means you don't need to use everything

max_sum = 0
sum1, sum2 = nums[0], nums[-1]
l, r = 0, len(nums) - 1
while l < r:
    if sum2 < sum1:
        r -= 1
        sum2 += nums[r]
        continue

    if sum1 == sum2:
        max_sum = sum1
    l += 1
    sum1 += nums[l]

print(max_sum)