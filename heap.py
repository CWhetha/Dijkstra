#Christian Whetham
#270916490

class heap:
 H=[]
 A=[]
 num=0
 sizeh=0 
 def __init__(self, keys,n):
    self.num = n
    self.sizeh=n
    x = n
    self.A=keys #keys store the weight of the vertices each index is the vertice value
    y=0
    self.H.append(None)
    while y <= (2*n)-2: #create the initial heap array with index 0 being null
       self.H.append(0)
       y=y+1
    while x <= ((2*n)-1):#set the last n indeces to be the verices values
       self.H[x]=x-n+1
       x=x+1
    x=self.num-1
    while x >= 1: # creates the heap
      if (self.A[self.H[2*x]] < self.A[self.H[(2*x)+1]]):
            self.H[x]=self.H[2*x]
      else:
            self.H[x]=self.H[(2*x)+1]
      x=x-1
 def inHeap(self,id):
   v=0
   for x in self.H:
      if v==id:
         return True
      v=v+1
   return False
 
 def minKey(self):
    return self.A[self.H[1]]
 
 def minId(self):
    return self.H[1]
 
 def key(self,id):
    return self.A[id]
 
 def deleteMin(self):
    self.A[0] =10000000000 #large value used to complete comparisons for removal 
    self.H[self.H[1]+self.num-1]=0 #sets the smallest value to point to our infinite
    v=self.H[1]	#stores the vertex number to be returned
    i=(self.H[1]+self.num-1)//2
    while i>=1: #reheapify's the heap
       if self.A[self.H[2*i]] < self.A[self.H[(2*i)+1]]:		
           self.H[i]=self.H[2*i]
       else:
           self.H[i]=self.H[(2*i)+1]
       i=i//2
    self.sizeh=self.sizeh-1
    return v	

 def decreaseKey(self,id,newkey): 
  if newkey<self.A[id]: # only changes if the new key is smaller
    self.A[id]=newkey #sets the new key value
    id=(id+self.num-1)//2
    while id>=1:#reheapify's the heap
       if self.A[self.H[2*id]] < self.A[self.H[(2*id)+1]]:
             self.H[id]=self.H[2*id]
       else:
           self.H[id]=self.H[(2*id)+1]	
       id=id//2
	
 def size(self):#returns the current size of the heap
   return self.sizeh

