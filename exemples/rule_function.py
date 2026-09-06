from pyrule import RuleFunction, ruledfunction


rule = RuleFunction(
    age=">18"
)


@ruledfunction(rule)
def hello(age):
    print(f"You are {age} years old.")


hello(20)