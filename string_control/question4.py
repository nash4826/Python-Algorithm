# Most Common Word(819)
# 가장 흔한 단어

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력
# 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

import collections
import re

# testcase
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# Output: "ball"

# 내가 푼 솔루션


def solution(paragraph, banned):
    words = re.sub(r'[^a-zA-Z0-9]', ' ', paragraph).lower().split()

    word_temp = []

    for word in words:
        if word not in banned:
            word_temp.append(word)

    result = collections.Counter(word_temp)

    return result.most_common(1)[0][0]

# 리스트 컴프리핸션 사용시


def solution_two(paragraph, banned):
    words = [word for word in re.sub(
        r'[^a-zA-Z0-9]', ' ', paragraph).lower().split() if word not in banned]

    result = collections.Counter(words)
    return result.most_common(1)[0][0]


if __name__ == "__main__":
    print(solution_two(paragraph, banned))
