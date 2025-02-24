class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.link = None

def create_linked_list():
    temp = None
    head = None
    n = int(input('Enter the number of nodes required: '))
    for i in range(n):
        ll_data = input(f'Enter the data to be stored in node no. {i+1}: ')   
        if i == 0:
            head = ListNode(ll_data)
            temp = head
        else:
            temp.link = ListNode(ll_data)
            temp = temp.link
    return head

def print_linked_list(head):
    print('The linked list is: ')
    while head:
        print(head.data, ' -> ', end='')
        head = head.link
    print('None')

def reverse_linked_list(head):
    temp_list = []
    while head:
        temp_list.append(head.data)
        head = head.link
    return temp_list[::-1]    

def check_if_converges(list1, list2):
    rev_list1 = reverse_linked_list(list1)
    rev_list2 = reverse_linked_list(list2)
    bigger_list = max(len(rev_list1), len(rev_list2))
    smaller_list = min(len(rev_list1), len(rev_list2))
    if bigger_list == len(rev_list1):
        bigger = 1
        smaller = 2
    else:
        bigger = 2 
        smaller = 1   
    count = 0
    for i in range(min(len(rev_list1), len(rev_list2))):
        if rev_list1[i] == rev_list2[i]:
            count +=1
        else:
            break    
    if count:
        print(f'The linked lists converge at node {bigger_list - count + 1} of linked list {bigger} and node {smaller_list - count + 1} of linked list {smaller} ')
    else:
        print('The lists do not converge')            



list1 = create_linked_list()
list2 = create_linked_list()
check_if_converges(list1, list2)
