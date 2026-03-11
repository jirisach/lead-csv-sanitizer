import re
import pandas as pd


COLUMN_ALIASES = {
    "first_name": [
        "first name",
        "firstname",
        "first_name",
        "fname"
    ],
    "last_name": [
        "last name",
        "lastname",
        "last_name",
        "lname"
    ],
    "email": [
        "email",
        "e-mail",
        "email address",
        "email_address"
    ],
    "phone": [
        "phone",
        "phone number",
        "mobile",
        "tel",
        "telephone"
    ],
    "company": [
        "company",
        "company name",
        "company_name",
        "organisation",
        "organization"
    ],
}


def normalize_column_name(name: str) -> str:
    """
    Normalize column name to comparable format.
    """
    name = name.strip().lower()
    name = re.sub(r"[_\-]", " ", name)
    return name


def map_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns to canonical names.
    """

    rename_map = {}

    for col in df.columns:
        normalized = normalize_column_name(col)

        for canonical, aliases in COLUMN_ALIASES.items():
            if normalized in aliases:
                rename_map[col] = canonical
                break

    return df.rename(columns=rename_map)