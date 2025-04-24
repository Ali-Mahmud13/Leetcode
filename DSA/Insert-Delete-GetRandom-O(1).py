import random
class RandomizedSet(object):

    def __init__(self):
        self.arr=[]
        self.hasht={}
        

    def insert(self, val):
        \\\
        :type val: int
        :rtype: bool
        \\\
        if val in self.hasht:
            return False
        self.arr.append(val)
        self.hasht[val]= len(self.arr)-1
        return True

        

    def remove(self, val):
        \\\
        :type val: int
        :rtype: bool
        \\\
        if val not in self.hasht:
            return False
        index = self.hasht[val]
        lastelement=self.arr[-1]
        self.arr[index]= lastelement
        self.hasht[lastelement]=index

        self.arr.pop()
        del self.hasht[val]
        return True


        

    def getRandom(self):
        \\\
        :rtype: int
        \\\
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()