#!/usr/bin/python


import os


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_self(self):
        print(self.val, end='')
        if self.next != None:
            print("-->", end='')
            self.next.print_self()
        elif self.next == None:
            print()


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        outlist = ListNode()
        outlist_cur = outlist
        while (l1.next != None or l2.next != None):
            digit = l1.val + l2.val + carry
            carry = 0
            if digit > 9:
                digit -= 10
                carry = 1
            outlist_cur.val = digit
            if l1.next != None and l2.next != None:
                l1 = l1.next
                l2 = l2.next
            elif l1.next == None and l2.next != None:
                l1.val = 0
                l2 = l2.next
            elif l2.next == None and l1.next != None:
                l2.val = 0
                l1 = l1.next
            outlist_cur.next = ListNode()
            outlist_cur = outlist_cur.next
        else:
            digit = l1.val + l2.val + carry
            if digit > 9:
                digit -= 10
                outlist_cur.next = ListNode(1)
            outlist_cur.val = digit
        return outlist


def main():


    test_1a = ListNode(2, ListNode(4, ListNode(3)))
    test_1b = ListNode(5, ListNode(6, ListNode(4)))

    test1 = Solution()

    output1 = test1.addTwoNumbers(test_1a,test_1b)
    output1.print_self()

    test_2a = ListNode()
    test_2b = ListNode()

    test2 = Solution()

    output2 = test2.addTwoNumbers(test_2a,test_2b)
    output2.print_self()

    test_3a = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    test_3b = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    test3 = Solution()

    output3 = test3.addTwoNumbers(test_3a,test_3b)
    output3.print_self()






if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))
        os._exit(1)

