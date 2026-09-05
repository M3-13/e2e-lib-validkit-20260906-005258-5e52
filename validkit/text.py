import unicodedata

from validkit._common import ensure_length_ok


def strip_accents(text: str) -> str:
    """Remove diacritical marks via Unicode normalization.

    The input is normalized to NFD form and every combining mark
    (Unicode category ``Mn``) is dropped. ``ß`` is not a diacritic and is
    therefore preserved (e.g. ``"Grüße"`` -> ``"Gruße"``).
    """
    ensure_length_ok(text)
    normalized = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")


def slugify(text: str) -> str:
    """Turn text into a clean, lowercase, URL-safe slug.

    Uses :func:`strip_accents`, replaces ``ß`` with ``ss``, folds every
    character that is not ``[a-z0-9]`` into ``-``, collapses consecutive
    separators and strips leading/trailing ``-``.
    """
    ensure_length_ok(text)
    stripped = strip_accents(text).replace("ß", "ss").lower()
    slug: list[str] = []
    for ch in stripped:
        if "a" <= ch <= "z" or "0" <= ch <= "9":
            slug.append(ch)
        elif slug and slug[-1] != "-":
            slug.append("-")
    return "".join(slug).strip("-")
