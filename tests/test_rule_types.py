from pyrule import Rule, RuleValue, Is, IsNot


def test_is():
    rule = Rule(value=Is(int))

    assert RuleValue(10).check_rule(rule.rules["value"])


def test_is_not():
    rule = Rule(value=IsNot(str))

    assert RuleValue(10).check_rule(rule.rules["value"])