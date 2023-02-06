class Node:

    next = None
    def __init__(self, value):
        self.value=value





class List:

    def __init__(self):
        self.size=0
        self.head=None
        self.tail=None

    def append(self, value):
        new_node = Node(value)

        if self.size == 0:
            self.head =new_node
            self.tail = new_node
            self.size=1
            return

        temp = self.tail
        temp.next = new_node
        self.tail = new_node
        self.size+=1

    def list_to_string(self):
        list_string =''
        current_node=self.head
        print(self.head)
        while current_node.next:
            list_string+=(str(current_node.value)+", ")
            current_node=current_node.next

        list_string+=str(current_node.value)

        return list_string

    def pop(self):
        current_node=self.head
        if self.size == 0:
            return
        elif self.size == 1:
            self.head = None
            self.size=0
            return current_node
        while current_node.next.next:
            current_node=current_node.next

        temp = self.tail
        self.tail = current_node
        self.tail.next = None
        self.size-=1
        return temp.value
        


