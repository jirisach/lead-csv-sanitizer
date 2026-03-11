import pandas as pd
from typing import List


REQUIRED_FIELDS = ["first_name", "last_name", "email", "phone", "company"]


def build_issue_flags(row: pd.Series) -> str:
    flags: List[str] = []

    if "valid_email" in row and not bool(row["valid_email"]):
        flags.append("invalid_email")

    if "valid_phone" in row and not bool(row["valid_phone"]):
        flags.append("invalid_phone")

    if "duplicate_email" in row and bool(row["duplicate_email"]):
        flags.append("duplicate_email")

    if "duplicate_phone" in row and bool(row["duplicate_phone"]):
        flags.append("duplicate_phone")

    for field in REQUIRED_FIELDS:
        if field in row.index and pd.isna(row[field]):
            flags.append(f"missing_{field}")

    return ";".join(flags)


def enrich_with_issue_flags(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["issue_flags"] = df.apply(build_issue_flags, axis=1)
    return df


def calculate_data_health_score(summary: dict) -> int:
    """
    Calculate data health score (0-100).
    """

    total = summary["total_rows"]

    if total == 0:
        return 0

    valid_email_ratio = summary["valid_emails"] / total
    valid_phone_ratio = summary["valid_phones"] / total
    duplicate_penalty = summary["duplicates"] / total

    missing_fields = (
        summary["missing_first_name"]
        + summary["missing_last_name"]
        + summary["missing_email"]
        + summary["missing_phone"]
        + summary["missing_company"]
    ) / (total * len(REQUIRED_FIELDS))

    score = (
        valid_email_ratio * 40
        + valid_phone_ratio * 20
        + (1 - duplicate_penalty) * 20
        + (1 - missing_fields) * 20
    )

    return int(round(score))


def build_summary(df: pd.DataFrame) -> dict:
    summary = {
        "total_rows": int(len(df)),
        "valid_emails": int(df["valid_email"].sum()) if "valid_email" in df.columns else 0,
        "valid_phones": int(df["valid_phone"].sum()) if "valid_phone" in df.columns else 0,
        "duplicates": int(df["is_duplicate"].sum()) if "is_duplicate" in df.columns else 0,
    }

    for field in REQUIRED_FIELDS:
        if field in df.columns:
            summary[f"missing_{field}"] = int(df[field].isna().sum())
        else:
            summary[f"missing_{field}"] = int(len(df))

    summary["data_health_score"] = calculate_data_health_score(summary)

    return summary