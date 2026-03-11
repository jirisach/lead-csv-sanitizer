import pandas as pd

from lead_csv_sanitizer.column_mapper import map_columns


def test_column_mapping():
    df = pd.DataFrame({
        "First Name": ["Jiri"],
        "Last Name": ["Sach"],
        "EMAIL": ["jiri@example.com"],
        "Phone": ["+420777123456"],
        "Company Name": ["Artwear"]
    })

    mapped = map_columns(df)

    assert "first_name" in mapped.columns
    assert "last_name" in mapped.columns
    assert "email" in mapped.columns
    assert "phone" in mapped.columns
    assert "company" in mapped.columns