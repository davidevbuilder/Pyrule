from pyrule import Rule, RuleValue, Equals


name_rule = Rule(
    name=Equals("Davi")
)

value = "Davi"

if RuleValue(value).check_rule(name_rule.rules["name"]):
    print("The name is valid!")