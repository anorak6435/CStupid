class Token:
    def __init__(self, name: str, value : str) -> None:
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"(TOKEN '{self.name}'::'{self.value}')"
