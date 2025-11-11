# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from source.base import MaschineObject
from source.group import MaschineGroup
from source.sample import MaschineSample


class MaschineExpansion(MaschineObject):
    """Data representation of a Maschine Expansion (sold by Native Instruments)."""

    def __init__(self, path: Path, groups: list[MaschineGroup] = None):
        """
        Initialization.
        :param path: The path to this Maschine Expansion directory.
        :param groups: The groups containing within this expansion.
        """
        assert path.is_dir()
        super().__init__(path)
        self.groups = set[MaschineGroup](groups) if groups is not None else set[MaschineGroup]()

    def __str__(self) -> str:
        """:return: The string representation of this Maschine Expansion."""
        return f"<Name: {self.name}, Path: {self.path}, Groups: {sorted(self.groups)}>"

    def __repr__(self) -> str:
        """:return: The string representation of this Maschine Expansion."""
        return str(self)

    @property
    def samples(self) -> list[MaschineSample]:
        """:return: All the WAV samples contained in this expansion. Fetched from all groups."""
        return [sample for group in self.groups for sample in group.samples]
