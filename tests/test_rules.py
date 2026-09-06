from pyrule import Rule, RuleValue
from pyrule import In, Equals, NotEquals


def test_equals():
    rule = Rule(name=Equals("Davi"))

    assert RuleValue("Davi").check_rule(rule.rules["name"])


def test_not_equals():
    rule = Rule(name=NotEquals("Davi"))

    assert RuleValue("John").check_rule(rule.rules["name"])


def test_in():
    rule = Rule(name=In(["Davi", "John", "Peter"]))

    assert RuleValue("Davi").check_rule(rule.rules["name"])