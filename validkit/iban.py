import re

from validkit._common import ensure_length_ok

_IBAN_PATTERN = re.compile(r"^[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}$")


def is_valid_iban(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("iban must be a string")
    ensure_length_ok(text)

    iban = text.replace(" ", "")
    if not iban:
        raise ValueError("iban must not be empty")
    if _IBAN_PATTERN.fullmatch(iban) is None:
        return False

    rearranged = iban[4:] + iban[:4]
    digits = "".join(ch if ch.isdigit() else str(ord(ch) - ord("A") + 10) for ch in rearranged)
    return int(digits) % 97 == 1
