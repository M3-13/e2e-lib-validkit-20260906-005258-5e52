from validkit._common import ensure_length_ok

MASK_CHAR = "*"


def mask_secret(text: str, keep: int = 4) -> str:
    ensure_length_ok(text)
    if keep <= 0:
        return MASK_CHAR * len(text)
    if keep >= len(text):
        return text
    return MASK_CHAR * (len(text) - keep) + text[-keep:]
