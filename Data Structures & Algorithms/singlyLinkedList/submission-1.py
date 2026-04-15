class LinkedList:
    
    def __init__(self):
        self.result = []

    
    def get(self, index: int) -> int:
        if index >= len(self.result):
            return -1 
        else:
            return self.result[index]
        

    def insertHead(self, val: int) -> None:
        self.result = [val] + self.result
        print(self.result)
        

    def insertTail(self, val: int) -> None:
        self.result.append(val)
        print(self.result)

    def remove(self, index: int) -> bool:
        print("index >= len(self.result) == ", index >= len(self.result))
        if index >= len(self.result):
            return False
        
        self.result = self.result[: index] + self.result[index + 1 :] 
        print(self.result)
        return True

    def getValues(self) -> List[int]:
        return self.result
        
