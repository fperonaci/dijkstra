import pytest
from dijkstra import *

def testWikipediaGraph():

  n1 = Node("n1")
  n2 = Node("n2")
  n3 = Node("n3")
  n4 = Node("n4")
  n5 = Node("n5")
  n6 = Node("n6")

  n1.Arcs.append(Arc(n1,n2,7))
  n1.Arcs.append(Arc(n1,n3,9))
  n1.Arcs.append(Arc(n1,n6,14))

  n2.Arcs.append(Arc(n2,n1,7))
  n2.Arcs.append(Arc(n2,n3,10))
  n2.Arcs.append(Arc(n2,n4,15))

  n3.Arcs.append(Arc(n3,n1,9))
  n3.Arcs.append(Arc(n3,n2,10))
  n3.Arcs.append(Arc(n3,n4,11))
  n3.Arcs.append(Arc(n3,n6,2))

  n4.Arcs.append(Arc(n4,n2,15))
  n4.Arcs.append(Arc(n4,n3,11))
  n4.Arcs.append(Arc(n4,n5,6))

  n5.Arcs.append(Arc(n5,n4,6))
  n5.Arcs.append(Arc(n5,n6,9))

  n6.Arcs.append(Arc(n6,n1,14))
  n6.Arcs.append(Arc(n6,n3,2))
  n6.Arcs.append(Arc(n6,n5,9))

  dijkstraSolver(root=n1)

  assert n1.Distance == 0
  assert n2.Distance == 7
  assert n3.Distance == 9
  assert n4.Distance == 20
  assert n5.Distance == 20
  assert n6.Distance == 11
