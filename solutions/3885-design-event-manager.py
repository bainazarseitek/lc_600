class EventManager:

    def __init__(self, events: list[list[int]]):
        self.hashmap={}
        self.heap=[]
        for i, p in events:
            self.hashmap[i]=p
            heappush(self.heap, (-p,i))
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.hashmap[eventId]=newPriority
        heappush(self.heap, (-newPriority,eventId))
        

    def pollHighest(self) -> int:
        while self.heap:
            p,i=heappop(self.heap)
            if i in self.hashmap and self.hashmap[i]==-p:
                del self.hashmap[i]
                return i
        return -1
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()