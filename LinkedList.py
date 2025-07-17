class LinkedListMerger:
    def mergeTwoLists(self, first_list: Optional[ListNode], second_list: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a placeholder node to act as the starting point for building the result
        current_node = dummy_head = ListNode()
        
        # Compare nodes from both lists and connect them in ascending order
        while first_list and second_list:               
            if first_list.val < second_list.val:
                current_node.next = first_list
                first_list, current_node = first_list.next, first_list
            else:
                current_node.next = second_list
                second_list, current_node = second_list.next, second_list
                
        # Connect any remaining nodes from the non-exhausted list
        if first_list or second_list:
            current_node.next = first_list if first_list else second_list
            
        # Return the constructed merged list, excluding the placeholder node
        return dummy_head.next
