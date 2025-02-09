from lsfl_singly_linked_list import LinkedList, Node

class Queue:
    def __init__(self):
        self.queue: LinkedList = LinkedList()

    def enqueue(self, data) -> None:
        
        # Appending to the end of the linked list
        self.queue.append(data)

    def dequeue(self) -> (str | Node):
        
        if self.queue.length == 0:
            print("Cannot dequeue: queue is empty.")
            return None
        
        # Popping from the beginning of the linked list
        return self.queue.pop(0)
    
    def peek(self):
        
        if self.queue.length == 0:
            print("Cannot peek: queue is empty.")
            return None

        return self.queue.at(0).data

    def __str__(self) -> str:
        s = str()
        t = self.queue.head
        while t:
            s += f"[{t.data}]"
            if t.next:
                s += " - "
            t = t.next
        return s

    # Aliases
    serve = dequeue