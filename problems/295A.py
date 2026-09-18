arr_len, op_count, q_count = map(int, input().split())

operations = []
for _ in range(op_count):
    operations.append(tuple(map(int, input().split())))

queries = []
for _ in range(q_count):
    queries.append(tuple(map(int, input().split())))

