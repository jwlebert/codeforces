num_test_case = int(input())

test_cases = []
for n in range(num_test_case):
    _ = input()
    test_cases.append(tuple(map(int, tuple(input()))))

good_ct = 0
for test_case in test_cases:
    # trying to check if sum = len, <=> sum - len = 0
    # so basic prefix sum, but account for length (-1 each number)

    adj_test_case = [n - 1 for n in test_case] # test case adjusted for len
    prefix_sum = [0] * (len(test_case) + 1)

    for i, n in enumerate(test_case, start=1):
        prefix_sum[i] = prefix_sum[i - 1] + n
        if prefix_sum[i] == 0: # when zero, is equal
            good_ct += 1

print(good_ct)