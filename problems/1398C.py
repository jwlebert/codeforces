num_test_case = int(input())

test_cases = []
for n in range(num_test_case):
    _ = input()
    test_cases.append(tuple(map(int, tuple(input()))))

good_ct = 0
for test_case in test_cases:
    prefix_sum = [0] * (len(test_case) + 1)
    for i, n in enumerate(test_case, start=1):
        # trying to check : sum = len
        # <=> sum - len = 0
        # so each step, sum, but subtract 1 (len increases by 1 each number)
        prefix_sum[i] = prefix_sum[i - 1] + n - 1
        if prefix_sum[i] == 0: 
            good_ct += 1

print(good_ct)