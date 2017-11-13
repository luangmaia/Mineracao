# needed imports
import sys
sys.setrecursionlimit(10000)
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import numpy as np
import BaseHandle
np.set_printoptions(precision=5, suppress=True)  # suppress scientific float notation

# generate two clusters: a with 100 points, b with 50:
tabela = BaseHandle.base2matrizSemNome('BasePorGenero.txt')
Z = linkage(tabela, 'single')

k=2
clusters = fcluster(Z, k, criterion='maxclust')

"""
plt.title('Hierarchical Clustering Dendrogram (truncated)')
#plt.xlabel('sample index')
#plt.ylabel('distance')
#dendrogram(
    Z,
    truncate_mode='lastp',  # show only the last p merged clusters
    p=12,  # show only the last p merged clusters
    show_leaf_counts=False,  # otherwise numbers in brackets are counts
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,  # to get a distribution impression in truncated branches
)
plt.show()"""
'''
plt.figure(figsize=(10, 8))
plt.scatter(Z[:,0], Z[:,1])  # plot all points
plt.show()'''

plt.figure(figsize=(10, 8))
plt.scatter(Z[:,0], Z[:,1], c=clusters, cmap='prism')  # plot points with cluster dependent colors
plt.show()