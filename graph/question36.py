# Combination Sum(39)
# 조합의 합
# 숫자 집합 Candidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열가능.

# testcase
candidates = [2, 3, 6, 7]
target = 7
# result = [[2,2,3],[7]]


def sol(candidates, target):
    result = []

    def dfs(csum, idx, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        for i in range(idx, len(candidates)):
            dfs(csum - candidates[i], i, path+[candidates[i]])

    dfs(target, 0, [])
    return result


print(sol(candidates, target))
