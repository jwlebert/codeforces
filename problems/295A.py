arr_len, op_count, q_count = tuple(map(int, input().split()))

numbers = tuple(map(int, input().split()))

operations = []
for _ in range(op_count):
    operations.append(tuple(map(int, input().split())))

queries = [] # l, r; performs operations l, l+1, ..., r once per query
for _ in range(q_count):
    queries.append(tuple(map(int, input().split())))

# start with diff array
q_arr = [0] * op_count
for l, r in queries:
    q_arr[l - 1] += 1
    q_arr[r - 1] += 1

# prefix sum it
for i in range(1, len(q_arr)):
    q_arr[i] += q_arr[i - 1]

# use q_arr to make second diff array to calculate impact of operations
op_arr = [0] * arr_len
for op in q_arr:
    l, r, d = operations[op]
    op_arr[l - 1] += d
    op_arr[r - 1] += d

# prefix sum it
for i in range(1, len(op_arr)):
    op_arr[i] += op_arr[i - 1]

res = []
for i in range(arr_len):
    res.append(numbers[i] + op_arr[i])

print(*res)