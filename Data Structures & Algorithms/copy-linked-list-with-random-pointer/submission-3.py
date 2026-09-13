class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        temp = head
        copies = {}
        
        while temp is not None:
            copy = Node(temp.val, None, None)
            copies[temp] = copy
            temp = temp.next

        temp = head

        while temp is not None:
            node = copies[temp]

            if temp.next is not None:
                node.next = copies[temp.next]

            if temp.random is not None:
                node.random = copies[temp.random]

            temp = temp.next
        
        return copies[head]