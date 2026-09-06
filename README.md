![PyRule Logo](https://davidevbuilder.github.io/portifolio/images/pyrule.png)

# PyRule

**PyRule** is a Python library designed to simplify the verification of conditions, parameters, and types through a flexible and intuitive rule-based system.

The main goal of PyRule is to make repetitive validations easier to write, read, maintain, and understand by providing a simple API for creating rules and checking whether values comply with them.

## Installation

Install PyRule using pip:

```bash
pip install py-rule-lib
```

Then import PyRule into your Python project:

```python
import pyrule
```

## Features

- Create reusable rules for values and parameters
- Verify whether values satisfy defined rules
- Validate function parameters using decorators
- Support for custom rule objects
- Object-oriented rule system
- Type validation
- Collection validation
- String validation
- Length validation
- Logical rule composition with `And` and `Or`
- `RuleList` for rule-based list validation
- `RuleDict` for rule-based dictionary validation
- Specific exceptions for validation failures
- Simple and readable syntax
- Designed to be extensible with new rule types
- Python-native implementation with minimal complexity

## Basic Example

```python
from pyrule import Rule, RuleValue, In

rule = Rule(
    name=In(["davi", "ricardo"])
)

value = RuleValue("davi")

if value.check_rule(rule.rules["name"]):
    print("The value follows the rule!")
```

## Comparisons

PyRule provides several built-in comparison rules.

### `Equals`

```python
from pyrule import Rule, RuleValue, Equals

rule = Rule(
    name=Equals("davi")
)

if RuleValue("davi").check_rule(rule.rules["name"]):
    print("The value is equal!")
```

### `NotEquals`

```python
from pyrule import Rule, RuleValue, NotEquals

rule = Rule(
    name=NotEquals("davi")
)

if RuleValue("ricardo").check_rule(rule.rules["name"]):
    print("The value is different!")
```

### `GreaterThan`

```python
from pyrule import Rule, RuleValue, GreaterThan

rule = Rule(
    age=GreaterThan(18)
)

if RuleValue(20).check_rule(rule.rules["age"]):
    print("The value is greater than 18!")
```

### `SmallerThan`

```python
from pyrule import Rule, RuleValue, SmallerThan

rule = Rule(
    age=SmallerThan(18)
)

if RuleValue(15).check_rule(rule.rules["age"]):
    print("The value is smaller than 18!")
```

### `GreaterThanOrEqual`

```python
from pyrule import Rule, RuleValue, GreaterThanOrEqual

rule = Rule(
    age=GreaterThanOrEqual(18)
)

if RuleValue(18).check_rule(rule.rules["age"]):
    print("The value is greater than or equal to 18!")
```

### `SmallerThanOrEqual`

```python
from pyrule import Rule, RuleValue, SmallerThanOrEqual

rule = Rule(
    age=SmallerThanOrEqual(18)
)

if RuleValue(18).check_rule(rule.rules["age"]):
    print("The value is smaller than or equal to 18!")
```

### `In`

The `In` rule checks whether a value exists inside a structure.

```python
from pyrule import Rule, RuleValue, In

rule = Rule(
    name=In(["davi", "ricardo"])
)

if RuleValue("davi").check_rule(rule.rules["name"]):
    print("The value is in the structure!")
```

## Type Rules

PyRule also provides rules for checking value types.

### `Is`

```python
from pyrule import Rule, RuleValue, Is

rule = Rule(
    value=Is(int)
)

if RuleValue(10).check_rule(rule.rules["value"]):
    print("The value is an integer!")
```

### `IsNot`

```python
from pyrule import Rule, RuleValue, IsNot

rule = Rule(
    value=IsNot(str)
)

if RuleValue(10).check_rule(rule.rules["value"]):
    print("The value is not a string!")
```

## String Rules

PyRule includes rules for checking string content.

### `StartsWith`

```python
from pyrule import Rule, RuleValue, StartsWith

rule = Rule(
    name=StartsWith("Da")
)

if RuleValue("Davi").check_rule(rule.rules["name"]):
    print("The value starts with 'Da'!")
```

### `EndsWith`

```python
from pyrule import Rule, RuleValue, EndsWith

rule = Rule(
    name=EndsWith("vi")
)

if RuleValue("Davi").check_rule(rule.rules["name"]):
    print("The value ends with 'vi'!")
```

### `Contains`

```python
from pyrule import Rule, RuleValue, Contains

rule = Rule(
    name=Contains("av")
)

if RuleValue("Davi").check_rule(rule.rules["name"]):
    print("The value contains 'av'!")
```

## Length

The `Length` rule allows you to define minimum and maximum lengths.

```python
from pyrule import Rule, RuleValue, Length

rule = Rule(
    username=Length(3, 20)
)

if RuleValue("Davi").check_rule(rule.rules["username"]):
    print("The username has a valid length!")
```

## Logical Rules

PyRule supports combining multiple rules using `And` and `Or`.

### `And`

All rules must be satisfied.

```python
from pyrule import Rule, RuleValue
from pyrule import And, GreaterThan, SmallerThan

rule = Rule(
    age=(
        And(
            GreaterThan(18),
            SmallerThan(60)
        ),
    )
)

if RuleValue(25).check_rule(rule.rules["age"]):
    print("All rules were satisfied!")
```

### `Or`

At least one rule must be satisfied.

```python
from pyrule import Rule, RuleValue
from pyrule import Or, Equals, In

rule = Rule(
    name=(
        Or(
            Equals("davi"),
            In(["ricardo", "pedro"])
        ),
    )
)

if RuleValue("davi").check_rule(rule.rules["name"]):
    print("At least one rule was satisfied!")
```

## Rule Functions

PyRule provides a way to apply rules directly to function parameters using decorators.

```python
from pyrule import RuleFunction, ruledfunction

rule = RuleFunction(
    age="<18"
)

@ruledfunction(rule)
def hello(age: int):
    print(f"Hello! You are {age} years old.")

hello(13)
```

Before the function is executed, PyRule checks whether the provided parameters satisfy the configured rules.

This allows validation to happen automatically without repeatedly writing conditional statements inside the function.

## RuleList

`RuleList` allows values to be added to a list while checking them against configured rules.

```python
from pyrule import RuleList, GreaterThan

numbers = []

rules = (
    GreaterThan(10),
)

numbers = RuleList(numbers, rules)

numbers.append(20)

print(numbers)
```

## RuleDict

`RuleDict` provides similar functionality for dictionaries.

```python
from pyrule import RuleDict, GreaterThan

data = {}

rules = (
    GreaterThan(10),
)

data = RuleDict(data, rules)

data.append("age", 20)

print(data)
```

## Rule System

PyRule is designed around the concept of rules as objects.

For example:

```python
Rule(
    name=In(["davi", "ricardo"])
)
```

Instead of manually writing repetitive conditions such as:

```python
if name == "davi" or name == "ricardo":
    ...
```

the condition can be represented as a reusable rule.

This architecture allows rules to be stored, reused, combined, and extended.

## Available Rules

PyRule currently provides the following built-in rules.

### Comparison Rules

- `Equals(...)`
- `NotEquals(...)`
- `GreaterThan(...)`
- `SmallerThan(...)`
- `GreaterThanOrEqual(...)`
- `SmallerThanOrEqual(...)`
- `In(...)`

### Type Rules

- `Is(...)`
- `IsNot(...)`

### String Rules

- `StartsWith(...)`
- `EndsWith(...)`
- `Contains(...)`

### Utility and Logical Rules

- `Length(...)`
- `And(...)`
- `Or(...)`

## Exceptions

PyRule provides specific exceptions for different validation failures.

- `RuleNotSatisfiedError` — raised when a value does not satisfy its configured rule.
- `ParameterNotProvidedError` — raised when a parameter required by a rule was not provided.
- `ValueIsNotInRule` — raised when a value does not comply with a rule during rule checking.

### Example

```python
from pyrule import Rule, RuleValue, In
from pyrule import ValueIsNotInRule

rule = Rule(
    name=In(["davi", "ricardo"])
)

try:
    RuleValue("lucas").check_rule(
        rule.rules["name"]
    )

except ValueIsNotInRule:
    print("The value does not satisfy the rule.")
```

## Extensibility

One of the main goals of PyRule is to provide an extensible rule system.

New rule types can be added without requiring the entire validation system to be rewritten.

The rule system is continuously being developed as PyRule evolves.

## Project Structure

```text
pyrule/
├── pyrule/
│   ├── __init__.py
│   ├── rules.py
│   ├── rule_comparations.py
│   ├── rule_types.py
│   ├── rule_utils.py
│   ├── rule_functions.py
│   └── rules_exeptions.py
│
├── tests/
│   ├── __init__.py
│   ├── test_rules.py
│   ├── test_rule_functions.py
│   ├── test_comparations.py
│   └── test_rule_types.py
│
├── examples/
│   ├── basic_rules.py
│   ├── comparisons.py
│   ├── rule_function.py
│   ├── rule_list.py
│   └── rule_dict.py
│
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

## Tests

PyRule includes automated tests to help ensure that the rule system works correctly.

The tests are located in the `tests/` directory.

Current tests cover:

- Basic rules
- Comparisons
- Type rules
- Rule functions

## Examples

The `examples/` directory contains practical examples showing how PyRule can be used.

Examples include:

- Basic rules
- Comparisons
- Rule functions
- Rule lists
- Rule dictionaries

## Project Status

PyRule is currently under active development.

The API and internal architecture may change between versions while the project is being developed.

Current version:

**0.3.0**

## Purpose

PyRule was created to make conditional validation more organized and expressive in Python projects.

Instead of repeatedly writing complex conditional statements, developers can define reusable rules and apply them wherever they are needed.

The project focuses on:

- Readability
- Simplicity
- Reusability
- Extensibility
- Maintainability

## Future Goals

Some planned improvements include:

- More built-in rule types
- Improved type validation
- More comparison operators
- Better error messages
- Expanded `RuleFunction` functionality
- More automated tests
- Complete API documentation
- Improved rule composition
- Performance improvements
- More advanced custom rule support

## License

PyRule is an open-source project. See the `LICENSE` file for the terms and conditions of using, modifying, and distributing the project.

---

**PyRule — Make your conditions become rules.**