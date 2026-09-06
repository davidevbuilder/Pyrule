"""
PYRULE 0.3.0 - RULE UTILITIES

Utility functions responsible for processing and validating PyRule
rules against provided values.

This module contains the core logic used to inspect rules and determine
whether a value satisfies the specified conditions.

The module supports different types of rules, including:

    - Comparison rules
    - Type rules
    - String rules
    - Collection rules
    - Logical rules such as And and Or

The ``inspect_value()`` function is responsible for processing a rule
or a collection of rules.

The ``check_rule()`` function performs the actual validation of a
single rule against a value.

If a value does not satisfy a rule, ``RuleNotSatisfiedError`` is raised.

Example:

    inspect_value(
        GreaterThan(10),
        15
    )
"""


from .rules_exeptions import (
    RuleNotSatisfiedError,
    ParameterNotProvidedError
)

from .rule_comparations import (
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
)

from .rule_types import (
    Is,
    IsNot
)


def inspect_value(rule, value):
    """
    Inspects a rule and checks whether a value satisfies it.

    This function supports individual rules, tuples of rules, and
    logical rules such as ``And`` and ``Or``.

    Args:
        rule:
            The rule or collection of rules to be inspected.

        value:
            The value that will be validated.

    Returns:
        bool:
            Returns ``True`` when the value satisfies the rule.

    Raises:
        RuleNotSatisfiedError:
            If the value does not satisfy the specified rule.

    Example:
        >>> inspect_value(GreaterThan(10), 20)
        True

        >>> inspect_value(
        ...     Or(GreaterThan(10), Equals(5)),
        ...     5
        ... )
        True
    """

    if isinstance(rule, tuple):
        for element in rule:

            if isinstance(element, And):
                for elements_values in element.rules:
                    check_rule(elements_values, value)

            elif isinstance(element, Or):
                or_satisfied = False

                for elements_values in element.rules:
                    try:
                        check_rule(elements_values, value)
                        or_satisfied = True
                        break

                    except RuleNotSatisfiedError:
                        pass

                if not or_satisfied:
                    raise RuleNotSatisfiedError(
                        'None of the OR rules were satisfied.'
                    )

            else:
                check_rule(element, value)

    else:
        check_rule(rule, value)

    return True


def check_rule(rule, value):
    """
    Checks a single rule against a provided value.

    This function contains the validation logic for the different
    rule types available in PyRule.

    Args:
        rule:
            The rule that will be checked.

        value:
            The value that will be compared against the rule.

    Returns:
        None:
            The function completes without returning a value when
            the rule is satisfied.

    Raises:
        RuleNotSatisfiedError:
            If the value does not satisfy the specified rule.

    Example:
        >>> check_rule(GreaterThan(10), 20)

        >>> check_rule(Equals("Davi"), "Davi")
    """

    if isinstance(rule, GreaterThan):
        if type(value) == int and value < rule.value:
            raise RuleNotSatisfiedError(
                'The amount is less than what is necessary.'
            )

    if isinstance(rule, SmallerThan):
        if type(value) == int and value > rule.value:
            raise RuleNotSatisfiedError(
                'The amount exceeds the permitted limit.'
            )

    if isinstance(rule, In):
        if value not in rule.structure:
            raise RuleNotSatisfiedError(
                'The value is not within the mentioned structure.'
            )

    if isinstance(rule, Equals):
        if value != rule.value:
            raise RuleNotSatisfiedError(
                'The value is not equal as the configured value.'
            )

    if isinstance(rule, NotEquals):
        if value == rule.value:
            raise RuleNotSatisfiedError(
                'The value is equal to the configured value.'
            )

    if isinstance(rule, GreaterThanOrEqual):
        if value < rule.value:
            raise RuleNotSatisfiedError(
                'The value exceeds the configured limit.'
            )

    if isinstance(rule, SmallerThanOrEqual):
        if value > rule.value:
            raise RuleNotSatisfiedError(
                'The value exceeds the configured limit.'
            )

    if isinstance(rule, Is):
        if type(value) != rule.value:
            raise RuleNotSatisfiedError(
                'The value type does not match the configured type.'
            )

    if isinstance(rule, IsNot):
        if type(value) == rule.value:
            raise RuleNotSatisfiedError(
                'The value type does not match the configured type.'
            )

    if isinstance(rule, StartsWith):
        str_len = len(rule.value)

        if value[:str_len] != rule.value:
            raise RuleNotSatisfiedError(
                'The value type does not match the configured type.'
            )

    if isinstance(rule, EndsWith):
        str_len = len(rule.value)

        if value[-str_len:] != rule.value:
            raise RuleNotSatisfiedError(
                'The value type does not match the configured type.'
            )

    if isinstance(rule, Contains):
        if not rule.value in value:
            raise RuleNotSatisfiedError(
                'The value type does not match the configured type.'
            )

    if isinstance(rule, Length):
        if len(value) < rule.min or len(value) > rule.max:
            raise RuleNotSatisfiedError(
                'The value type does not match the configured type.'
            )