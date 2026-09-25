num_test_case = int(input())

test_cases = []
for n in range(num_test_case):
    _ = input()
    test_cases.append(tuple(map(int, tuple(input()))))

for test_case in test_cases:
    good_sub_arr_ct = 0
    # trying to check if sum = len, <=> sum - len = 0
    # so basic prefix sum, but account for length (-1 each number)
    adj_test_case = [n - 1 for n in test_case] # test case adjusted for len

    prefix_freq = {0: 1}
    prefix_sum = [0] * (len(test_case) + 1)
    for i, n in enumerate(adj_test_case, start=1):
        prefix = prefix_sum[i - 1] + n

        # 0 is always in freq, so always true when prefix == 0
        if prefix in prefix_freq:
            # good array when the subarray's prefix is 0.
            # we are only counting prefix sum starting at first pos

            # we take advantage of : sum(l, r) = p[r] - p[l - 1]
            # i.e., if you have prefix sum from 1, ..., l, ..., r, can remove
            #       prefix sum of 1, ..., l to get pref. sum for l + 1, ..., r
            
            # thus, the frequency of a given prefix is the number of subarrays we can
            # create which will be equal to 0
            good_sub_arr_ct += prefix_freq.get(prefix, 0)

        prefix_sum[i] = prefix
        prefix_freq[prefix] = prefix_freq.get(prefix, 0) + 1
    print(good_sub_arr_ct)