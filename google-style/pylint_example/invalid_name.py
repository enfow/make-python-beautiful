"""Exmaple for pylint."""

constant = 0

class this_is_snake_case:
    """Class docstring."""

    def thisISCamelCase():
        """Method docstring."""
        return 0
"""
# Result of `pylint invalid_name.py`

************* Module invalid_name
invalid_name.py:3:0: C0103: Constant name "constant" doesn't conform to UPPER_CASE naming style (invalid-name)
invalid_name.py:5:0: C0103: Class name "this_is_snake_case" doesn't conform to PascalCase naming style (invalid-name)
invalid_name.py:8:4: C0103: Method name "thisISCamelCase" doesn't conform to snake_case naming style (invalid-name)
invalid_name.py:8:4: E0211: Method has no argument (no-method-argument)
invalid_name.py:8:4: R0201: Method could be a function (no-self-use)
invalid_name.py:5:0: R0903: Too few public methods (1/2) (too-few-public-methods)
"""
