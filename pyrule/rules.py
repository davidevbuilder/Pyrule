"""
PyRule 0.3.0

A Python library designed to make conditions and rule-based validation
simpler, cleaner, and easier to understand.

PyRule allows you to create reusable rules and validate values against
different conditions, such as comparisons, types, collections, strings,
and logical rules.

Basic example:

    rule = Rule(name="Davi")

You can access the rules stored in a Rule object through the ``rules``
attribute:

    rule.rules["name"]

Values can then be checked against a rule using RuleValue:

    if RuleValue("Davi").check_rule(rule.rules["name"]):
        print("The value follows the rule!")

PyRule also provides several built-in rules, including:

    - GreaterThan
    - SmallerThan
    - GreaterThanOrEqual
    - SmallerThanOrEqual
    - Equals
    - NotEquals
    - In
    - Is
    - IsNot
    - StartsWith
    - EndsWith
    - Contains
    - Length
    - And
    - Or

Rules can be combined to create more expressive validations while
keeping the conditions in your code organized and readable.

The main goal of PyRule is to reduce repetitive conditional checks
and provide a simple and reusable way to define and validate rules.
"""

from .rules_exeptions import (
    ValueIsNotInRule
)

from .rule_comparations import (
    GreaterThan,
    SmallerThan,
    In,
    RULE_COMPARATIONS_LIST
)

from .rule_utils import inspect_value

from .rule_types import (
    RULE_TYPES_LIST
)

import inspect


class Rule:
    """
    Represents a collection of rules associated with named values.

    A Rule can contain multiple named conditions that can later be
    accessed through the ``rules`` attribute.

    Args:
        **rules: Named rules to be stored.

    Example:
        >>> rule = Rule(age=18)
        >>> rule.rules["age"]
        18
    """

    def __init__(self, **rules):
        self.rules = rules

    def __str__(self):
        for key, value in self.rules.items():
            return f'{key}: {value}'

    def add_value(self, **value):
        return self.rules.update(value)


class RuleValue:
    """
    Represents a value that can be checked against a PyRule rule.

    Args:
        value: The value to be validated.

    Example:
        >>> value = RuleValue("Davi")
        >>> value.check_rule("Davi")
        True
    """

    def __init__(self, value):
        self.value = value

    def check_rule(self, rule_item):
        """
        Checks whether the stored value satisfies the given rule.

        Args:
            rule_item: A rule or rule collection to be evaluated.

        Returns:
            bool: ``True`` when the value satisfies the rule.

        Raises:
            ValueIsNotInRule: If the value does not satisfy the rule.

        Example:
            >>> rule = RuleValue("Davi")
            >>> rule.check_rule("Davi")
            True
        """

        if self.value == rule_item:
            return True

        if isinstance(rule_item, In) and self.value in rule_item.structure:
            return True

        for i in range(0, len(rule_item)):
            print(rule_item[i])
            if rule_item[i].__class__ == RULE_COMPARATIONS_LIST[11] or RULE_COMPARATIONS_LIST[12]:
                return inspect_value(rule_item, self.value)

        if rule_item.__class__ in RULE_COMPARATIONS_LIST + RULE_TYPES_LIST:
            return inspect_value(rule_item, self.value)

        else:
            raise ValueIsNotInRule(
                '\033[91mThe value does not comply with the rule.'
            )