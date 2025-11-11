# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from re import compile as re_compile
from shutil import copy2 as sh_copy, move as sh_move
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from source.expansion import MaschineExpansion


def get_expansions_from_path(search_dir: Path | str) -> list["MaschineExpansion"]:
    """
    Find all Maschine Expansions in a given directory. Done by locating MXGRP files within subdirectories.
    :param search_dir: The directory to search within.
    :return: The Maschine Expansions found, in a list.
    """
    from source.expansion import MaschineExpansion
    from source.group import MaschineGroup
    from source.sample import MaschineSample

    search_dir = Path(search_dir)

    if not search_dir.is_dir():
        return []

    expansions = dict[str, MaschineExpansion]()

    # TODO: the operations below are not optimized - not necessarily a problem, but something to watch out for.

    for mxgrp_file in search_dir.rglob(f"*.{MaschineGroup.get_file_format()}"):  # Find .mxgrp files (recursive)
        for parent_dir in mxgrp_file.parents:  # Add the top-level directory under root that contains the file
            if parent_dir.parent == search_dir:  # Stop once we reach a direct child of the root
                if parent_dir.name not in expansions:
                    expansions[parent_dir.name] = MaschineExpansion(parent_dir)
                group = MaschineGroup(mxgrp_file)
                with open(mxgrp_file, "rb") as mxgrp_io:
                    wav_pattern = re_compile(r"(?i)Samples(?:/[\w\s().,'!&-]+)+/[\w\s().,'!&-]+\.wav")
                    mxgrp_str = mxgrp_io.read().decode("utf-8", errors="ignore")
                    group_samples = [MaschineSample(parent_dir / sample_subdir)
                                     for sample_subdir in wav_pattern.findall(mxgrp_str)]
                    group.samples.update(group_samples)
                expansions[parent_dir.name].groups.add(group)

    return list(expansions.values())


def find_path_case_insensitive(path: Path):
    """
    Return the real path on disk, ignoring case, or None if not found.
    :param path: The path to look for.
    :return: The real path on disk, ignoring case, or None if not found.
    """
    if path.exists():
        return path
    directory = path.parent
    if not directory.exists():
        directory = find_path_case_insensitive(directory)
        if directory.parent is None:
            return directory
    target_name = path.name.lower()
    for f in directory.iterdir():
        if f.name.lower() == target_name:
            return f
    return None


def export_wav_samples(expansions: list["MaschineExpansion"], output: Path, kits: bool = False, move: bool = False):
    """
    Exports all WAV samples associated with the specified Maschine expansions.
    :param expansions: The Maschine Expansions to export WAV samples from.
    :param output: The path where the WAV samples will be exported.
    :param kits: Whether to export WAVs in folders representing Maschine Groups rather than sample type (e.g. Kick).
    :param move: Whether to move the original WAVs rather than copying them.
    """
    if not kits:
        for expansion in expansions:
            for sample in expansion.samples:
                sample_output = output / expansion.name / sample.subdir.replace("Samples/", "")
                sample_output.parent.mkdir(parents=True, exist_ok=True)
                if move:
                    sh_move(sample.path, sample_output)
                else:
                    sh_copy(sample.path, sample_output)
    else:
        for expansion in expansions:
            for group in expansion.groups:
                for sample in group.samples:
                    sample_output = output / expansion.name / group.name / sample.name
                    sample_output.parent.mkdir(parents=True, exist_ok=True)
                    if move:
                        sh_move(sample.path, sample_output)
                    else:
                        sh_copy(sample.path, sample_output)
