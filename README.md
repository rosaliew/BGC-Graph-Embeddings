# BGC Graph Embeddings

> Thesis Aim 1 — MASc Chemical Engineering & Applied Chemistry

Genomic preprocessing and BGC representation pipeline using AntiSMASH and ESM-2 protein language model embeddings. This is the first step toward a multimodal BGC–metabolite linking model for natural product discovery in marine microbes.

---

## Repository structure

```text
BGC-Graph-Embeddings/
├── data/
│ ├── raw/ # Raw GenBank files (e.g. 1A01.gbk)
│ └── processed/
│ └── fasta/ # FASTA files converted from GenBank (e.g. 1A01.fasta)
├── notebooks/
│ ├── 01_eda_bgc_structure.ipynb # Exploratory analysis of BGC structure and features
│ ├── 02_esm2_mean_pool_baseline.ipynb # ESM-2 mean pooling baseline embeddings
│ └── 03_bgc_graph_construction.ipynb # Graph construction experiments for BGCs
├── results/
│ ├── antismash_1A01/ # AntiSMASH output for isolate 1A01
│ └── figures/ # Plots and visualizations
├── scripts/
│ ├── antismash_batch_run.py # Run AntiSMASH on multiple genomes
│ ├── esm_embeddings.py # Generate ESM-2 embeddings from protein sequences
│ └── genbank-to-fasta.py # Convert GenBank files to FASTA format
├── src/
│ ├── _init_.py
│ ├── bgc_dataset.py # Dataset class for BGC inputs
│ ├── esm_embeddings.py # Reusable embedding generation utilities
│ ├── graph_builder.py # BGC graph construction logic
│ ├── paths_and_constants.py # Shared file paths and project constants
│ └── utils.py # General utility functions
├── tests/
│ └── test_data.py # Tests for data loading and processing steps
├── .gitignore
├── environment.yml
├── LICENSE
└── README.md
```

---

## Workflow

```text
GenBank (.gbk)
→ genbank-to-fasta.py # convert to FASTA
→ antismash_batch_run.py # run AntiSMASH to identify BGC regions
→ esm_embeddings.py # generate protein embeddings via ESM-2
→ 02_esm2_mean_pool_baseline # explore mean-pool baseline representations
→ 03_bgc_graph_construction # experiment with graph-based BGC representations
```


---

## Getting started

```bash
conda env create -f environment.yml
conda activate bgc-ml
```

Run preprocessing:

```bash
python scripts/genbank-to-fasta.py
python scripts/antismash_batch_run.py
python scripts/esm_embeddings.py
```

Then open notebooks in order from `notebooks/`.

---

## Data

- `data/raw/` — original GenBank files; large files are gitignored
- `data/processed/fasta/` — FASTA outputs ready for embedding generation
- `results/antismash_1A01/` — AntiSMASH output for *Vibrio* isolate 1A01 (demo/development genome)

For large or shared datasets, see `data/README.md` (to be added).

---

## Thesis context

Part of a thesis pipeline for linking BGCs to their metabolite products in understudied marine microbes using multimodal machine learning. This repository handles the **genomic input side**: converting raw genome files, running BGC detection, and generating initial representations for comparison and downstream linking.

Related repos: `ms2-spectral-embeddings` · `multimodal-np-linker` · `marine-np-discovery` · `npomics-toolkit`

---

## Author

Rosalie Wang · University of Toronto  
MASc Chemical Engineering and Applied Chemistry