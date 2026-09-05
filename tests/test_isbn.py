import pytest

from validkit.isbn import is_valid_isbn13


def test_valid_isbn13_with_hyphens():
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn13_without_separators():
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn13_with_spaces():
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_wrong_check_digit():
    assert is_valid_isbn13("978-3-16-148410-1") is False


def test_too_short():
    assert is_valid_isbn13("978-3-16-148410") is False


def test_too_long():
    assert is_valid_isbn13("978-3-16-148410-00") is False


def test_non_digit_character():
    assert is_valid_isbn13("978-3-16-14841X-0") is False


def test_empty_string():
    assert is_valid_isbn13("") is False


def test_only_separators():
    assert is_valid_isbn13("   --  ") is False


def test_length_limit_exceeded_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("1" * 1025)


def test_at_length_limit_is_evaluated():
    padded = "9783161484100" + " " * (1024 - 13)
    assert is_valid_isbn13(padded) is True


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(None)


def test_int_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(9783161484100)
