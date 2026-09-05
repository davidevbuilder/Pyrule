class RuleNotSatisfiedError(Exception):
    """
    Exception thrown when a parameter does not meet the rule.
    Correct:
        rule = RuleFunction(
            name='davi',
            age='<18'

        def hello(name:str, age: int):
            print(name, age)
        hello('davi', 13)

    Incorrect:
        rule = RuleFunction(
            name='davi',
            age='<18'

        def hello(name:str, age: int):
            print(name, age)
        hello('davi', 19)
    """
    pass

class ParameterNotProvidedError(Exception):
    """
    Exception raised when a parameter required by a rule
    was not provided when calling the function.
    Correct:
        rule = RuleFunction(
            name='davi',
            age=18

        def hello(name:str, age: int):
            print(name, age)

    Incorrect:
        rule = Rule(
            name='davi',
        )

        def hello(name:str, age: int):
            print(name, age)
    """
    pass

class ValueIsNotInRule(Exception):
    """
    Exception raised when the analyzed value does not satisfy the rule.

    This exception is raised by `check_rule()` when the provided value
    does not comply with the specified rule.

    Example:
        rule = Rule(name="Davi")

        RuleValue("Lucas").check_rule(rule.rules["name"])
    """
    pass