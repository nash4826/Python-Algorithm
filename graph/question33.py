# 전화 번호 문자 조합(17)
# 2에서 9까지 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 조합을 출력하라

def sol(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            for j in phone[digits[i]]:
                dfs(i+1, path+j)

    if not digits:
        return []

    phone = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    result = []
    dfs(0, "")

    return result


print(sol("2"))
