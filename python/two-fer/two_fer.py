def two_fer(name: str | None = None) -> str:
    """Return the "one for X, one for me" phrase for the given name."""
    return f"One for {name or 'you'}, one for me."
