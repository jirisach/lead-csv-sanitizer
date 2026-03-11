from pathlib import Path
import pandas as pd


SUPPORTED_ENCODINGS = ("utf-8", "utf-8-sig", "cp1250", "latin1")
MAX_ROWS = 1_000_000


def load_csv(input_file: Path) -> pd.DataFrame:
    """
    Safely load a CSV file using several common encodings.
    """

    if not input_file.exists():
        raise ValueError(f"Input file does not exist: {input_file}")

    last_error = None

    for encoding in SUPPORTED_ENCODINGS:
        try:
            df = pd.read_csv(input_file, encoding=encoding)

            if df.empty:
                raise ValueError("Input CSV is empty")

            if len(df) > MAX_ROWS:
                raise ValueError(
                    f"Dataset too large: {len(df)} rows. "
                    f"Max supported rows: {MAX_ROWS}."
                )

            return df

        except Exception as exc:
            last_error = exc

    raise ValueError(f"Could not read CSV file: {input_file}. Last error: {last_error}")