# 3Sum(15)
# 세수의 합
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

# testcase
nums = [-1, 0, 1, 2, -1, -4]
#result = [[-1,-1,2],[-1,0,1]]

# 머릿속에서 떠오르는 건 브루트포스인데 3중 for문을 써야해서 시간복잡도 O(n^3) 이상이 된다. 아마 시간초과로 Pass되지 않을 것 같다.


def sol(nums):
    result = []
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1

    return result


if __name__ == "__main__":
    print(sol(nums))

# 후기
# 투포인터 기법으로 O(n^2) 정도의 시간복잡도를 가지고 풀 수 있다.
# 곧바로 풀이가 생각날만한 문제는 아닌것 같다.
# 코드의 흐름은 이해했으나, 단번에 해결방식이 떠오르지 못하는게 문제다.
