class PyMultiFuncException(Exception):
    """Base exception for all `PyMultiFunc` related errors."""
    pass




"""
PyMultiFuncNoOverideException:
    - Exceptions responsible for the lack of proper overload
"""
class PyMultiFuncNoOverideException(PyMultiFuncException):
    pass


class NoOverideError(PyMultiFuncException):
    """
    This exception is raised when python does not find the desired overload
    """
    pass




"""
PyMultiFuncDefaultArgException:
    - A subgroup of exceptions related to issues with default arguments.
"""
class PyMultiFuncDefaultArgException(PyMultiFuncException):
    pass


class NoDefaultsArgsError(PyMultiFuncDefaultArgException):
    """
    Raised when a `DEFAULT_ARG` marker is passed,
    but the target function has no parameters with default values.
    """
    pass


class NoDefaultValueForThisArgError(PyMultiFuncDefaultArgException):
    """
    Raised when a `DEFAULT_ARG` marker is passed for a parameter
    that does not have a default value.
    This may indicate a mismatch between argument position and its default value.
    """
    pass
