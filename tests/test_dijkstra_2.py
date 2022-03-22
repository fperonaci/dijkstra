import pytest
from dijkstra import *

def testWikipediaGraph():

  labels = ['n1','n2','n3','n4','n5','n6']

  arcs = [
    ('n1','n2',7),('n1','n3',9),('n1','n6',14),
    ('n2','n3',10),('n2','n4',15),('n3','n4',11),
    ('n5','n6',9)]

  nodes = buildUndirectedGraph(labels,arcs)

  dijkstraSolver(root=nodes[0],nodes=nodes)

  assert nodes[0].Distance == 0
  assert nodes[1].Distance == 7
  assert nodes[2].Distance == 9
  assert nodes[3].Distance == 20
  assert nodes[4].Distance == 23
  assert nodes[5].Distance == 14
