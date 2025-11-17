# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint

from source.expansion import MaschineExpansion
from source.modes import EMode
from source.utils import get_expansions_from_path, export_wav_samples

_VERSION = "0.2.0"


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
    parser.add_argument("-m", "--mode", type=str, choices=[mode.value for mode in EMode],
                        help="export WAVs to folders representing Maschine Groups rather than sample types")
    parser.add_argument("-d", "--destructive", action="store_true",
                        help="move original WAV files rather than creating new copies - USE WITH CAUTION")

    args = parser.parse_args()

    if args.input is None or args.input == "":
        print("Search path not specified. Example: 'maschinery -p \"D:/NativeInstruments/Content/\"'")
        return -1

    mode = EMode.from_str(args.mode)

    if mode is None:
        print(f"Invalid export mode specified: \"{args.mode}\".")
        return -1

    print(f"Input Path: {args.input}")
    print(f"Output Path: {args.output}")
    print(f"Export Mode: {args.mode}")

    print("\nProcessing input paths. This may take a minute...")

    expansions: list[MaschineExpansion] = sorted(get_expansions_from_path(args.input))

    print(f"\nLocated a total of {len(expansions)} expansions:")
    pprint(expansions)

    print("\nExporting samples. This may take a minute...")

    args.output = Path(args.output) / "Maschinery"
    args.output.mkdir(parents=True, exist_ok=True)

    export_wav_samples(expansions, args.output, args.mode, args.destructive)

    print(f"\n{args.mode} have been exported to \"{args.output}\".")

    print("\nDone!")

    return 0


if __name__ == "__main__":
    main()
