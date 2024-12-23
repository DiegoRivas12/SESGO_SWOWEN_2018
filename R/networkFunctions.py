import networkx as nx

def create_graph(X):
    edges = compute_edge_table(X)
    
    G = nx.DiGraph()
    for _, row in edges.iterrows():
        G.add_edge(row['source'], row['target'], weight=row['weight'])
    
    G.remove_nodes_from([n for n, d in G.out_degree() if d == 0])
    return G

def compute_edge_table(X):
    if 'Freq' in X.columns:
        edges = X[['cue', 'response', 'Freq']].rename(columns={
            'cue': 'source', 'response': 'target', 'Freq': 'weight'
        })
    else:
        grouped = X.dropna(subset=['response']).groupby(['cue', 'response']).size()
        edges = grouped.reset_index(name='weight').rename(columns={
            'cue': 'source', 'response': 'target'
        })
    return edges

def normalize_edge_weights(G):
    for u, v, d in G.edges(data=True):
        out_strength = sum(d['weight'] for _, _, d in G.out_edges(u, data=True))
        d['weight'] /= out_strength
    return G
