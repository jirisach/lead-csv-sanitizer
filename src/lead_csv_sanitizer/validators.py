import re
from typing import Optional

import pandas as pd
import phonenumbers


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email: object) -> bool:
    """
    Basic email validation.
    """
    if email is None or pd.isna(email):
        return False

    email_str = str(email).strip().lower()

    if not email_str:
        return False

    return bool(EMAIL_PATTERN.match(email_str))


def normalize_phone(phone: object, default_country: str = "CZ") -> Optional[str]:
    """
    Normalize phone numbers to E.164 format.

    Example:
    +420777123456
    """

    if phone is None or pd.isna(phone):
        return None

    phone_str = str(phone).strip()

    if not phone_str:
        return None

    try:
        parsed = phonenumbers.parse(phone_str, default_country)

        if not phonenumbers.is_valid_number(parsed):
            return None

        return phonenumbers.format_number(
            parsed,
            phonenumbers.PhoneNumberFormat.E164
        )

    except phonenumbers.NumberParseException:
        return None


def validate_dataframe(df: pd.DataFrame, default_country: str = "CZ") -> pd.DataFrame:
    """
    Add validation columns to dataframe.
    """

    df = df.copy()

    # email validation
    if "email" in df.columns:

        df["email"] = df["email"].apply(
            lambda x: str(x).strip().lower()
            if x is not None and not pd.isna(x)
            else x
        )

        df["valid_email"] = df["email"].apply(is_valid_email)

    else:
        df["valid_email"] = False

    # phone normalization
    if "phone" in df.columns:

        df["sanitized_phone"] = df["phone"].apply(
            lambda x: normalize_phone(x, default_country)
        )

        df["valid_phone"] = df["sanitized_phone"].notna()

    else:
        df["sanitized_phone"] = None
        df["valid_phone"] = False

    return df