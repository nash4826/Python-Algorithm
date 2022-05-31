# Palindrome Linked List(234)
# 펠린드롬 연결리스트

# 연결 리스트가 팰린드롬 구조인지 판별하라

# testcase
#head = [1, 2, 2, 1]
#result = true


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 연결리스트의 value값을 list[]에 넣고 pop작업을 통해 회문 판별(문제가 추구하는 방향인지 모르겠음)

def sol1(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    while len(values) > 1:
        if values.pop(0) != values.pop():
            return False

    return True

# ===============================================

# Runner를 이용한 풀이
# 팰린드롬 연결리스트 문제의 제대로 된 풀이법은 Runner 기법을 활용하는 것이다.


def sol2(head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev
