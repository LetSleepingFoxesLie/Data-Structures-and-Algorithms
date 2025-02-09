from lsfl_singly_linked_list import LinkedList, Node

class Stack:
    def __init__(self):
        self.stack: LinkedList = LinkedList()
    
    def push(self, data) -> None:
        self.stack.prepend(data)
    
    def pop(self) -> (str | Node):
        
        if self.stack.length == 0:
            print("Cannot pop: stack is empty.")
            return None
        
        return self.stack.pop(0)
    
    def peek(self) -> (str | Node):
        
        if self.stack.length == 0:
            print("Cannot peek: stack is empty.")
            return None

        return self.stack.at(0)
    
    def __str__(self) -> str:
        
        # Reusing code? Yeah.
        s = str()
        t = self.stack.head
        
        while t:
            s += f"[{t.data}]"
            if t.next:
                s += " - "
            t = t.next
        
        return s
    
    # Aliases
    retrieve = pop