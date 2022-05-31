#순열 (46)

# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라

nums = [1, 2, 3]

#result = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


def sol(nums):
    result = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            print(next_elements)
            next_elements.remove(e)

            prev_elements.append(e)
            print(f'prev : {prev_elements}')
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result


print(sol(nums))
