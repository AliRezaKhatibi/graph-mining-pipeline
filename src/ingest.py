"""ingest.py
Utilities to load the sample graph and (optionally) download the full SNAP email-Eu-core dataset.
"""
import os
import gzip
import shutil
import pandas as pd
from pathlib import Path

SNAP_URL = "https://snap.stanford.edu/data/email-Eu-core.txt.gz"
DEFAULT_RAW = Path(__file__).resolve().parents[1] / "data" / "raw"

def download_snap_email_eu_core(dest_dir=None, timeout=30):
    """Download the official email-Eu-core dataset from SNAP and unpack it.
    NOTE: this function uses requests; if your environment blocks network access,
    run the wget command in the README manually.
    """
    import requests
    dest_dir = Path(dest_dir or DEFAULT_RAW)
    dest_dir.mkdir(parents=True, exist_ok=True)
    gz_path = dest_dir / "email-Eu-core.txt.gz"
    txt_path = dest_dir / "email-Eu-core.txt"
    print(f"Downloading {SNAP_URL} to {gz_path} ...")
    r = requests.get(SNAP_URL, stream=True, timeout=timeout)
    r.raise_for_status()
    with open(gz_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    # unpack
    import gzip
    with gzip.open(gz_path, "rb") as f_in:
        with open(txt_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("Downloaded and unpacked to", txt_path)
    return txt_path

def load_edge_list(path=None, directed=False, comment_prefix="#"):
    path = Path(path or (DEFAULT_RAW / "email-Eu-core-sample.csv"))
    df = pd.read_csv(path, comment=comment_prefix, header=None, names=["source","target"]) if path.suffix in [".csv",".txt"] else pd.read_csv(path)
    return df

if __name__ == "__main__":
    print("ingest utilities. Use download_snap_email_eu_core() to fetch the full dataset or load_edge_list() to load sample.")
