"""evaluate.py
Evaluation helpers: modularity, NMI (requires ground-truth labels), embedding-quality metrics.
"""
import networkx as nx
from sklearn.metrics import normalized_mutual_info_score
from sklearn.metrics import silhouette_score
import numpy as np

def modularity_from_partition(G, partition_dict):
    # partition_dict: node -> community
    try:
        import community as community_louvain
        # build partition list
        inv = {}
        for n,c in partition_dict.items():
            inv.setdefault(c, set()).add(n)
        parts = list(inv.values())
        return nx.algorithms.community.quality.modularity(G, parts)
    except Exception:
        # fallback naive
        return None

def nmi_from_labels(true_labels, pred_labels):
    return normalized_mutual_info_score(true_labels, pred_labels)

def embedding_silhouette(embeddings, labels):
    # embeddings: dict node->vector
    nodes = list(embeddings.keys())
    X = np.vstack([embeddings[n] for n in nodes])
    y = [labels.get(int(n), -1) if isinstance(n, str) and n.isdigit() else labels.get(n, -1) for n in nodes]
    if len(set(y)) <= 1:
        return None
    return silhouette_score(X, y)
