#  Group Anagrams(49)
#  그룹 에너그램

import collections

# testcase
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def solution(strs):
    word_Anagram = collections.defaultdict(list)

    for word in strs:
        word_Anagram[''.join(sorted(list(word)))].append(word)

    result = list(word_Anagram.values())

    return result


if __name__ == "__main__":
    print(solution(strs))
