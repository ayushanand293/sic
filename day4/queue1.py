import sys

class Queue:
    def __init__(self, size=5):
        self.que = []
        self.size = size
        print('Empty Queue is created')
    
    def insert(self):
        if len(self.que) == self.size:
            print('Queue is full')
            return
        element = input('Enter the element to be inserted: ')
        self.que.insert(0, element)

    def delete(self):
        if not self.que:
            print('Queue is empty')
            return
        print(f'deleted element is {self.que.pop()}')

    def list_queue(self):
        if not self.que:
            print('Queue is empty')
            return
        print('The Queue is \n', self.que) # que[::-1]

class Menu:
    def get_menu(self, queue):
        menu = {
            1 : queue.insert,
            2 : queue.delete,
            3 : queue.list_queue,
            4 : self.end_of_program
        }
        return menu
    
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def run_menu(self):
        queue = Queue()
        while True:
            choice = int(input('1: Insert 2: Delete 3: Display 4:Exit. Your choice: '))
            menu = self.get_menu(queue)
            menu.get(choice, self.invalid_choice)()
    
menu = Menu()
menu.run_menu()