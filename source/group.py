# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from typing import Literal

from source.base import MaschineObject
from source.sample import MaschineSample


class MaschineGroup(MaschineObject):
    """Data representation of a Maschine Group (MXGRP file)."""

    def __init__(self, path: Path | str, samples: set[MaschineSample] = None):
        """
        Initialization.
        :param path: The path to this group's file.
        :param samples: The WAV files referenced by this group.
        """
        assert path.is_file()
        super().__init__(path)
        self.samples = set[MaschineSample](samples) if samples is not None else set[MaschineSample]()

    def __str__(self) -> str:
        """:return: The string representation of this Maschine object."""
        return self.name

    def __repr__(self) -> str:
        """:return: The string representation of this Maschine object."""
        return str(self)

    @property
    def name(self) -> str:
        """:return: The name of this Maschine object."""
        return self.path.stem

    @staticmethod
    def get_file_format() -> Literal["mxgrp"]:
        """:return: The format of the Maschine Group (MXGRP file). """
        return "mxgrp"
