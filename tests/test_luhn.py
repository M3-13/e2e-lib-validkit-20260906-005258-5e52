import pytest

from validkit.luhn import luhn_check

VALID_NUMBER = "4532015112830366"


def test_valid_number_returns_true():
    assert luhn_check(VALID_NUMBER) is True


def test_valid_number_with_spaces_returns_true():
    assert luhn_check("4532 0151 1283 0366") is True


def test_valid_number_with_hyphens_returns_true():
    assert luhn_check("4532-0151-1283-0366") is True


def test_invalid_check_digit_returns_false():
    assert luhn_check("4532015112830365") is False


def test_all_zeros_returns_true():
    assert luhn_check("0000000000000000") is True


@pytest.mark.parametrize(
    "value",
    [
        "",
        "   ",
        "----",
        "4532 0151 1283 036a",
        "abc",
        "4532!0151",
    ],
)
def test_invalid_input_raises_value_error(value):
    with pytest.raises(ValueError):
        luhn_check(value)


def test_input_over_length_limit_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("1" * 1025)


def test_input_at_length_limit_does_not_raise():
    assert luhn_check("0" * 1024) is True
