"""community.py
Community detection utilities: Louvain (python-louvain) and label propagation.
"""
import networkx as nx

def louvain_partition(G):
    try:
        import community as community_louvain
    except Exception:
        raise RuntimeError('python-louvain required: pip install python-louvain')
    part = community_louvain.best_partition(G)
    return part

def label_propagation_communities(G):
    # networkx returns generator
    return list(nx.algorithms.community.label_propagation_communities(G))
