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

def insert_at_pos(current):
    temp = None
    pos = int(input('Enter the position of the node to be added: '))
    for i in range(pos - 1):
        temp = current 
        current = current.link 
    input_data = input('Enter the data to be added: ')
    temp.link = ListNode(input_data)
    temp.link.link = current

def delete_at_pos(head):
    current = head
    temp = None
    pos = int(input('Enter the position of the node to be deleted: '))
    if pos == 0 :
        return current.link
    for i in range(pos - 1):
        temp = current 
        current = current.link 
    print(f'Data being deleted is {current.data}')    
    temp.link = current.link
    return head 

def print_reverse_linked_list(head):
    temp_list = []
    print('The reversed linked list is: ')
    while head:
        temp_list.append(head.data)
        head = head.link
    for n in temp_list[::-1]:
        print(n, ' -> ', end = '') 
    print('None')
       


# Example usage:
head = create_linked_list()
print_linked_list(head)
insert_at_pos(head)
print_linked_list(head)
head = delete_at_pos(head)
print_linked_list(head)
print_reverse_linked_list(head)
