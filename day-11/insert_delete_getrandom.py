from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        self.items, self.idxs = [], defaultdict(set) 

    def insert(self, val: int) -> bool:
        self.items.append(val)
        self.idxs[val].add(len(self.items)-1)
        return len(self.idxs[val]) == 1
        

    def remove(self, val: int) -> bool:
        if not self.idxs[val]:
            return False
        out_idx, in_item = self.idxs[val].pop(), self.items[-1]
        self.items[out_idx] = in_item
        self.idxs[in_item].add(out_idx)
        self.idxs[in_item].discard(len(self.items)-1)
        self.items.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.items)
