class UnmatchedSourceError(Exception):
    def __init__(self, sourceStream, line, index):
        self.message = f"Could not match a token in the source:'{sourceStream}' on line:{line}, index:{index}"
        super().__init__(self.message)

    def __str__(self):
        return self.message