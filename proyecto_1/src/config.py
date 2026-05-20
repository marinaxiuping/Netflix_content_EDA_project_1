from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = ROOT / "data" / "raw" / "netflix_titles.csv"
OUT_PATH = ROOT / "data" / "processed" / "clean_dataset.csv"
FIGSIZE = (10, 6)
STYLE = "darkgrid"
