"""
PYRULE 0.2.0

A Python library made to make conditions and rule-based checks in your code easier.
PyRule allows you to create rules and check whether values follow those rules.

Creating a rule:
* variable = Rule(key=value)

Example:
* name_rule = Rule(name="Davi")

Checking if an item follows a rule:
* if RuleValue(var).check_rule(variable_of_rule.rules[key]):

Example:
* if RuleValue("Davi").check_rule(name_rule.rules["name"]):
  print("The value follows the rule!")

Rules can be used to organize conditions and make your code easier
to read, maintain, and understand.
The main idea of PyRule is to make repetitive conditions simpler
and provide an easy way to create and check rules.
"""

from .rules_exeptions import (
    ValueIsNotInRule
)

import inspect

class Rule:
    """
    Class for a simple rule; place multiple checks within a single rule.
    Args:
        **rules: set of rules that will be passed to the main rule.
    Example:
        rule = Rule(
            age=18
        )
    """
    def __init__(self, **rules):
        self.rules = rules

    def __str__(self):
        for k, v in self.rules.items():
            return(f'{k}: {v}')

    def add_value(self, **value):
        return self.rules.update(value)


class RuleValue:
    """
    Converts a value into a rule item that can be analyzed.
    Args:
        value: Amount to be converted.
    Exemple:
        RuleValue('Davi')
    """
    def __init__(self, value):
        self.value = value

    def check_rule(self, rule_item):
        """
        Checks whether the item follows the created rule.
        Args:
            rule_item (Dict Elementy): Element of the main rule to be analyzed.
        Returns:
            True, False or Raise
        Exemple:
            if pyrule.RuleValue(name).check_rule(nome.rules['name']):
        """

        if self.value == rule_item:
            return True

        if isinstance(rule_item, In) and self.value in rule_item.structure:
            return True

        else:
            raise ValueIsNotInRule('\033[91mThe value does not comply with the rule.')

class In:
    def __init__(self, structure):
        self.structure = structure