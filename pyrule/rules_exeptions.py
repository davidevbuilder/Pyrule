"""
PYRULE 0.3.0 - EXCEPTIONS

Custom exceptions used by PyRule to handle errors that may occur
during rule validation and rule-based function execution.

PyRule provides specific exceptions for different situations,
making it easier to identify why a rule validation failed.

Exceptions included in this module:

    - RuleNotSatisfiedError
        Raised when a parameter does not satisfy its defined rule.

    - ParameterNotProvidedError
        Raised when a parameter required by a rule is not provided.

    - ValueIsNotInRule
        Raised when a value does not satisfy the specified rule.

These exceptions allow PyRule to provide clearer and more
specific error handling when working with rules and validations.
"""


class RuleNotSatisfiedError(Exception):
    """
    Exception raised when a parameter does not satisfy the defined rule.

    This exception is raised by RuleFunction when a function parameter
    does not comply with the rule associated with it.

    Example:
        Correct:
            rule = RuleFunction(
                name='davi',
                age='<18'
            )

            def hello(name: str, age: int):
                print(name, age)

            hello('davi', 13)

        Incorrect:
            rule = RuleFunction(
                name='davi',
                age='<18'
            )

            def hello(name: str, age: int):
                print(name, age)

            hello('davi', 19)
    """
    pass


class ParameterNotProvidedError(Exception):
    """
    Exception raised when a parameter required by a rule
    was not provided when calling the function.

    Example:
        Correct:
            rule = RuleFunction(
                name='davi',
                age=18
            )

            def hello(name: str, age: int):
                print(name, age)

            hello('davi', 18)

        Incorrect:
            rule = RuleFunction(
                name='davi',
                age=18
            )

            def hello(name: str, age: int):
                print(name, age)

            hello('davi')
    """
    pass


class ValueIsNotInRule(Exception):
    """
    Exception raised when the analyzed value does not satisfy
    the specified rule.

    This exception is raised by ``check_rule()`` when the provided
    value does not comply with the rule being evaluated.

    Example:
        rule = Rule(name="Davi")

        RuleValue("Lucas").check_rule(rule.rules["name"])
    """
    pass
