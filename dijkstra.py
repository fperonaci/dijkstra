from numpy import argmin

class Node():
  def __init__(self,label):
    self.Label = label
    self.Visited = False
    self.Arcs = []
    self.Distance = float("inf")

class Arc():
  def __init__(self,orig,dest,cost):
    self.Orig = orig
    self.Dest = dest
    self.Cost = cost

def dijkstraSolver(root):

  root.Distance = 0
  node = root
  
  while True:
  
    arcsToNotVisited = [
      arc for arc in node.Arcs if not arc.Dest.Visited]
    
    if not arcsToNotVisited:
      break
    
    for arc in arcsToNotVisited:
      d = node.Distance + arc.Cost
      if d < arc.Dest.Distance:
        arc.Dest.Distance = d

    node.Visited = True
  
    idx = argmin([arc.Dest.Distance for arc in arcsToNotVisited])
    node = arcsToNotVisited[idx].Dest
