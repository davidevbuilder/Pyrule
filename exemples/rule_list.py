from pyrule import RuleList, GreaterThan


numbers = []

rules = (
    GreaterThan(10),
)

numbers = RuleList(numbers, rules)

numbers.append(20)

print(numbers)