#!/usr/bin/python3
"""Defines class Myint"""


class MyInt(int):
    """Inherits from built-in Int"""

    def __eq__(self, other):
        """Override the equality operator ==."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override the in-equality operator !=."""
        return not super().__ne__(other)
