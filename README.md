![Logo do PyRule](https://davidevbuilder.github.io/Portifolho-Repositorio/images/pyrule.png)
# PyRule

**PyRule** is a Python library designed to simplify the verification of conditions, parameters, and types through a flexible and intuitive rule-based system.

The main goal of PyRule is to make repetitive validations easier to write, read, maintain, and understand, providing a simple API for creating rules and checking whether values comply with them.

## Features

* Create reusable rules for values and parameters
* Verify whether values satisfy defined rules
* Validate function parameters using decorators
* Support for custom rule objects
* Object-oriented rule system
* Specific exceptions for validation failures
* Simple and readable syntax
* Designed to be extensible with new rule types
* Python-native implementation with minimal complexity

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

## Rule Functions

PyRule also provides a way to apply rules directly to function parameters using decorators.

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

This architecture also allows PyRule to be extended with additional rule types in the future.

## Exceptions

PyRule provides specific exceptions for different validation failures, including:

* `RuleNotSatisfiedError` — raised when a parameter does not satisfy its configured rule.
* `ParameterNotProvidedError` — raised when a parameter required by a rule was not provided.
* `ValueIsNotInRule` — raised when a value does not comply with a rule during rule checking.

Example:

```python
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

For example, the library can be extended with rules for:

```text
In(...)
Equals(...)
GreaterThan(...)
LessThan(...)
Is(...)
...
```

The rule system is continuously being developed as PyRule evolves.

## Project Status

PyRule is currently under active development.

The API and internal architecture may change between versions while the project is being developed.

Current version:

**0.2.0**

## Purpose

PyRule was created to make conditional validation more organized and expressive in Python projects.

Instead of repeatedly writing complex conditional statements, developers can define reusable rules and apply them wherever they are needed.

The project focuses on:

* Readability
* Simplicity
* Reusability
* Extensibility
* Maintainability

## Future Goals

Some planned improvements include:

* More built-in rule types
* Improved type validation
* More comparison operators
* Better error messages
* Expanded `RuleFunction` functionality
* Comprehensive automated tests
* Complete API documentation
* Improved rule composition
* Package distribution through PyPI
* Performance improvements

## Installation

PyRule is currently under development and may not yet be available as a stable PyPI release.

Once published, it will be installable using:

```bash
pip install py-rule
```

## License

PyRule is an open-source project. See the `LICENSE` file for the terms and conditions of using, modifying, and distributing the project.

---

**PyRule — Make your conditions become rules.**
