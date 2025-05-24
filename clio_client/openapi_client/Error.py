class Error:
    def __init__(self, type=None, message=None):
        self.type = type
        self.message = message

    @classmethod
    def from_dict(cls, data):
        error = data.get("error", data)
        return cls(
            type=error.get("type"),
            message=error.get("message"),
        )

    def __repr__(self):
        return f"<Error type={self.type!r} message={self.message!r}>"