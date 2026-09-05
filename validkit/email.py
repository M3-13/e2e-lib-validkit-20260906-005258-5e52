import re

from validkit._common import ensure_length_ok

_LOCAL_PART_RE = re.compile(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+")
_DOMAIN_LABEL_RE = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?")
_TLD_RE = re.compile(r"[A-Za-z]{2,}")


def is_valid_email(text: str) -> bool:
    ensure_length_ok(text)

    if text.count("@") != 1:
        return False

    local, domain = text.split("@")
    if not local or not domain:
        return False

    if _LOCAL_PART_RE.fullmatch(local) is None:
        return False
    if local.startswith(".") or local.endswith(".") or ".." in local:
        return False

    labels = domain.split(".")
    if len(labels) < 2:
        return False
    if "" in labels:
        return False
    if _TLD_RE.fullmatch(labels[-1]) is None:
        return False
    return all(_DOMAIN_LABEL_RE.fullmatch(label) is not None for label in labels[:-1])
