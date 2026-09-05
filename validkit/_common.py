MAX_INPUT_LENGTH = 1024


def ensure_length_ok(value: str) -> None:
    if len(value) > MAX_INPUT_LENGTH:
        raise ValueError("input exceeds maximum allowed length")
