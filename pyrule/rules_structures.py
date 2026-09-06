"""
PYRULE 0.3.0 - RULE COLLECTIONS

Rule collections provided by PyRule for creating lists and
dictionaries whose values must comply with a defined set of rules.

This module provides:

    - RuleList
        A list that validates every value before it is added.

    - RuleDict
        A dictionary that validates every value before it is added.

Values are checked using PyRule's rule system. If a value does not
satisfy one of the defined rules, the corresponding PyRule exception
is raised and the value is not added to the collection.

Example:

    numbers = RuleList(
        list=[],
        rules=(
            GreaterThan(0),
            SmallerThan(100)
        )
    )

    numbers.append(50)
"""


from .rules import (
    Rule
)

from .rules_exeptions import (
    RuleNotSatisfiedError,
    ParameterNotProvidedError
)

from .rule_comparations import (
    GreaterThan,
    SmallerThan,
    In
)

from .rule_utils import inspect_value

import inspect


class RuleList(Rule):
    """
    A list whose values must satisfy a defined set of rules.

    Every value added through ``append()`` is validated against all
    rules before being added to the list.

    Args:
        list (list):
            The list that will be used to store the values.

        rules (tuple):
            A tuple containing the rules that every value must satisfy.

    Example:
        >>> numbers = RuleList(
        ...     list=[],
        ...     rules=(
        ...         GreaterThan(0),
        ...         SmallerThan(100)
        ...     )
        ... )
        >>> numbers.append(50)
        >>> print(numbers)
        [50]

    Raises:
        RuleNotSatisfiedError:
            If the value does not satisfy one of the defined rules.
    """

    def __init__(self, list, rules):
        self.rules = rules
        self.list = list

    def add_value(self, *value):
        """
        Adds values to the collection of rules.

        Args:
            *value:
                Values to be added to the rules.

        Returns:
            The result of updating the rules.
        """
        return self.rules.update(value)

    def __str__(self):
        """
        Returns a string representation of the list.

        Returns:
            str: The contents of the list as a string.
        """
        return str(list(self.list))

    def append(self, value):
        """
        Validates and adds a value to the list.

        The value is checked against every rule before being added.
        If any rule is not satisfied, the value is not added.

        Args:
            value:
                The value to be added to the list.

        Raises:
            RuleNotSatisfiedError:
                If the value does not satisfy a rule.

        Example:
            >>> numbers.append(25)
        """
        for rule in self.rules:
            inspect_value(rule, value)

        self.list.append(value)


class RuleDict(Rule):
    """
    A dictionary whose values must satisfy a defined set of rules.

    Every value added through ``append()`` is validated against all
    rules before being added to the dictionary.

    Args:
        dict (dict):
            The dictionary that will be used to store the values.

        rules (tuple):
            A tuple containing the rules that every value must satisfy.

    Example:
        >>> data = RuleDict(
        ...     dict={
        ...         'name': 'davi',
        ...         'age': 13
        ...     },
        ...     rules=(
        ...         In([1, 4, 15, 'lisbon', 13]),
        ...         GreaterThan(10),
        ...         SmallerThan(100)
        ...     )
        ... )
        >>> data.append('age', 18)
    """

    def __init__(self, dict, rules):
        self.rules = rules
        self.dict = dict

    def add_value(self, *value):
        """
        Adds values to the collection of rules.

        Args:
            *value:
                Values to be added to the rules.

        Returns:
            The result of updating the rules.
        """
        return self.rules.update(value)

    def __str__(self):
        """
        Returns a string representation of the dictionary.

        Returns:
            str: The contents of the dictionary as a string.
        """
        return str(dict(self.dict))

    def append(self, key, value):
        """
        Validates and adds a key-value pair to the dictionary.

        The value is checked against every defined rule before being
        added to the dictionary.

        Args:
            key:
                The key to be added.

            value:
                The value associated with the key.

        Raises:
            RuleNotSatisfiedError:
                If the value does not satisfy a rule.

        Example:
            >>> data.append('city', 'Lisbon')
        """
        for rule in self.rules:
            inspect_value(rule, value)

        self.dict[key] = value
