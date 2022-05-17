# Reverse String (문자열 뒤집기)

# input -> s(list) 내부의 조작한다. return은 없다.

# two Pointer냐 reverse 함수, 2가지 방법이 존재
# 하지만 two Pointer로 코딩해보자.

s = ["h", "e", "l", "l", "o"]


def solution(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    solution(s)
    print(s)
