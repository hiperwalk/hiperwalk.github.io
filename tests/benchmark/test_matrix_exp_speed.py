import numpy as np
import numpy.linalg as npla
import networkx as nx
from time import time
import scipy.linalg as dense_la
import scipy.sparse.linalg as sparse_la
import scipy.sparse



def benchmark(func, arg, message):
    times = np.zeros(30)
    for i in range(len(times)):
        start = time()
        func(arg)
        times[i] = time() - start

    avg = np.average(times)
    print(message + "\t" + str(avg) + 's')
    return avg


def benchmark_grid(num_vert):
    
    ret = [0] * 7

    G = nx.grid_2d_graph(num_vert, num_vert)
    adj = nx.adjacency_matrix(G)
    adj_dense = adj.todense()
    # computing time for np final matrix
    ret[0] = benchmark(np.exp, 1j * adj_dense, 'np final')

    # computing time for np expoent (adjacency matrix)
    ret[1] = benchmark(npla.eig, adj_dense, 'np eig adj')
    ret[2] = benchmark(npla.eigh, adj_dense, 'np eigh adj')

    # computing time for sp final matrix
    ret[3] = benchmark(dense_la.expm, adj_dense, 'sp dense final')

    # computing time for sp expoent (adjacency matrix)
    ret[4] = benchmark(dense_la.eig, adj_dense, 'sp dense eig')
    ret[5] = benchmark(dense_la.eigh, adj_dense, 'sp dense eigh')

    # computing time for sp sparse final matrix
    ret[6] = benchmark(sparse_la.expm, scipy.sparse.csc_matrix(adj),
                       'sp sparse final')

    # cannot be used because according to the documentation,
    # not all eigenvectors can be calculated.
    ## computing time for sp sparse expoent (adjacency matrix)
    #benchmark(sparse_la.eigs, adj, 'sp sparse eig')
    #benchmark(sparse_la.eigsh, adj, 'sp sparse eigh')
    return ret


######################################################################
times = []
for n in range(5, 201, 5):
    print("=========== " + str(n) + " X " + str(n) + " GRID ========== ")
    times.append(benchmark_grid(n))
    print(times)
    print()

print(times)
