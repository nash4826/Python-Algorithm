# Reorder Data in Log Files(937)
# 로그 파일 재정렬

# 기준
# 1. 로그의 가장 앞 부분은 식별자이다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.

# test case
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

#output = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


def solution(logs):
    letter = []
    digit = []

    for log in logs:
        if log.split()[1].isdigit():
            digit.append(log)
        else:
            letter.append(log)

    letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letter + digit


if __name__ == "__main__":
    result = solution(logs)
    print(result)
