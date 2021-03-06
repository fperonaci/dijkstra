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
    
    if arcsToNotVisited != []:
      for arc in arcsToNotVisited:
        d = node.Distance + arc.Cost
        if d < arc.Dest.Distance:
          arc.Dest.Distance = d
      idx = argmin([arc.Dest.Distance for arc in arcsToNotVisited])
      node = arcsToNotVisited[idx].Dest

    else:
      notVisited = [node for node in nodes if not node.Visited]
      if notVisited != []:
        idx = argmin([node.Distance for node in notVisited])
        node = notVisited[idx]
        continue
      else:
        break

def buildUndirectedGraph(labels,arcs):
  nodes = {label:Node(label) for label in labels}
  for arc in arcs:
    orig = nodes[arc[0]]
    dest = nodes[arc[1]]
    cost = arc[2]
    orig.Arcs.append(Arc(orig,dest,cost))
    dest.Arcs.append(Arc(dest,orig,cost))
  return list(nodes.values())
