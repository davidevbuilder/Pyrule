from pyrule import RuleFunction, ruledfunction


def test_rule_function():
    rule = RuleFunction(age=">18")

    @ruledfunction(rule)
    def hello(age):
        return f"Hello {age}"

    assert hello(20) == "Hello 20"