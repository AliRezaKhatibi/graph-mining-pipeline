
"""visualize.py
Plotly network plot helper for the graph-mining-pipeline.
This module is intentionally small and defensive so it works on sample graphs.
"""
import networkx as nx
import plotly.graph_objects as go
from typing import Optional

def network_plotly(G: nx.Graph, node_size_attr: Optional[str]=None, top_n: int=200):
    """
    Build a lightweight Plotly figure for a (possibly small) NetworkX graph.
    - G: networkx Graph or DiGraph
    - node_size_attr: optional node attribute name to scale marker sizes
    - top_n: maximum number of nodes to layout/plot (subsample if graph is large)
    """
    # choose nodes (subsample if large)
    nodes = list(G.nodes())[:top_n]
    # compute layout for chosen nodes
    subG = G.subgraph(nodes)
    pos = nx.spring_layout(subG, seed=42)

    # build edge traces
    edge_x, edge_y = [], []
    for u, v in subG.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        mode='lines',
        line=dict(width=0.5),
        hoverinfo='none'
    )

    # build node traces
    node_x, node_y, text, sizes = [], [], [], []
    for n in subG.nodes():
        x, y = pos[n]
        node_x.append(x)
        node_y.append(y)
        text.append(str(n))
        if node_size_attr and node_size_attr in subG.nodes[n]:
            try:
                sizes.append(float(subG.nodes[n].get(node_size_attr, 1.0)) * 5.0)
            except Exception:
                sizes.append(8)
        else:
            sizes.append(8)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        marker=dict(size=sizes),
        text=text,
        hoverinfo='text'
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(showlegend=False, margin=dict(l=0, r=0, t=20, b=0))
    return fig
