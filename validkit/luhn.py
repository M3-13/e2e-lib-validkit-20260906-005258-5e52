from validkit._common import ensure_length_ok


def luhn_check(digits: str) -> bool:
    ensure_length_ok(digits)

    cleaned = digits.replace(" ", "").replace("-", "")

    if not cleaned:
        raise ValueError("input must contain digits")

    if not cleaned.isdecimal():
        raise ValueError("input must contain only digits")

    total = 0
    for index, char in enumerate(reversed(cleaned)):
        digit = int(char)
        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0
