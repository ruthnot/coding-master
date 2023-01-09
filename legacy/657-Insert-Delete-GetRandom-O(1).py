import random

class RandomizedSet:

    def __init__(self):

    # do intialization if necessary
        self.nums, self.valToindexDict = [], {}


    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """


    def insert(self, val):

    # write your code here
        if val in self.valToindexDict:
            return False
        self.nums.append(val)
        self.valToindexDict[val] = len(self.nums) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):

    # write your code here
        if val not in self.valToindexDict:
            return False
        remove_idx = self.valToindexDict[val]
        if remove_idx < len(self.nums) - 1:
            self.nums[remove_idx] = self.nums[-1]
            self.valToindexDict[self.nums[-1]] = remove_idx

        del self.valToindexDict[val]
        self.nums.pop()
        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
# write your code here
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()