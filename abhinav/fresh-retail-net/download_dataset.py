"""
Download FreshRetailNet-50K dataset from HuggingFace
Run: poetry run python abhinav/fresh-retail-net/download_dataset.py
"""
from datasets import load_dataset
import pandas as pd
import os

DEST = os.path.dirname(os.path.abspath(__file__))

print("Downloading FreshRetailNet-50K from HuggingFace...")
ds = load_dataset("Dingdong-Inc/FreshRetailNet-50K")

for split in ds:
    df = ds[split].to_pandas()
    out_path = os.path.join(DEST, f"{split}.csv")
    df.to_csv(out_path, index=False)
    print(f"  {split}: {len(df):,} rows, {df.shape[1]} cols -> {out_path}")

print(f"\nDone. Files: {os.listdir(DEST)}")
