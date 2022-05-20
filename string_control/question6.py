# Longest Palindromic Substring (5)
# 가장 긴 팰린드롬 부분 문자열
# 가장 긴 팰린드롬 부분 문자열을 출력하라. (체감상 어려웠고, 책의 힘을 빌렸음)


# testcase
# s = "babad"
# result = "bab" or "aba"

# s = "cbbd"
# result = "bb"
s = "babad"


def solution(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result


if __name__ == "__main__":
    print(solution(s))
