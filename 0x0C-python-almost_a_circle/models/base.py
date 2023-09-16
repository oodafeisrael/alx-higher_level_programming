#!/usr/bin/python3
"""Defines Base class"""


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0  # Private class attribute to manage object counts

    def __init__(self, id=None):
        """Initialize a Base instance with a unique id or auto-incremented id."""
        if id is not None:
            self.id = id  # Assign id if provided
        else:
            Base.__nb_objects += 1  # Increment the object count
            self.id = Base.__nb_objects  # Assign the new id
