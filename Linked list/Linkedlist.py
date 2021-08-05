from Node import Node

class Linkedlist:
    def __init__(self) :
        self.head_node = None

    def is_empty(self):
        if(self.head_node == None):
            return True
        else:
            return False
    
    def get_head(self):
        return self.head_node
    
    def print_list(self):
        if(self.is_empty()):
            print('List is empty')
            return False
        temp=self.head_node

        while temp.next_element is not None:
            print(temp.data, end= "->")
            temp=temp.next_element
        print(temp.data, "-> None")
        return True
    
