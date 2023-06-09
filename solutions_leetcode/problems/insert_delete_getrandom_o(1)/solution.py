class RandomizedSet:

    def __init__(self):
        self.i = -1
        self.x = []

    def insert(self, val: int) -> bool:
        if val in self.x:
            return False
        self.x.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.x:
            self.x.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.x)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()