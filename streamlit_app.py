import streamlit as st
import pandas as pd
import networkx as nx
from src.ingest import load_edge_list
from src.preprocess import df_to_graph, clean_graph
from src.visualize import network_plotly

st.set_page_config(layout='wide', page_title='Graph Mining Pipeline')
st.title('Graph Mining Pipeline — Demo (sample data)')

uploaded = st.file_uploader('Upload an edge list CSV (source,target) or use sample', type=['csv','txt'])
if uploaded:
    df = pd.read_csv(uploaded, header=None, names=['source','target'])
else:
    df = pd.read_csv('data/raw/email-Eu-core-sample.csv', comment='#', header=None, names=['source','target'])

G = df_to_graph(df)
G = clean_graph(G)
st.write('Nodes:', G.number_of_nodes(), 'Edges:', G.number_of_edges())

fig = network_plotly(G)
st.plotly_chart(fig, use_container_width=True)
