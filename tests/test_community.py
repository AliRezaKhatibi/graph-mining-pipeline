import networkx as nx
from src.community import label_propagation_communities
def test_label_propagation_small():
    G = nx.karate_club_graph()
    parts = label_propagation_communities(G)
    assert isinstance(parts, list) or hasattr(parts, '__iter__')
