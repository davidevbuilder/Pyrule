from pyrule import (
    Rule,
    RuleValue,
    GreaterThan,
    SmallerThan,
    GreaterThanOrEqual,
    SmallerThanOrEqual
)


age_rule = Rule(
    age=GreaterThanOrEqual(18)
)

age = 20

if RuleValue(age).check_rule(age_rule.rules["age"]):
    print("Age is valid!")