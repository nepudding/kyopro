
Copy
Copy
class uni:
    def __init__(self,n):
        self.n = n
        self.pare = [i for i in range(n)]
        self.rank = [0]*n
 
    def find(self,x):
        if self.pare[x] == x:
            return x
        else:
            self.pare[x] = self.find(self.pare[x])
            return self.pare[x]
 
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.pare[x] = y
        else:
            self.pare[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
 
    def show(self):
        return self.pare