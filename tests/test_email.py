import pytest

from validkit.email import is_valid_email


@pytest.mark.parametrize(
    "text",
    [
        "user@example.com",
        "firstname.lastname@example.co.uk",
        "user+tag@sub.domain.example.com",
        "user_name@example-domain.com",
        "a@b.co",
        "user123@mail.example.org",
    ],
)
def test_valid_emails(text):
    assert is_valid_email(text) is True


@pytest.mark.parametrize(
    "text",
    [
        "nicht@valide",
        "plainaddress",
        "user@example",
        "@example.com",
        "user@.com",
        "user@example..com",
        "user@example.com.",
        "user @example.com",
        "user@exam ple.com",
        "user@@example.com",
        "user@example.c",
        "üser@example.com",
        "user name@example.com",
        ".user@example.com",
        "user.@example.com",
        "user@-example.com",
        "user@example-.com",
        "",
    ],
)
def test_invalid_emails_return_false_without_raising(text):
    assert is_valid_email(text) is False


def test_length_limit_boundary_is_valid():
    assert is_valid_email("a" * 1019 + "@b.co") is True


def test_length_exceeding_limit_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_email("a" * 1025)


def test_length_error_message_does_not_contain_input():
    long_value = "x" * 1025
    with pytest.raises(ValueError) as excinfo:
        is_valid_email(long_value)
    assert long_value not in str(excinfo.value)


def test_non_string_input_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_email(123)  # type: ignore[arg-type]
