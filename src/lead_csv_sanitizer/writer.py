from pathlib import Path
import json
import csv
import pandas as pd

from lead_csv_sanitizer.report import build_summary


CRM_COLUMNS = [
    "first_name",
    "last_name",
    "email",
    "phone",
    "company",
]


def split_clean_and_rejected(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split dataframe into cleaned and rejected rows.

    Rejected rows = rows with no email AND no phone.
    """

    df = df.copy()

    rejected_mask = df["email"].isna() & df["sanitized_phone"].isna()

    cleaned_df = df.loc[~rejected_mask].copy()
    rejected_df = df.loc[rejected_mask].copy()

    return cleaned_df, rejected_df


def build_crm_export(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build CRM import-ready dataset.

    Uses sanitized_phone instead of raw phone.
    """

    crm_df = df.copy()

    if "sanitized_phone" in crm_df.columns:
        crm_df["phone"] = crm_df["sanitized_phone"]

    cols = [c for c in CRM_COLUMNS if c in crm_df.columns]

    return crm_df[cols]


def write_outputs(df: pd.DataFrame, output_dir: Path) -> dict:
    """
    Write all output files.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    cleaned_df, rejected_df = split_clean_and_rejected(df)

    crm_df = build_crm_export(cleaned_df)

    cleaned_path = output_dir / "cleaned_leads.csv"
    rejected_path = output_dir / "rejected_rows.csv"
    crm_path = output_dir / "crm_import_ready.csv"
    report_path = output_dir / "sanitizer_report.json"

    # audit dataset
    cleaned_df.to_csv(cleaned_path, index=False)

    # rejected dataset
    rejected_df.to_csv(rejected_path, index=False)

    # CRM-ready dataset
    crm_df.to_csv(
        crm_path,
        index=False,
        quoting=csv.QUOTE_ALL
    )

    report = build_summary(df)

    report["cleaned_rows"] = int(len(cleaned_df))
    report["rejected_rows"] = int(len(rejected_df))

    report["output_files"] = {
        "cleaned_csv": str(cleaned_path),
        "crm_import_ready": str(crm_path),
        "rejected_csv": str(rejected_path),
        "report_json": str(report_path),
    }

    with report_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return report