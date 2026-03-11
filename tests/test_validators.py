import pandas as pd

from lead_csv_sanitizer.validators import validate_dataframe


def test_email_validation():
    df = pd.DataFrame({
        "email": [
            "john@example.com",
            "invalid@@example",
        ]
    })

    result = validate_dataframe(df)

    assert result["valid_email"].tolist() == [True, False]


def test_phone_normalization():
    df = pd.DataFrame({
        "phone": [
            "+420 777 123 456",
            "123"
        ]
    })

    result = validate_dataframe(df)

    assert result["valid_phone"].tolist() == [True, False]