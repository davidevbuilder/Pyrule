from pyrule import RuleDict, GreaterThan


data = {}

rules = (
    GreaterThan(10),
)

data = RuleDict(data, rules)

data.append("age", 20)

print(data)