"""preprocess.py
Basic cleaning and conversion utilities (NetworkX-friendly).
"""
import networkx as nx
import pandas as pd
from pathlib import Path

def df_to_graph(df, directed=False):
    if 'weight' in df.columns:
        edges = list(df[['source','target','weight']].itertuples(index=False, name=None))
    else:
        edges = list(df[['source','target']].itertuples(index=False, name=None))
    G = nx.DiGraph() if directed else nx.Graph()
    G.add_edges_from(edges)
    return G

def clean_graph(G):
    # remove self-loops, isolate nodes optional
    G.remove_edges_from(nx.selfloop_edges(G))
    # remove isolates
    isolates = list(nx.isolates(G))
    if isolates:
        G.remove_nodes_from(isolates)
    return G

def save_graph_edgelist(G, path):
    nx.write_edgelist(G, path, data=False)
    return path

if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('../data/raw/email-Eu-core-sample.csv', comment='#', header=None, names=['source','target'])
    G = df_to_graph(df)
    G = clean_graph(G)
    save_graph_edgelist(G, '../data/processed/email-Eu-core-processed.txt')
    print('Processed and saved sample graph.')
