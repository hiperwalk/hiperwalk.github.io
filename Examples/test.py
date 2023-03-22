import numpy as np
import networkx as nx
import sys
sys.path.append('..')
import qwalk.coined as hpcoined
import plot as hplot

# generating adjacency matrix of a 5x5 2d-horizontal-latiice
grid_dim = 3
G = nx.grid_graph(dim=(grid_dim, grid_dim), periodic=True)
adj_matrix = nx.adjacency_matrix(G)
del G # only the adjacency matrix is going to be used

print(adj_matrix)

chl = hpcoined.Coined(adj_matrix) #coined horizontal lattice
S = chl.flip_flop_shift_operator()
print(S)
np.set_printoptions(threshold=np.inf)
#print(S.todense())
print(S.indptr)
print(S.indices)

print(S.todense())
