import pandas as pd
from pathlib import Path

def test_ipl_csv_columns():
    csv_path = Path(__file__).resolve().parents[1] / 'data' / 'ipl-2025-mumbai-indians-UTC.csv'
    df = pd.read_csv(csv_path)
    expected_columns = ['Match Number','Round Number','Date','Location','Home Team','Away Team','Result']
    assert list(df.columns) == expected_columns
