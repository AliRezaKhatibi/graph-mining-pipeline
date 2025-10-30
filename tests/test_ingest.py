from src.ingest import load_edge_list
def test_load_sample():
    df = load_edge_list(path='data/raw/email-Eu-core-sample.csv')
    assert 'source' in df.columns and 'target' in df.columns
    assert len(df) > 0
