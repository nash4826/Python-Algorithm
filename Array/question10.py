# Array Partition I(561)
# 배열 파티션 I

# n개의 페어를 이용한 min(a,b)의 합으로 만들수 있는 가장 큰 수를 출력하라

# testcase

nums = [1, 4, 3, 2]
#result = 4


def sol(nums):
    nums.sort()
    result = 0
    two = []
    for num in nums:
        two.append(num)
        if(len(two) == 2):
            result += min(two)
            two = []

    return result


if __name__ == "__main__":
    print(sol(nums))
