class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None # Pointer!
        self.length: int = 0
    
    # Insertion
        
    def prepend(self, data) -> None:
        node = Node(data)
        self.length += 1
        
        # Swap operation
        node.next = self.head
        self.head = node
    
    def append(self, data) -> None:
        node = Node(data)
        self.length += 1
        
        # First, check if list is empty
        if self.head is None:
            self.head = node
            return
        
        # Otherwise, iterate through the list until last node is found
        # Then, append node to it
        t = self.head
        while t.next:
            t = t.next
        t.next = node
        
    def insert(self, data, index) -> None:
        
        if index < 0:
            print(f"Given index must be non-negative.")
            return
        
        if index > self.length:
            print(f"Given index ({index}) is out of bounds. Current list length is {self.length} (remember it's zero-indexed.)")
            return
            
        # Passing all checks...
        self.length += 1
        
        if index == self.length:
            self.append(data)
        elif index == 0:
            self.prepend(data)
        else:
            p = t = self.head
            i = 0
            
            while i != index:
                if i != 0:
                    p = p.next
                t = t.next
                i += 1
            
            p.next = Node(data)
            p.next.next = t
            return     
    
    # Deletion
    
    def pop(self, index: int) -> (str | Node):
        
        # Error handling
        if self.head is None:
            return "List is empty!"

        if index < 0:
            # Assume it's a negative index, perhaps?
            index += self.length
        
        if index >= self.length:
            return f"Your index ({index}) is out of bounds. Current list length is {self.length} (remember it's zero-indexed.)"
        
        # Passing all checks...
        self.length -= 1
        
        if index == 0:
            node = self.head
            self.head = self.head.next
            return node
        
        # For higher indexes
        p = t = self.head # Temporary pointers
        i = 0 # Index
        while i != index:
            if i != 0:
                p = p.next
            t = t.next
            i += 1
            
        p.next = t.next
        return t

    # Search
    
    def find(self, data) -> (int | None):
        
        if self.head is None:
            print("Linked list is empty.")
            return None

        t = self.head
        i = 0
        while t.next:
            if data == t.data:
                print(f"Found node with data = {data} at index {i}.")
                return i
            t = t.next
            i += 1
        
        print(f"Node with data = {data} wasn't found in linked list.")
        return None
    
    def at(self, index: int) -> (Node | None):
        if self.head is None:
            print("Linked list is empty.")
            return None
        
        if index < 0:
            index += self.length
    
        if index >= self.length:
            return f"Your index ({index}) is out of bounds. Current list length is {self.length} (remember it's zero-indexed.)"
        
        # Passing all checks...
        if index == 0:
            return self.head
        
        # For higher indexes
        t = self.head
        i = 0 # Index
        while i != index:
            t = t.next
            i += 1

        return t

    
    # Everything else?
    
    def print_elements_in_list(self):
        
        # Iterate through every node in list, printing it
        t = self.head
        while t:
            print(f"[{t.data}]", end = "", sep = " - ")
            t = t.next
        print()
        
    
    
    # Aliases?
    insert_at_the_beginning = prepend
    insert_at_the_end = append
    delete_at = pop

linked_list = LinkedList()
for i in range(10):
    linked_list.append(i)
linked_list.print_elements_in_list()
print(linked_list.pop(-3))
print(linked_list.pop(0))
print(linked_list.pop(5))
print(linked_list.pop(2))
linked_list.print_elements_in_list()
linked_list.insert("let", 1)
linked_list.insert("sleeping", 5)
linked_list.insert("foxes", 6)
linked_list.insert("lie", 9)
linked_list.print_elements_in_list()
print(linked_list.length)
linked_list.find(10)
print(linked_list.at(linked_list.find("foxes")))
print(linked_list.at(-2))