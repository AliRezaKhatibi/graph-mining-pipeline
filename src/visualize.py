"""visualize.py
Plotting helpers (plotly) and Streamlit wiring.
""")
import networkx as nx
import plotly.graph_objects as go

def network_plotly(G, node_size_attr=None, top_n=200):
    # lightweight plotly visual for small graphs (subsample if large)
    nodes = list(G.nodes())[:top_n]
    pos = nx.spring_layout(G, seed=42)
    edge_x, edge_y = [], []
    for u, v in G.edges():
        if u in pos and v in pos:
            x0, y0 = pos[u]
            x1, y1 = pos[v]
            edge_x += [x0, x1, None]
            edge_y += [y0, y1, None]
    edge_trace = go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=0.5), hoverinfo='none')
    node_x, node_y, text = [], [], []
    for n in nodes:
        x, y = pos[n]
        node_x.append(x); node_y.append(y); text.append(str(n))
    node_trace = go.Scatter(x=node_x, y=node_y, mode='markers', marker=dict(size=8), text=text, hoverinfo='text')
    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(showlegend=False)
    return fig
