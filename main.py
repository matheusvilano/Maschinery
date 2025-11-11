# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint

from source.expansion import MaschineExpansion
from source.utils import get_expansions_from_path, export_wav_samples

_VERSION = "0.1.0"


def main() -> int:
    """
    Build sample kits from Maschine Groups (MXGRP files).
    :return: Error code, if any. Otherwise, 0.
    """
    print(f"Maschinery (v{_VERSION})\n")

    parser = ArgumentParser()

    parser.add_argument("-i", "--input", required=True, type=str,
                        help="set path to dir containing Maschine Expansions (e.g. \"Crate Cuts Library\")")
    parser.add_argument("-o", "--output", required=True, type=str,
                        help="set output path (where to create a \"Maschinery\" folder with the WAV exports inside)")
    parser.add_argument("-k", "--kits", action="store_true",
                        help="export WAVs in folders representing Maschine Groups rather than sample type (e.g. Kick) ")
    parser.add_argument("-m", "--move", action="store_true",
                        help="export WAVs in folders representing Maschine Groups rather than sample type (e.g. Kick) ")

    args = parser.parse_args()

    if args.input is None or args.input == "":
        print("Search path not specified. Example: 'maschinery -p \"D:/NativeInstruments/Content/\"'")
        return -1

    print(f"Input Path: {args.input}")
    print(f"Output Path: {args.output}")
    print(f"Export Mode: {"Library" if args.kits is False else "Kits"}")

    print("\nProcessing input paths. This may take a minute...")

    expansions: list[MaschineExpansion] = sorted(get_expansions_from_path(args.input))

    print(f"\nLocated a total of {len(expansions)} expansions:")
    pprint(expansions)

    print("\nExporting samples. This may take a minute...")

    args.output = Path(args.output) / "Maschinery"
    args.output.mkdir(parents=True, exist_ok=True)

    export_wav_samples(expansions, args.output, args.kits, args.move)

    print("\nDone!")

    return 0


if __name__ == "__main__":
    main()
