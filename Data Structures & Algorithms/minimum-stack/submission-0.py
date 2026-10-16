class MinStack:

    def __init__(self):
        self.main=[]
        self.mins=[]
        

    def push(self, val: int) -> None:
        low= self.mins[-1] if self.mins else val
        self.main.append(val)
        self.mins.append(min(val,low))


    def pop(self) -> None:
        self.mins.pop()
        self.main.pop()

        

    def top(self) -> int:
        return self.main[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
