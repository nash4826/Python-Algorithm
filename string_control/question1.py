# Valid Palindrome (125)

# input값 s 가 팰린드롬인지 확인하기(회문 문제)

# 조건: 대소문자를 구분하지 않음, 영문자와 숫자만을 대상으로 한다.

import collections
import re

s = "A man, a plan, a canal: Panama"

# [].pop() 은 시간복잡도가 O(1)이나,
# [].pop(0)는 시간복잡도가 O(n)이다.
# solution_list 함수 내의 시간복잡도는 O(n^2)


def solution_list(s):
    s = list(s)
    result = []
    for char in s:
        if char.isalnum():
            result.append(char.lower())

    while len(result) > 1:
        if result.pop(0) != result.pop():
            return False

    return True


# Deque 버전 (collection 모듈 사용)
# Deque.popleft() 는 시간복잡도가 O(1)이다.
# solution_deque 함수의 시간복잡도는 O(n)이며 빠르다.


def solution_deque(s):
    s = list(s)
    result = collections.deque()
    for char in s:
        if char.isalnum():
            result.append(char.lower())

    while len(result) > 1:
        if result.popleft() != result.pop():
            return False

    return True


if __name__ == "__main__":
    print(solution_deque(s))
