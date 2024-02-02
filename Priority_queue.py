class PriorityQueue: 
    def __init__(self): 
        self.items = []
    def is_empty(self): 
        return len(self.items)==0
    def push(self,data,priority): 
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    def pop(self): 
        if self.is_empty(): 
            raise IndexError("queue is empty")
        return self.items.pop(0)[0]
    def size(self): 
        return len(self.items)
P=PriorityQueue()
P.push(2,4)
P.push(4,7)
P.push(6,2)
P.push(1,4)
P.push(5,1)
P.push(1,4)
while not P.is_empty():
    print(P.pop())