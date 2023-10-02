import numpy as np
import networkx as nx
csv_file = 'cosine_similiarity_matrix.csv'

matrix = np.genfromtxt(csv_file)

G=nx.from_numpy_matrix(matrix)