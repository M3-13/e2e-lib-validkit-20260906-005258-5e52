import pytest

from validkit.secret import mask_secret


def test_default_keeps_last_four_characters():
    assert mask_secret("S3cret!") == "***ret!"
    assert mask_secret("abcdefgh") == "****efgh"


def test_keep_zero_masks_fully():
    assert mask_secret("S3cret!", 0) == "*******"


def test_negative_keep_behaves_like_zero():
    assert mask_secret("S3cret!", -3) == "*******"


def test_keep_greater_than_length_shows_whole_text():
    assert mask_secret("abc", 10) == "abc"


def test_keep_equal_to_length_shows_whole_text():
    assert mask_secret("abc", 3) == "abc"


def test_custom_keep_reveals_only_last_characters():
    assert mask_secret("S3cret!", 1) == "******!"


def test_empty_text_returns_empty_string():
    assert mask_secret("", 4) == ""
    assert mask_secret("", 0) == ""


def test_mask_characters_do_not_come_from_input():
    result = mask_secret("S3cret!", 4)
    assert result == "***ret!"
    assert result[:3] == "***"


def test_length_limit_is_enforced_before_masking():
    with pytest.raises(ValueError):
        mask_secret("a" * 1025)


def test_length_limit_allows_exact_maximum():
    assert mask_secret("a" * 1024, 0) == "*" * 1024


def test_error_message_does_not_contain_input_value():
    payload = "secret-value-that-must-not-leak"
    with pytest.raises(ValueError) as excinfo:
        mask_secret(payload * 40)
    assert payload not in str(excinfo.value)
