from pathlib import Path
from collections import Counter
import re
from Bio import SeqIO
import pandas as pd

OUTDIR = Path("results/antismash_1A01")

gbks = sorted(OUTDIR.glob("*region*.gbk"))
if not gbks:
    raise SystemExit(f"No region GBK files found in {OUTDIR.resolve()}")

def extract_class_from_feature(feat):
    # antiSMASH puts type info in various places; try the common ones.
    q = feat.qualifiers
    # 1) direct product/type
    for key in ("product", "type", "kind", "class"):
        if key in q and q[key]:
            return str(q[key][0])
    # 2) notes often contain "Type: NRPS", "Type: PKS", etc.
    for key in ("note", "description"):
        if key in q:
            txt = " ".join(map(str, q[key]))
            m = re.search(r"(?:Type|type)\s*:\s*([A-Za-z0-9\-\+_/ ]+)", txt)
            if m:
                return m.group(1).strip()
    return None

rows = []
for gbk in gbks:
    rec = SeqIO.read(gbk, "genbank")
    # antiSMASH stores a 'region' (or 'cluster') feature describing the BGC
    bgc_class = None
    for feat in rec.features:
        if feat.type in ("region", "cluster", "protocluster", "cand_cluster"):
            bgc_class = extract_class_from_feature(feat) or bgc_class
    rows.append({"file": gbk.name, "bgc_class": (bgc_class or "Unknown")})

df = pd.DataFrame(rows).sort_values("file")
counts = Counter(df["bgc_class"])

print(f"Total BGCs: {len(df)}")
print("\nBGC class breakdown:")
for k,v in counts.most_common():
    print(f"{k}: {v}")

# optional: save a TSV
tsv = OUTDIR / "bgc_classes_from_gbk.tsv"
df.to_csv(tsv, sep="\t", index=False)
print(f"\nSaved per-region classes → {tsv}")



# antiSMASH Results Summary (Genome: 1A01)
# ----------------------------------------
# Total BGCs identified: 8
#
# Breakdown by class:
#   - RiPP-like: 2  → ribosomally synthesized peptides, often antimicrobial
#   - NRPS: 1       → classic antibiotic-producing cluster (assembly line)
#   - Arylpoylene: 1 → pigment-like, oxidative stress roles
#   - hglE-KS: 1    → atypical KS-domain, possible novel metabolite
#   - Betalactone: 1 → β-lactone products, some antibiotic potential
#   - Opine-like-metallophore: 1 → metal-binding, nutrient competition
#   - Terpene-precursor: 1 → precursor for terpenes/steroids
#
# Why it matters:
#   • Demonstrates genomic biosynthetic potential = 8 distinct BGCs
#   • NRPS + RiPP clusters are strong antimicrobial candidates
#   • Diversity of cluster types suggests ecological + therapeutic novelty
#   • These genomic predictions can be cross-validated against metabolomics 
#     (GNPS/MS data) to assess which predicted metabolites are actually expressed
#
# Next step:
#   → Process isolate-1.mzXML (metabolomics) to compare detected compounds 
#     with antiSMASH-predicted BGC classes
