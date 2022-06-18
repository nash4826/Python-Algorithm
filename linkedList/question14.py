# 21. Merge Two Sorted Lists
# 두 정렬 리스트의 병합
# 정렬되어 있는 두 연결 리스트를 합쳐라.

# testcase
# Input: list1 = [1,2,4], list2 = [1,3,4]
# output: [1,1,2,3,4,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol(list1, list2):
    if (not list1) or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1

    if list1:
        list1.next = sol(list1.next, list2)

    return list1
