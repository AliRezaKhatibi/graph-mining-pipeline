# Graph Mining Pipeline

Explore graph mining with Python, NetworkX and Streamlit using the Stanford SNAP email-Eu-core dataset. This repository provides a pipeline skeleton, graph-processing utilities, tests, a notebook example and an interactive local demo.

## Try the demo

The repository includes a small sample edge list, so you can explore the visualization without downloading the full research dataset. Run the commands from the repository root.

### Linux / macOS

```bash
git clone https://github.com/AliRezaKhatibi/graph-mining-pipeline.git
cd graph-mining-pipeline
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

### Windows (PowerShell)

```powershell
git clone https://github.com/AliRezaKhatibi/graph-mining-pipeline.git
cd graph-mining-pipeline
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

Open the local URL printed by Streamlit. The demo displays node and edge counts and a Plotly network visualization. You can use the bundled sample or upload a headerless, comma-separated edge list with two columns, for example:

```csv
0,1
1,2
2,0
```

The visualization is exploratory; the bundled sample is not a substitute for the full dataset.

## Project resources

| Resource | Purpose |
| --- | --- |
| [Streamlit demo](streamlit_app.py) | Interactive graph exploration |
| [Ingestion utilities](src/ingest.py) | Loading data and downloading the full dataset |
| [Preprocessing](src/preprocess.py) | Graph construction and cleaning |
| [Visualization](src/visualize.py) | Plotly graph visualization |
| [Sample edge list](data/raw/email-Eu-core-sample.csv) | Small local example |
| [Dependencies](requirements.txt) | Python libraries used by the project |

## Full research dataset

The full [email-Eu-core dataset](https://snap.stanford.edu/data/email-Eu-core.html) is hosted by Stanford's SNAP project. It contains approximately 1,000 nodes and 25,000 edges and is not included in this repository. Consult the original dataset page for its description, provenance and citation requirements.

From the repository root, with the dependencies installed, use the included Python downloader:

```bash
python -c "from src.ingest import download_snap_email_eu_core; download_snap_email_eu_core()"
```

The helper downloads and extracts the official file into `data/raw/`. Internet access is required. The official text edge list is separate from the demo's headerless CSV input; do not assume the formats are interchangeable without conversion.

Alternatively, on Linux/macOS:

```bash
cd data/raw
wget https://snap.stanford.edu/data/email-Eu-core.txt.gz
gunzip email-Eu-core.txt.gz
```

On Windows, from the repository root:

```powershell
Invoke-WebRequest -Uri "https://snap.stanford.edu/data/email-Eu-core.txt.gz" -OutFile "data/raw/email-Eu-core.txt.gz"
python -c "import gzip, shutil; a=gzip.open('data/raw/email-Eu-core.txt.gz','rb'); b=open('data/raw/email-Eu-core.txt','wb'); shutil.copyfileobj(a,b); a.close(); b.close()"
```

## Development and experiments

Run the test suite from the repository root:

```bash
python -m pytest -q
```

For notebook exploration, open `notebooks/analysis.ipynb` using a Jupyter environment. Install Jupyter separately if needed. On Linux/macOS, the documented pipeline entry point is `./run_pipeline.sh`; the feature script can also be invoked with `python scripts/run_features.py`.

Dependency versions are not pinned in `requirements.txt`. For reproducible research, record the Python version, installed package versions, dataset source, preprocessing settings and random seeds alongside your results.

## Contributing

Feedback on graph algorithms, reproducibility, dataset handling and documentation is welcome. For a useful bug report, include your OS, Python version, the command you ran, a minimal non-sensitive edge list and the traceback. For research comparisons, describe preprocessing and evaluation settings.

If this repository is useful in your work, consider starring it or following the [author](https://github.com/AliRezaKhatibi) for related mathematical machine learning projects.
