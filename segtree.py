import math

class segtree:
    def __init__(self,size,calc):
        n = 1
        self._calc = calc
        while n < size:
            n *= 2
        self.node = [0]*(2*n+10)
        self.begin = n

    def update(self,dex,value):
        dex += self.begin-1
        self.node[dex] = value
        while dex > 0:
            dex = (dex-1)//2
            self.node[dex] = calc(self.node[dex*2+1], self.node[dex*2+2])
    
    def segment(self,l,r):
        l += self.begin-1
        r += self.begin-1
        ans = 0
        while l <= r:
            if l==0:
                ans = self.node[0]
                break
            if l%2 == 0:
                ans = calc(ans,self.node[l])
            l//=2
            if r%2 == 1:
                ans = calc(ans,self.node[r])
            r = r//2 -1
        return ans 

    def view(self):
        return  self.node


