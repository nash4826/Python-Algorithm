# Subsets(78)
# 부분 집합

# 모든 부분 집합을 리턴하라.

nums = [1, 2, 3]

#result = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


def sol(nums):
    result = []

    def dfs(idx, path):
        result.append(path)

        for i in range(idx, len(nums)):
            dfs(i+1, path+[nums[i]])

    dfs(0, [])
    return result


print(sol(nums))
