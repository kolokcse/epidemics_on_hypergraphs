''' This  file contains algorithms which ganerate random hypergraphs for given parameters. 

    H=(V,E) pair is a hypergraph

    The hypergraph implementation is described in hypergraphs.py
    
    V: vertices
    E: hyperedges (subsets of V)
    
    Hypergraph types:
    
    GIRH: Geometric Inhomogenious Random Hypergraph
    
    V: is a finite ranom set of an d-dimensional points in the d-dimensioanl cube
    
    E: m hyperedge generation operates as follows:
        Every node has a w_v weight. 
        We generate hyperedges step by step. 
        In the step i, we pick a random point in the n-dimensioanl cube.
        This point will be the hyperedge i central point c_i. After that,
        we generate the hyperedge weight w_e according to some hyperedge size distribution.
        And we chose the nodes which are contianed by the hyperede with probability proportinal:
        
        w_e*w_v/(W*||c_i-v||_2)^(d*alpha),
        
        where alpha is a parameter given as input. W is the sum of the weights.
'''

import numpy as np
import random as rnd
import math
import powerlaw
from scipy.stats import poisson
from scipy.stats import pareto
from scipy.stats import gamma
from scipy.spatial import distance
import bisect
from classes.node import Node
from classes.edge import Hyperedge
from classes.hypergraph import Hypergraph
import hypernetx as hnx


def get_hypergraph(type, args):
    if type=='random-geometric':
        H=get_girh(args['n'],args['m'],args['alpha'],args['attr list'], args)
        return H
    if type=='flower':
        H=get_flower(args)
        return H


def get_girh(n,m, alpha, attr_lists, args):
    H = Hypergraph()
    coordinates=np.array([np.random.rand(2) for i in range(n)])
    for i in range(n):
        if len(attr_lists)==n:
            H.add_node([[], attr_lists[i]],True)
        elif len(attr_lists)>0:
            print('The attr_list size does not match')
        else:
            H.add_node([])
    if "deg_exp" in args:
        deg_exp = args["deg_exp"]
    else:
        deg_exp = 3.5
    d=powerlaw.Power_Law(xmin=3,parameters=[deg_exp]).generate_random(n)
    w_v=d
    if "size_exp" in args:
        size_exp = args["size_exp"]
    else:
        size_exp = 3.5
    c_is = np.array([np.random.rand(2) for i in range(m)])
    k=powerlaw.Power_Law(xmin=3,parameters=[size_exp]).generate_random(m)
    w_es = k
    W=sum(d)+sum(k)
    for i in range(m):
        nodelist=[]
        for j in range(n):
            if rnd.random()< np.power((w_es[i]*w_v[j]/W),alpha)/np.power(distance.euclidean(c_is[i],coordinates[j]), alpha * 2) :
                nodelist.append(H.nodes[j])
        H.add_edge([nodelist, {'id': '20' +str(i)}], True)
    return H
    
def get_flower(args):
    k=args["edge size"]
    s=args["number of levels"]
    scenes={str(0) : tuple(np.arange(k))}
    m=int(k*(((k-1)**(s-1))-1)/(k-2))
    n=int(k*(((k-1)**(s))-1)/(k-2))
    v=list(np.arange(n))
    for i in range(m):
        scenes[str(i+1)]=tuple([i]+v[(i+1)*(k-1)+1:(i+2)*(k-1)+1])
    H=hnx.Hypergraph(scenes)
    
    return H  
        
    
    
    