"""
PYRULE 0.3.0 - RULE TYPES

Base classes and type-related rules provided by PyRule.

This module contains the ``RuleType`` base class, which provides
the common structure used by type-based rules.

Available type rules:

    - Is
        Checks whether a value is exactly of the specified type.

    - IsNot
        Checks whether a value is not of the specified type.

All type-based rules inherit from ``RuleType`` and store the
type or value they should be compared against.

Example:

    rule = Is(int)

    # The value must be an integer.
"""


from abc import ABC


class RuleType(ABC):
    """
    Base class for type-related PyRule rules.

    Args:
        value:
            The type or value that the rule will use for validation.
    """

    def __init__(self, value):
        self.value = value


class Is(RuleType):
    """
    Checks whether a value is exactly of the specified type.

    Args:
        value:
            The expected type.

    Example:
        >>> rule = Is(int)
        >>> rule.value
        <class 'int'>
    """

    def __init__(self, value):
        super().__init__(value)


class IsNot(RuleType):
    """
    Checks whether a value is not of the specified type.

    Args:
        value:
            The type that the value must not be.

    Example:
        >>> rule = IsNot(str)
        >>> rule.value
        <class 'str'>
    """

    def __init__(self, value):
        super().__init__(value)


RULE_TYPES_LIST = [
    RuleType,
    Is,
    IsNot
]