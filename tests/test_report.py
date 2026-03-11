import pandas as pd

from lead_csv_sanitizer.report import enrich_with_issue_flags


def test_issue_flags():
    df = pd.DataFrame([
        {
            "first_name": "Jiri",
            "last_name": "Sach",
            "email": "bad@@example.com",
            "phone": None,
            "company": "Artwear",
            "valid_email": False,
            "valid_phone": False,
            "duplicate_email": True,
            "duplicate_phone": False,
        }
    ])

    result = enrich_with_issue_flags(df)

    flags = result.loc[0, "issue_flags"]

    assert "invalid_email" in flags
    assert "invalid_phone" in flags
    assert "duplicate_email" in flags
    assert "missing_phone" in flags