import pytest

from validkit.text import slugify, strip_accents


def test_strip_accents_umlaut():
    assert strip_accents("Grüße") == "Gruße"


def test_strip_accents_acute_and_diaeresis():
    assert strip_accents("Héllo Wörld!") == "Hello World!"


def test_strip_accents_preserves_sharp_s():
    assert strip_accents("Straße") == "Straße"


def test_strip_accents_leaves_plain_text_unchanged():
    assert strip_accents("plain ascii 123") == "plain ascii 123"


def test_strip_accents_empty():
    assert strip_accents("") == ""


def test_strip_accents_combining_only():
    assert strip_accents("u\u0308") == "u"


def test_slugify_basic():
    assert slugify("Héllo Wörld!") == "hello-world"


def test_slugify_sharp_s_becomes_ss():
    assert slugify("Grüße") == "grusse"


def test_slugify_collapses_whitespace():
    assert slugify("  Hello   World  ") == "hello-world"


def test_slugify_punctuation_to_dash():
    assert slugify("Café & Restaurant") == "cafe-restaurant"


def test_slugify_lowercases_and_keeps_digits():
    assert slugify("Test123") == "test123"


def test_slugify_already_clean():
    assert slugify("already-clean") == "already-clean"


def test_slugify_empty():
    assert slugify("") == ""


def test_slugify_only_symbols():
    assert slugify("!!!") == ""


def test_slugify_only_dashes():
    assert slugify("---") == ""


def test_strip_accents_length_limit_boundary():
    assert strip_accents("a" * 1024) == "a" * 1024


def test_slugify_length_limit_boundary():
    assert slugify("a" * 1024) == "a" * 1024


@pytest.mark.parametrize("func", [strip_accents, slugify])
def test_length_over_limit_raises_value_error(func):
    with pytest.raises(ValueError):
        func("a" * 1025)


@pytest.mark.parametrize("func", [strip_accents, slugify])
def test_error_message_does_not_contain_input(func):
    marker = "SENSITIVE-VALUE-42"
    payload = marker + "a" * 2000
    with pytest.raises(ValueError) as excinfo:
        func(payload)
    assert marker not in str(excinfo.value)
