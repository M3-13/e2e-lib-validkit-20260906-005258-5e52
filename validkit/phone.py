import re

from validkit._common import ensure_length_ok

_NON_DIGITS = re.compile(r"\D")


def normalize_phone(text: str, country_code: str) -> str:
    ensure_length_ok(text)
    ensure_length_ok(country_code)

    if not country_code or not country_code.isdigit():
        raise ValueError("country code must be a non-empty digit string")

    stripped = text.strip()
    if not stripped:
        raise ValueError("input is empty")

    if stripped.startswith("+"):
        digits = _NON_DIGITS.sub("", stripped)
    elif stripped.startswith("00"):
        digits = _NON_DIGITS.sub("", stripped[2:])
    else:
        digits = _NON_DIGITS.sub("", stripped).lstrip("0")
        if digits:
            digits = country_code + digits

    if not digits or not digits.strip("0"):
        raise ValueError("input contains no usable digits")

    return "+" + digits
