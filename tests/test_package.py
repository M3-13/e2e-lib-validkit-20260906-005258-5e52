import validkit

EXPECTED_NAMES = {
    "clamp",
    "is_valid_email",
    "is_valid_iban",
    "is_valid_isbn13",
    "luhn_check",
    "mask_secret",
    "normalize_phone",
    "slugify",
    "strip_accents",
}


def test_all_contains_exactly_nine_names():
    assert len(validkit.__all__) == 9
    assert set(validkit.__all__) == EXPECTED_NAMES


def test_every_exported_name_is_callable():
    for name in validkit.__all__:
        assert callable(getattr(validkit, name)), f"{name} is not callable"
