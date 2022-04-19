

class Solution:
    # Write your code here
    def __init__(self):
        self.stack=[]
        self.queue=[]
    def pushCharacter(self,c):
        self.stack.append(c)
    def enqueueCharacter(self,c):
        self.queue.append(c)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop(0)
        
