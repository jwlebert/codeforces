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

    prefix_freq = {}
    prefix_sum = [0] * (len(test_case) + 1)
    for i, n in enumerate(test_case, start=1):
        prefix = prefix_sum[i - 1] + n

        if prefix == 0 or prefix in prefix_freq: 
            good_ct += 1 + prefix_freq[prefix]

        prefix_sum[i] = prefix
        prefix_freq[prefix] = prefix_freq.get(prefix, 0) + 1


print(good_ct)