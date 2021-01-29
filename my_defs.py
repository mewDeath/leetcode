# -*- coding: utf-8 -*-
# @Author  : mew

# Definition for singly-linked list.
# ... from leetcode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# by mew
class myList:
    """ 自定义单向链表
    >>> a = myList([1, 2,3, 4, 5])
    >>> a.to_list()
    [1, 2, 3, 4, 5]

    """

    def __init__(self, lst: list = None):
        self._head = ListNode()
        self._tail = self._head
        if lst is None: lst = []
        for i in lst:
            self._tail.next = ListNode(i)
            self._tail = self._tail.next

    @property
    def first_node(self):
        return self._head.next

    def __iter__(self, cur: ListNode = None) -> ListNode:
        if cur is None: cur = self._head.next
        while cur:
            yield cur
            cur = cur.next

    def to_list(self):
        return [i.val for i in self]