# Two-Sum (1)
# 두수의 합

# 덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

# testcase

nums = [2, 7, 11, 15]
target = 9
#result = [0, 1]

# case 1 (브루트 포스)


def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# case 2 (enumerate를 이용한 탐색)

def solution_2(nums, target):
    for idx, num in enumerate(nums):
        subNum = target - num

        if subNum in nums[idx+1:]:
            return [nums.index(num), nums[idx+1:].index(subNum) + (idx + 1)]


if __name__ == '__main__':
    print(solution_2(nums, target))
