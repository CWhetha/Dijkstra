from heap import heap
import sys

#Christian Whetham
#270916490

class graph:
  vertices=[]
  weights=[]
  h=[]
  def __init__ (self,num):
      x=1
      while x < int(num)+1: #creates a list of all the vertices
         l=vertex(x)
         self.vertices.append(l)
         x=x+1
      self.vertices[0].setWeight(0)
      self.weights.append(None)
      for w in self.vertices: #creates a list of weights with index 0 being NULL
          self.weights.append(w.getWeight())
      self.h = heap(self.weights, num) #creates a heap from the list 
  
  def setEdge (self,start, end, weight):
     for x in self.vertices:
         if x.getVal()==int(start): #findes the correct vertex to add the edge to
             x.addedge(int(start), int(end),int(weight))
  
  def getVert(self):
    return self.h
  
  def secq(self,v): #returns a vertex at the given positio 
     return self.vertices[v[1]-1]
  
  def updateheap(self,id,w):
     h.decreaseKey(id,w)
  
  def reduce(self, id, weight):  #reduce the weight of a vertex
      self.h.decreaseKey(id,weight)
  
  def getv(self,x):
     return self.vertices[x]
  
  def heapsize (self):
     return self.h.size()
  
  def allvert(self):
     return self.vertices

class vertex:
  edges=[]
  value=2
  weight=1000000
  pred=[]
  def __init__ (self,val):
     self.value=val
     self.edges=[]
     self.weight=1000000
     self.pred=[]
  def getVal(self):
     return self.value
  
  def addedge(self,start,vert, weight):
    c=start,vert,weight #add the edge to this vertex
    self.edges.append(c)
  
  def getedges(self):
     return self.edges
  
  def getWeight(self):
     return self.weight
  
  def setWeight(self,w):
     self.weight=w


f = open(sys.argv[1], "r") #opens the given file
count=0
for x in f: 
  val = x.split()
  if len(val) ==3: # get the edge triples and set them to their vertices
      g.setEdge(val[0],val[1],val[2])
      count=count+1
  else: #for the first line get the number of vertices
      g = graph(int(val[0]))

final=[]
q=g.getVert() #get a list of all the vertices
x=0
while g.heapsize() !=0: #run until the heap is empty
 u=g.getv(g.getVert().deleteMin()-1) #get the smallest vertex from the heap
 x=x+1
 for v in u.getedges(): #go through all of the vertexes edges
     w=u.getWeight()+v[2] #calculate the weight to go from the current vertix to the new one
     if w < g.secq(v).getWeight(): #check if it is a better path than the current weight
          g.secq(v).setWeight(w)
          g.reduce(g.secq(v).getVal(),w) #reduce the weight of the edge vertex 
          e=u.getVal(), g.secq(v).getVal()
          final.append(e) #add it to the list of searched edges
final.reverse()
found=[]
display=[]
for z in final:#goes through the found edges
    if z[1] not in found: #finds the correct path through them
        display.append(z)
        found.append(z[1])
display.reverse()
print ("Initial Tree (Edges: u, v, weight)")
for s in g.allvert():# print al the vertices and their edges
   print ("Vertex",s.getVal(),"Edges:")
   for b in s.getedges():
        print (b)
print("")
print("Optimal Path from Algorithm:")
for c in display: #print the found path
    print(c)
