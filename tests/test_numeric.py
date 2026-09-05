import pytest

from validkit.numeric import clamp


def test_clamp_upper_bound():
    assert clamp(15, 0, 10) == 10


def test_clamp_lower_bound():
    assert clamp(-5, 0, 10) == 0


def test_clamp_within_range_is_unchanged():
    assert clamp(5, 0, 10) == 5


def test_clamp_returns_int_for_pure_int_input():
    assert type(clamp(5, 0, 10)) is int


def test_clamp_returns_float_when_value_is_float():
    assert type(clamp(5.5, 0, 10)) is float


def test_clamp_returns_float_when_bound_is_float():
    assert clamp(5, 0.0, 10) == 5.0
    assert type(clamp(5, 0.0, 10)) is float


def test_clamp_value_at_low_boundary():
    assert clamp(0, 0, 10) == 0
    assert type(clamp(0, 0, 10)) is int


def test_clamp_value_at_high_boundary():
    assert clamp(10, 0, 10) == 10


def test_clamp_single_point_range():
    assert clamp(0, 0, 0) == 0


def test_clamp_single_point_range_clamps_both_sides():
    assert clamp(-1, 0, 0) == 0
    assert clamp(1, 0, 0) == 0


def test_clamp_float_value_clamped_to_float_bound():
    assert clamp(12.5, 0, 10) == 10.0


def test_clamp_negative_range():
    assert clamp(-3, -10, -2) == -3
    assert clamp(-11, -10, -2) == -10


def test_clamp_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)


def test_clamp_non_numeric_value_raises_type_error():
    with pytest.raises(TypeError):
        clamp("5", 0, 10)


def test_clamp_non_numeric_low_raises_type_error():
    with pytest.raises(TypeError):
        clamp(5, "0", 10)


def test_clamp_non_numeric_high_raises_type_error():
    with pytest.raises(TypeError):
        clamp(5, 0, "10")


def test_clamp_none_raises_type_error():
    with pytest.raises(TypeError):
        clamp(5, 0, None)


def test_clamp_bool_raises_type_error():
    with pytest.raises(TypeError):
        clamp(True, 0, 10)


def test_clamp_error_messages_do_not_leak_input_value():
    with pytest.raises(ValueError) as excinfo:
        clamp(5, 10, 0)
    assert "5" not in str(excinfo.value)
    assert "10" not in str(excinfo.value)
    assert "0" not in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        clamp("secret-input", 0, 10)
    assert "secret-input" not in str(excinfo.value)
