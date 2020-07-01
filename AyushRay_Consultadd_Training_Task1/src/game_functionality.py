global count
count = 0


def dfs(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == '0':
        return 0

    global count
    matrix[i][j] = '0'
    count += 1
    dfs(matrix, i + 1, j)
    dfs(matrix, i - 1, j)
    dfs(matrix, i, j + 1)
    dfs(matrix, i, j - 1)
    return 1


def game_functionality(matrix):
    if not matrix:
        return []

    global count

    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count = 0
            if matrix[i][j] == '1':
                dfs(matrix, i, j)
            result.append(count)

    return result
