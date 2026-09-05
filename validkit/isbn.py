from validkit._common import ensure_length_ok


def is_valid_isbn13(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("expected a string")

    ensure_length_ok(text)

    digits = text.replace("-", "").replace(" ", "")
    if len(digits) != 13 or not digits.isdigit():
        return False

    total = 0
    for index, char in enumerate(digits):
        weight = 1 if index % 2 == 0 else 3
        total += int(char) * weight

    return total % 10 == 0
