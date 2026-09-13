def steps(number: int) -> int:
    """Return the number of Collatz steps needed to reach 1."""
    count = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        number = number // 2 if number % 2 == 0 else number * 3 + 1
        count += 1
    return count
