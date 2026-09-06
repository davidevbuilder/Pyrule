"""
PYRULE 0.3.0 - RULE COMPARISONS

Comparison and logical rules provided by PyRule.

This module contains rules used to compare, validate, and combine
values according to specific conditions.

Available rules include:

    - GreaterThan
    Checks whether a value is greater than a specified value.

    - SmallerThan
        Checks whether a value is smaller than a specified value.

    - GreaterThanOrEqual
        Checks whether a value is greater than or equal to a value.

    - SmallerThanOrEqual
        Checks whether a value is smaller than or equal to a value.

    - Equals
        Checks whether a value is equal to a specified value.

    - NotEquals
        Checks whether a value is different from a specified value.

    - In
        Checks whether a value exists within a specified structure.

    - StartsWith
        Checks whether a value starts with a specified value.

    - EndsWith
        Checks whether a value ends with a specified value.

    - Contains
        Checks whether a value contains a specified value.

    - Length
        Checks whether the length of a value is within a specified range.

    - And
        Combines multiple rules that must all be satisfied.

    - Or
        Combines multiple rules where at least one must be satisfied.

The ``RuleComparation`` class serves as the base class for comparison
rules that operate using a reference value.
"""


from abc import ABC


class RuleComparation(ABC):
    """
    Base class for rules that operate with a comparison value.

    Args:
        value:
            The value used by the rule as a reference.
    """

    def __init__(self, value):
        self.value = value


class GreaterThan(RuleComparation):
    """
    Checks whether a value is greater than the value defined in the rule.

    Args:
        value:
            The minimum value that must be exceeded.

    Example:
        >>> GreaterThan(10)
        # 11 -> valid
        # 10 -> invalid
    """

    def __init__(self, value):
        super().__init__(value)


class SmallerThan(RuleComparation):
    """
    Checks whether a value is smaller than the value defined in the rule.

    Args:
        value:
            The maximum value that must not be reached.

    Example:
        >>> SmallerThan(10)
        # 9  -> valid
        # 10 -> invalid
    """

    def __init__(self, value):
        super().__init__(value)


class In:
    """
    Checks whether a value exists within a given structure.

    Args:
        structure:
            The structure containing the allowed values.

    Example:
        >>> In([1, 2, 3])
        # 2 -> valid
        # 5 -> invalid
    """

    def __init__(self, structure):
        self.structure = structure


class Equals(RuleComparation):
    """
    Checks whether a value is exactly equal to the value defined in the rule.

    Args:
        value:
            The value that must be equal to the analyzed value.

    Example:
        >>> Equals(10)
        # 10 -> valid
        # 5  -> invalid
    """

    def __init__(self, value):
        super().__init__(value)


class NotEquals(RuleComparation):
    """
    Checks whether a value is different from the value defined in the rule.

    Args:
        value:
            The value that must not be equal to the analyzed value.

    Example:
        >>> NotEquals(10)
        # 5  -> valid
        # 10 -> invalid
    """

    def __init__(self, value):
        super().__init__(value)


class GreaterThanOrEqual(RuleComparation):
    """
    Checks whether a value is greater than or equal to the value
    defined in the rule.

    Args:
        value:
            The minimum value that the analyzed value must reach.

    Example:
        >>> GreaterThanOrEqual(10)
        # 10 -> valid
        # 11 -> valid
        # 9  -> invalid
    """

    def __init__(self, value):
        super().__init__(value)


class SmallerThanOrEqual(RuleComparation):
    """
    Checks whether a value is smaller than or equal to the value
    defined in the rule.

    Args:
        value:
            The maximum value that the analyzed value can reach.

    Example:
        >>> SmallerThanOrEqual(10)
        # 10 -> valid
        # 9  -> valid
        # 11 -> invalid
    """

    def __init__(self, value):
        super().__init__(value)


class StartsWith(RuleComparation):
    """
    Checks whether a value starts with the value defined in the rule.

    Args:
        value:
            The prefix that the analyzed value must start with.

    Example:
        >>> StartsWith("Py")
        # "PyRule" -> valid
        # "Rule"   -> invalid
    """

    def __init__(self, value):
        super().__init__(value)


class EndsWith(RuleComparation):
    """
    Checks whether a value ends with the value defined in the rule.

    Args:
        value:
            The suffix that the analyzed value must end with.

    Example:
        >>> EndsWith("Rule")
        # "PyRule" -> valid
        # "PyTest" -> invalid
    """

    def __init__(self, value):
        super().__init__(value)


class Contains(RuleComparation):
    """
    Checks whether a value contains the value defined in the rule.

    Args:
        value:
            The value that must be contained within the analyzed value.

    Example:
        >>> Contains("Py")
        # "PyRule" -> valid
        # "Rule"   -> invalid
    """

    def __init__(self, value):
        super().__init__(value)


class Length:
    """
    Checks whether the length of a value is within a specified range.

    Args:
        min:
            The minimum allowed length.

        max:
            The maximum allowed length.

    Example:
        >>> Length(3, 10)
        # "Python" -> valid
        # "Py"     -> invalid
        # "PythonLibrary" -> invalid
    """

    def __init__(self, min, max):
        self.max = max
        self.min = min


class And:
    """
    Combines multiple rules that must all be satisfied.

    Args:
        *rules:
            The rules that must all be satisfied.

    Example:
        >>> And(
        ...     GreaterThan(10),
        ...     SmallerThan(100)
        ... )
        # 50 -> valid
        # 5  -> invalid
    """

    def __init__(self, *rules):
        self.rules = rules


class Or:
    """
    Combines multiple rules where at least one must be satisfied.

    Args:
        *rules:
            The rules where at least one must be satisfied.

    Example:
        >>> Or(
        ...     Equals(10),
        ...     Equals(20)
        ... )
        # 10 -> valid
        # 20 -> valid
        # 15 -> invalid
    """

    def __init__(self, *rules):
        self.rules = rules


RULE_COMPARATIONS_LIST = [
    GreaterThan,
    SmallerThan,
    In,
    Equals,
    NotEquals,
    GreaterThanOrEqual,
    SmallerThanOrEqual,
    StartsWith,
    EndsWith,
    Contains,
    Length,
    And,
    Or
]