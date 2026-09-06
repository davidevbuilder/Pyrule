from pyrule import (
    Rule,
    RuleValue,
    GreaterThan,
    SmallerThan,
    GreaterThanOrEqual,
    SmallerThanOrEqual
)


def test_greater_than():
    rule = Rule(age=GreaterThan(18))

    assert RuleValue(20).check_rule(rule.rules["age"])


def test_smaller_than():
    rule = Rule(age=SmallerThan(18))

    assert RuleValue(15).check_rule(rule.rules["age"])


def test_greater_than_or_equal():
    rule = Rule(age=GreaterThanOrEqual(18))

    assert RuleValue(18).check_rule(rule.rules["age"])


def test_smaller_than_or_equal():
    rule = Rule(age=SmallerThanOrEqual(18))

    assert RuleValue(18).check_rule(rule.rules["age"])