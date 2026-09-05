def clamp(value: int | float, low: int | float, high: int | float) -> int | float:
    if any(isinstance(x, bool) for x in (value, low, high)):
        raise TypeError("clamp requires numeric arguments")
    if not all(isinstance(x, (int, float)) for x in (value, low, high)):
        raise TypeError("clamp requires numeric arguments")
    if low > high:
        raise ValueError("low must not be greater than high")

    if value <= low:
        result: int | float = low
    elif value > high:
        result = high
    else:
        result = value

    if isinstance(value, int) and isinstance(low, int) and isinstance(high, int):
        return int(result)
    return float(result)
