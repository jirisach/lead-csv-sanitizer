import pandas as pd

from lead_csv_sanitizer.dedupe import detect_duplicates


def test_duplicate_detection():
    df = pd.DataFrame({
        "email": [
            "a@example.com",
            "a@example.com",
            "b@example.com"
        ],
        "sanitized_phone": [
            "+420777123456",
            "+420777123456",
            "+420605111222"
        ]
    })

    result = detect_duplicates(df)

    assert result["is_duplicate"].sum() == 2