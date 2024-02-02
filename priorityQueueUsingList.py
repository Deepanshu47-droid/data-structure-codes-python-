class Node: 
    def __init__(self,item=None,priority=None,next=None):
        self.priority=priority
        self.item=item
        self.next=next 

class PriorityQueue:
    def __init__(self): 
        self.start=None
        self.item_count=0
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority<self.start.priority: 
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<=priority: 
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1

    def is_empty(self): 
        return self.start==None
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data
    def size(self):
        return self.item_count
P=PriorityQueue()
P.push(2,4)
P.push(4,7)
P.push(6,2)
P.push(1,4)
P.push(5,1)
P.push(1,4)
while not P.is_empty():
    print(P.pop())