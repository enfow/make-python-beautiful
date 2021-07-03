"""Exmaple for pylint."""

# Raises unused-argument warning
def viking_cafe_order_1(spam, beans, eggs=None):
    """viking cafe order."""
    return spam + spam + spam

# Does not raise unused-argument warning: with deleting variable
def viking_cafe_order_2(spam, beans, eggs=None):
    """viking cafe order."""
    del beans, eggs  # Unused by vikings.
    return spam + spam + spam

# Does not raise unused-argument warning: with prefix `_`, `unused_`
def viking_cafe_order_3(spam, unused_beans, _eggs=None):
    """viking cafe order."""
    return spam + spam + spam

"""
# Result of `pylint unused_argument.py`

************* Module unused_argumnet
unused_argumnet.py:4:30: W0613: Unused argument 'beans' (unused-argument)
unused_argumnet.py:4:37: W0613: Unused argument 'eggs' (unused-argument)
"""
