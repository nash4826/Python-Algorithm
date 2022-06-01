# Combinations(77)
# 조합
# 전체 수 n을 입력받아 k개의 조합을 리턴하라

# testcase
n = 4
k = 2
# result = [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# n! / (k! * (n-k)!)


def sol(n, k):
    result = []

    def dfs(element, start, k):
        if k == 0:
            result.append(element[:])
            return

        for i in range(start, n+1):
            element.append(i)
            dfs(element, i+1, k-1)
            element.pop()

    dfs([], 1, k)
    return result


print(sol(n, k))
