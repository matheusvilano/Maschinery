# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from enum import StrEnum
from typing import Self


class EMode(StrEnum):
    """Enum for the different export modes."""

    LIBRARIES = "Libraries"
    """Export samples as regular libraries, with sounds grouped by sample type (e.g. Kick, Snare, Hi-Hat, etc)."""

    GROUPS = "Groups"
    """Export samples as folders representing Maschine Groups rather than sample types (e.g. Kick)."""

    KITS = "Kits"
    """Export samples as import-ready kits, with samples being enumerated from 1 to a maximum of 128."""

    @classmethod
    def from_str(cls, mode_value: str) -> Self | None:
        """
        Get the mode enum from a string.
        :param mode_value: The string value of the mode.
        :return: The mode enum. Will be None if not found.
        """
        for mode in cls:
            if mode.value == mode_value:
                return mode
        return None