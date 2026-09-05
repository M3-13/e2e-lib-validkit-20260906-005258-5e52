import pytest

from validkit.iban import is_valid_iban


def test_valid_iban_with_spaces():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_iban_without_spaces():
    assert is_valid_iban("DE89370400440532013000") is True


def test_valid_iban_other_countries():
    assert is_valid_iban("GB29 NWBK 6016 1331 9268 19") is True
    assert is_valid_iban("FR14 2004 1010 0505 0001 3M02 606") is True
    assert is_valid_iban("NL91 ABNA 0417 1643 00") is True


def test_manipulated_check_digits_return_false():
    assert is_valid_iban("DE89 3704 0044 0532 0130 01") is False
    assert is_valid_iban("DE88370400440532013000") is False


def test_manipulated_bban_returns_false():
    assert is_valid_iban("DE89 3704 0044 0532 0131 00") is False
    assert is_valid_iban("GB29NWBK60161331926818") is False


def test_minimum_length_valid_iban():
    assert is_valid_iban("NO93 8601 1117 947") is True


def test_too_short_returns_false():
    assert is_valid_iban("NO938601111794") is False


def test_too_long_returns_false():
    assert is_valid_iban("DE" + "0" * 33) is False


def test_lowercase_country_code_returns_false():
    assert is_valid_iban("de89370400440532013000") is False


def test_invalid_characters_return_false():
    assert is_valid_iban("DE89!70400440532013000") is False
    assert is_valid_iban("DE89 3704 0044 0532 0130 0O") is False


def test_wrong_structure_returns_false():
    assert is_valid_iban("D889370400440532013000") is False
    assert is_valid_iban("DE8X370400440532013000") is False


def test_empty_string_raises_valueerror():
    with pytest.raises(ValueError):
        is_valid_iban("")


def test_whitespace_only_raises_valueerror():
    with pytest.raises(ValueError):
        is_valid_iban("   ")


def test_non_string_raises_typeerror():
    with pytest.raises(TypeError):
        is_valid_iban(123456789)
    with pytest.raises(TypeError):
        is_valid_iban(None)


def test_over_length_limit_raises_valueerror():
    with pytest.raises(ValueError):
        is_valid_iban("A" * 1025)


def test_error_message_does_not_contain_input():
    secret = "DE89 3704 0044 0532 0130 00"
    with pytest.raises(ValueError):
        is_valid_iban("A" * 1025)
    try:
        is_valid_iban("")
    except ValueError as exc:
        assert secret not in str(exc)
