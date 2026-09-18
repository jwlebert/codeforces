arr_len, op_count, q_count = tuple(map(int, input().split()))

numbers = tuple(map(int, input().split()))

operations = []
for _ in range(op_count):
    operations.append(tuple(map(int, input().split())))

queries = [] # l, r; performs operations l, l+1, ..., r once per query
for _ in range(q_count):
    queries.append(tuple(map(int, input().split())))

# start with diff array
q_arr = [0] * (op_count + 1)
for l, r in queries:
    q_arr[l - 1] += 1
    q_arr[r] -= 1 # undo 1 after the range ends

# prefix sum it
for i in range(1, len(q_arr)):
    q_arr[i] += q_arr[i - 1]
op_application_count = q_arr[:len(q_arr) - 1]

# use q_arr to make second diff array to calculate applications of operations
op_arr = [0] * (arr_len + 1)
for i, op in enumerate(q_arr):
    l, r, d = operations[i]
    op_arr[l - 1] += op
    op_arr[r] -= op # stop 1 after the range ends

# prefix sum it
for i in range(1, len(op_arr)):
    op_arr[i] += op_arr[i - 1]

add_arr = [
    n * operations[i][2] for i, n in enumerate(op_arr)
]

res = []
for i in range(arr_len):
    res.append(numbers[i] + add_arr[i])

print(*res)