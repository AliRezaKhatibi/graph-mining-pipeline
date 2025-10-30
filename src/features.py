"""features.py
Compute common node features and Node2Vec embedding (if node2vec package is installed).
"""
import networkx as nx
import numpy as np
import pandas as pd

def degree_centrality(G):
    return dict(G.degree())

def betweenness_centrality(G, k=None):
    return nx.betweenness_centrality(G, k=k)

def eigenvector_centrality_safe(G, max_iter=1000):
    try:
        return nx.eigenvector_centrality_numpy(G)
    except Exception:
        return nx.eigenvector_centrality(G, max_iter=max_iter)

def compute_node2vec_embeddings(G, dimensions=64, walk_length=30, num_walks=200, p=1, q=1):
    try:
        from node2vec import Node2Vec
    except Exception as e:
        raise RuntimeError("node2vec package required for embeddings: pip install node2vec") from e
    n2v = Node2Vec(G, dimensions=dimensions, walk_length=walk_length, num_walks=num_walks, p=p, q=q, workers=2)
    model = n2v.fit(window=10, min_count=1, batch_words=4)
    emb = {str(node): model.wv.get_vector(str(node)) for node in G.nodes()}
    return emb
