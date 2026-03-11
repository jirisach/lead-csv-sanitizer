import pandas as pd


def detect_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detect duplicate leads based on email or phone.
    """

    df = df.copy()

    if "email" in df.columns:
        df["duplicate_email"] = df.duplicated(subset=["email"], keep=False)
    else:
        df["duplicate_email"] = False

    if "sanitized_phone" in df.columns:
        df["duplicate_phone"] = df.duplicated(subset=["sanitized_phone"], keep=False)
    else:
        df["duplicate_phone"] = False

    df["is_duplicate"] = df["duplicate_email"] | df["duplicate_phone"]

    return df