import pytest

from validkit.phone import normalize_phone


def test_normal_national_number():
    assert normalize_phone("030 1234567", "49") == "+49301234567"


def test_normal_with_separators():
    assert normalize_phone("030-123/45 67", "49") == "+49301234567"


def test_normal_international_plus():
    assert normalize_phone("+49 30 1234567", "49") == "+49301234567"


def test_normal_international_double_zero():
    assert normalize_phone("0049 30 1234567", "49") == "+49301234567"


def test_normal_no_spaces_national():
    assert normalize_phone("0301234567", "49") == "+49301234567"


def test_normal_single_digit_country_code():
    assert normalize_phone("212 555 1234", "1") == "+12125551234"


def test_normal_with_parentheses_and_dashes():
    assert normalize_phone("(030) 123-4567", "49") == "+49301234567"


def test_boundary_plus_only_number():
    assert normalize_phone("+4930", "49") == "+4930"


def test_boundary_input_at_max_length():
    assert normalize_phone("030" + "1" * 1021, "49") == "+4930" + "1" * 1021


def test_empty_input_raises():
    with pytest.raises(ValueError):
        normalize_phone("", "49")


def test_whitespace_only_raises():
    with pytest.raises(ValueError):
        normalize_phone("   ", "49")


def test_no_digits_raises():
    with pytest.raises(ValueError):
        normalize_phone("abc-def", "49")


def test_only_zeros_raises():
    with pytest.raises(ValueError):
        normalize_phone("000", "49")


def test_empty_country_code_raises():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "")


def test_non_digit_country_code_raises():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "4a")


def test_only_country_prefix_raises():
    with pytest.raises(ValueError):
        normalize_phone("+", "49")


def test_overlong_input_raises():
    with pytest.raises(ValueError):
        normalize_phone("0" * 1025, "49")


def test_error_message_does_not_leak_input():
    with pytest.raises(ValueError) as exc:
        normalize_phone("secretvalue", "49")
    assert "secretvalue" not in str(exc.value)
