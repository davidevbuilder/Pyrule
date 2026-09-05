"""
PYRULE 0.2.0

Rule Functions:
PyRule allows you to create rules for function parameters
and automatically check those rules before executing a function.

Creating rules for a function:
* function_rules = RuleFunction(parameter=rule)

Example:
* age_rule = RuleFunction(age="<18")

Using a rule function:
* @ruledfunction(rule)

Example:
* @ruledfunction(RuleFunction(age="<18"))
  def hello(age):
      print(f"Hello! You are {age} years old.")

When the function is called, PyRule checks the parameters
against the defined rules before executing the function.

Example:
* hello(15)
  -> The rule is satisfied, so the function executes.

* hello(20)
  -> The rule is not satisfied, so the function does not execute.

Rule Functions are useful for validating function parameters
and avoiding repetitive conditions inside your functions.

The main idea is to make parameter validation simpler,
more readable, and easier to maintain.
"""

import inspect
from .rules import Rule
from .rules_exeptions import (
    RuleNotSatisfiedError,
    ParameterNotProvidedError
)
from functools import wraps


class RuleFunction(Rule):
    """
    A class for a rule that can only be used with functions; it groups multiple parameter checks into a single rule.
    Args:
        **rules: a set of rules passed to the main rule; these only apply to parameter validation.
    Example:
        rule = RuleFunction(
            age='<18'
        )
    """
    def __init__(self, **rules):
        super().__init__(**rules)

def ruledfunction(rule):
    """
    Decorator that checks whether the function received parameters that meet the rule.
    Args:
        rule: Rule to be analyzed.
    Returns:
        Function: The decorated function with rule validation.
    """
    def wrapper(func):
        parameters = inspect.signature(func).parameters
        print(parameters)

        @wraps(func)
        def execute(*args, **kwargs): #pega os args e kwrags
            print(args)
            values = dict(zip(parameters, args)) #associa o valor com o nome do parametro
            print(values)
            values.update(kwargs) #adiciona os kwrags que não são tuplas, não precisa de dict nem zip
            print(values)

            for name, rule_value in rule.rules.items(): #name=key rule_value = valueb {key; value} or {name: rule_value}

                if name not in values:
                    raise ParameterNotProvidedError(f'\033[91mThe parameter "{name}" was not provided.\033[0m')

                value = values[name]

                if isinstance(rule_value, str) and rule_value.startswith("<"):
                    limit = int(rule_value[1:])

                    if not value < limit:
                        raise RuleNotSatisfiedError(f'\033[91mThe rule for "{name}" was not satisfied.\033[0m')

                elif isinstance(rule_value, str) and rule_value.startswith(">"):
                    limit = int(rule_value[1:])

                    if not value > limit:
                        raise RuleNotSatisfiedError(f'\033[91mThe rule for "{name}" was not satisfied.\033[0m')

                else:
                    if value != rule_value: #argument value != rule_value
                        raise RuleNotSatisfiedError(f'\033[91mThe rule for "{name}" was not satisfied.\033[0m')

            return func(*args, **kwargs)

        return execute

    return wrapper