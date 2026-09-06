"""
PYRULE 0.3.0 - RULE FUNCTIONS

Tools for creating and applying rules to function parameters.

This module allows PyRule to validate function parameters before
the function is executed. Rules can be associated with specific
parameters using ``RuleFunction`` and applied to functions through
the ``ruledfunction`` decorator.

A rule function can define conditions for one or more parameters.

Example:

    function_rules = RuleFunction(
        age="<18"
    )

The rules can then be applied to a function:

    @ruledfunction(function_rules)
    def hello(age):
        print(f"Hello! You are {age} years old.")

When the function is called, its arguments are checked against
the defined rules before the original function is executed.

Example:

    hello(15)
    # The rule is satisfied and the function executes.

    hello(20)
    # RuleNotSatisfiedError is raised.

If a parameter required by a rule is not provided,
``ParameterNotProvidedError`` is raised.

Rule Functions are useful for keeping parameter validation
separate from the function's main logic and reducing repetitive
conditional checks.

The main goal of this module is to make function parameter
validation simpler, more readable, and easier to maintain.
"""


import inspect

from functools import wraps

from .rules import Rule

from .rules_exeptions import (
    RuleNotSatisfiedError,
    ParameterNotProvidedError
)

from .rule_comparations import (
    GreaterThan,
    SmallerThan,
    In
)


class RuleFunction(Rule):
    """
    Represents a collection of rules intended for function parameters.

    ``RuleFunction`` extends ``Rule`` and allows multiple parameters
    to have their own validation rules.

    Args:
        **rules:
            Named rules where each key represents a function parameter
            and each value represents the rule that must be satisfied.

    Example:
        >>> rule = RuleFunction(
        ...     age="<18",
        ...     name="Davi"
        ... )
    """

    def __init__(self, **rules):
        super().__init__(**rules)


def ruledfunction(rule):
    """
    Decorator that validates function parameters before execution.

    The decorator receives a ``RuleFunction`` containing the rules
    that should be applied to the decorated function.

    Args:
        rule:
            A ``RuleFunction`` containing the parameter rules.

    Returns:
        function:
            A decorated function that validates its parameters
            before executing the original function.

    Raises:
        ParameterNotProvidedError:
            If a parameter required by the rule was not provided.

        RuleNotSatisfiedError:
            If a provided parameter does not satisfy its rule.

    Example:
        >>> rule = RuleFunction(age="<18")
        >>>
        >>> @ruledfunction(rule)
        ... def hello(age):
        ...     print(f"Hello! You are {age} years old.")
        >>>
        >>> hello(15)
        Hello! You are 15 years old.

        Calling the function with an invalid value:

        >>> hello(20)
        Traceback (most recent call last):
            ...
        RuleNotSatisfiedError: The rule for "age" was not satisfied.
    """

    def wrapper(func):
        parameters = inspect.signature(func).parameters

        @wraps(func)
        def execute(*args, **kwargs):
            values = dict(zip(parameters, args))
            values.update(kwargs)

            for name, rule_value in rule.rules.items():

                if name not in values:
                    raise ParameterNotProvidedError(
                        f'\033[91mThe parameter "{name}" was not provided.\033[0m'
                    )

                value = values[name]

                if isinstance(rule_value, str) and rule_value.startswith("<"):
                    limit = int(rule_value[1:])

                    if not value < limit:
                        raise RuleNotSatisfiedError(
                            f'\033[91mThe rule for "{name}" was not satisfied.\033[0m'
                        )

                elif isinstance(rule_value, str) and rule_value.startswith(">"):
                    limit = int(rule_value[1:])

                    if not value > limit:
                        raise RuleNotSatisfiedError(
                            f'\033[91mThe rule for "{name}" was not satisfied.\033[0m'
                        )

                else:
                    if value != rule_value:
                        raise RuleNotSatisfiedError(
                            f'\033[91mThe rule for "{name}" was not satisfied.\033[0m'
                        )

            return func(*args, **kwargs)

        return execute

    return wrapper