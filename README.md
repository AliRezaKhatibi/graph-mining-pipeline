# Graph Mining Pipeline

This repository contains a complete pipeline skeleton for graph mining built around the SNAP `email-Eu-core` dataset.

**What you get**
- project structure with `src/` utilities, tests, a Streamlit demo app, and a small *sample* of the dataset (data/raw/email-Eu-core-sample.csv).
- a downloader script (`src/ingest.py::download_snap_email_eu_core`) and instructions below to fetch the *official* dataset from SNAP.

**Important — dataset**
The full EU Email Core dataset is hosted by SNAP (Stanford Large Network Dataset Collection). To download the official dataset run:

```bash
# from project root
cd data/raw
wget https://snap.stanford.edu/data/email-Eu-core.txt.gz
gunzip email-Eu-core.txt.gz
mv email-Eu-core.txt email-Eu-core.txt
```

Alternatively run the Python helper in `src/ingest.py` (requires `requests` and internet access).

**Quick start (local)**
1. create environment: `conda env create -f environment.yml` or `python -m venv .venv && pip install -r requirements.txt`
2. install packages and run tests: `pytest -q`
3. run Streamlit demo: `streamlit run streamlit_app.py`
4. To run a notebook example: open `notebooks/analysis.ipynb` in Jupyter.

**Notes**
- This archive includes only a small sample CSV so you can run the demo immediately.
- The full dataset (~25K edges, ~1k nodes) is *not* included here due to size and licensing best-practices — use the downloader above to fetch it directly from SNAP.


## Quick Virtualenv (venv) setup and editable install

1. Create and activate a virtual environment (Linux/macOS):
```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m pip install -e .
```

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m pip install -e .
```

Run tests:
```bash
pytest
```

If you prefer not to install editable, you can run pytest with PYTHONPATH set:
Linux/macOS:
```bash
PYTHONPATH=. pytest
```
Windows PowerShell:
```powershell
$env:PYTHONPATH = (Get-Location).Path
pytest

.\.venv\Scripts\activate.bat


pytest

streamlit run streamlit_app.py

./run_pipeline.sh    # or : python scripts/run_features.py

```
