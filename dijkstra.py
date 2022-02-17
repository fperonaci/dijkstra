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

def dijkstraSolver(root,nodes):

  root.Distance = 0
  node = root
  
  while True:
  
    node.Visited = True
  
    arcsToNotVisited = [
      arc for arc in node.Arcs if not arc.Dest.Visited]
    
    if not arcsToNotVisited:
      notVisited = [node for node in nodes if not node.Visited]
      if not notVisited:
        break
      else:
        idx = argmin([node.Distance for node in notVisited])
        node = notVisited[idx]
        continue

    else:
      for arc in arcsToNotVisited:
        d = node.Distance + arc.Cost
        if d < arc.Dest.Distance:
          arc.Dest.Distance = d
      idx = argmin([arc.Dest.Distance for arc in arcsToNotVisited])
      node = arcsToNotVisited[idx].Dest
