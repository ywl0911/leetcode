r = []
n = 4
k = 2


def dfs(read_list):
    if len(read_list) == k:
        r.append(read_list)

    for i in range(1, n + 1):
        if i in read_list:
            continue
        dfs(read_list + [i])


dfs([])
print(r)
