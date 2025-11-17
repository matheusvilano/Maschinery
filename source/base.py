# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from typing import Self


class MaschineObject:
    """Base class for Maschine objects (e.g. groups, expansions, etc)."""

    def __init__(self, path: Path | str):
        """
        Initialization.
        :param path: The path to this group's file.
        """
        assert path.exists()
        self.path = Path(path)

    def __hash__(self) -> int:
        """:return: The hash of this Maschine object, based on its name."""
        return hash(self.name)

    def __eq__(self, other: Self) -> bool:
        """
        Determine equality between two Maschine object instances. Two objects are considered equal if their names
        match case-insensitively.
        :param other: The object to compare against.
        :return: True if both are Maschine objects with the same name, False otherwise.
        """
        if not isinstance(other, MaschineObject):
            return NotImplemented
        return self.name.lower() == other.name.lower()

    def __lt__(self, other: Self) -> bool:
        """
        Compare two Maschine Group instances for sorting. Groups are ordered alphabetically by their lowercase
        name.
        :param other: Another Maschine Group instance.
        :return: True if this group's name is lexicographically smaller than the other's, False otherwise.
        """
        return self.name.lower() < getattr(other.name, "lower")()

    @property
    def name(self) -> str:
        """:return: The name of the object."""
        return self.path.name.rstrip(" Library")

    @property
    def stem(self) -> str:
        """:return: The stem of the object. For certain types, this will be the same as the name."""
        return self.path.stem
