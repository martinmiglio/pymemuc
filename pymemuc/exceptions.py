"""PyMemuc exceptions module"""

from subprocess import TimeoutExpired


class PyMemucError(Exception):
    """PyMemuc error class"""

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return repr(self.value)


class PyMemucException(Exception):
    """PyMemuc exception class"""

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return repr(self.value)


class PyMemucIndexError(PyMemucException):
    """PyMemuc index error class"""

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return repr(self.value)


class PyMemucTimeoutExpired(TimeoutExpired):
    """PyMemuc timeout error class"""

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return repr(self.value)
