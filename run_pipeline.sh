#!/usr/bin/env bash
set -e
python - <<'PY'
from src.ingest import load_edge_list
from src.preprocess import df_to_graph, clean_graph, save_graph_edgelist
import pandas as pd
df = load_edge_list('data/raw/email-Eu-core-sample.csv')
G = df_to_graph(df)
G = clean_graph(G)
print('Nodes:', G.number_of_nodes(), 'Edges:', G.number_of_edges())
PY
