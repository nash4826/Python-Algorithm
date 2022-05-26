# Trapping Rain Water(42) => 난이도 상(가장 어려웠음)
# 빗물 트래핑

# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산해라

# testcase

height = [4, 2, 0, 3, 2, 5]
#result = 9


def solution(height):
    if not height:
        return 0

    result = 0
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(
            height[right], right_max)

        if left_max <= right_max:
            result += left_max - height[left]
            left += 1
        else:
            result += right_max - height[right]
            right -= 1

    return result


if __name__ == '__main__':
    print(solution(height))


# 후기
# 그림을 확인해보면 구해야하는게 무엇인지 단번에 확인할 수 있었다. 그러나 결과값 산출을 위한 구현은 감이 잡히지 않았다.
# 투포인터 기법으로 left,right라는 인덱스 변수를 height배열에 사용하여 해당 배열의 요소값을 left_max,right_max 라는 변수에 할당하고 max()함수를 이용해여 최대값을 유지한후 result라는 변수에 left_max or right_max의 값과 배열의 left or right 값을 빼서 고저차를 구하는 문제이다.
