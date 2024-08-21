# medium

import random
class RandomizedSet:

    def __init__(self):
        # self.lst = []
        self.set1 = set()
        # self.hash1 = dict()

    def insert(self, val: int) -> bool:
        if val not in self.set1:
            self.set1.add(val)
            # self.lst.append(val)
            # self.hash1.update({val: len(self.lst) -1})
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.set1:
            return False

        # self.set1.remove(val)
        # ind = self.hash1[val]
        # tempLst = self.lst[:ind] + self.lst[ind+1:]
        # self.set1.clear()
        # self.set1.update(tempLst)
        self.set1.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.set1))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
