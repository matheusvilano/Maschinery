# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from source.base import MaschineObject
from source.utils import find_path_case_insensitive


class MaschineSample(MaschineObject):
    """:return: All the paths contained in this sample"""

    def __init__(self, path: Path):
        """
        Initialization.
        :param path: The full system path to the sample.
        """
        if not path.exists():
            path = find_path_case_insensitive(path)
        assert path.is_file()
        super().__init__(path)

    @property
    def subdir(self) -> str:
        """:return: The subdirectory of the sample, which also acts as an identifier."""
        return str(self.path)[str(self.path).find("Samples/"):]
