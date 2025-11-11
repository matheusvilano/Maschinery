# Maschinery

Maschinery is a pure Python console application for organizing Maschine Expansions in a way that is more accessible to third-party *samplers* and *drum machines*. Note that Maschinery will *not* generate files in proprietary formats (e.g. `.bwpreset`); instead, it really will simply organize the WAV files in your Maschine Expansions.

## Compatibility

### Operational Systems

This project targets Windows, macOS, and Linux.

### Maschine Expansions

Only official Maschine Expansions from Native Instruments have been verified. Third-party expansions should work too, as long as they follow the exact same format as the official expansions.

### DAWs, Samplers, and Drum Machines

The organized WAV files are still regular audio files. Maschinery's processes are non-destructive and their sole purpose is to make your Maschine Expansions easier to navigate and import into tools other than Maschine.

## Usage

### Python 3

Running Maschinery in Python 3 directly is preferred if you are not comfortable using pre-built binaries. To do so, first make sure you have Python 3 installed – preferably version 3.13, as that was used for development and confirmed to work. Then, download or clone this repository and run `main.py`. To see usage details, run `main.py -h` or `main.py --help`.

### Binaries

Binaries are provided as a convenience. A Python 3 installation is not required in this case. After downloading the binaries from the Releases page, extract them. Then, open a console/terminal instance and navigate to the new folder. To see usage details, run `maschinery -h` or `maschinery --help`.

## Features

Currently, Maschinery supports these modes:

- Libraries (default): WAV files are organized per Expansion and per sound categories (e.g. "D:/SoundLibs/Maschinery/Crate Cuts/Drums/Kick/Kick April Showers.wav").
- Groups: WAV files are organized per Expansion and per Group (e.g. "D:/SoundLibs/Maschinery/Crate Cuts/April Showers/Kick April Showers.wav").

Maschinery is also *planning* to support the following modes:

- Kits: Similarly to the Groups mode, WAV files are organized per Expansion and per Group, but files are enumerated based on an order chosen by the user. This format is supported for batch-imports in the most popular samplers and drum machines.

## Examples

A couple of examples of running Maschinery:

- Export with Libraries mode: `maschinery -i "D:/SoundLibs/NativeInstruments" -o "D:/SoundLibs/Maschinery"`
- Export with Groups mode: `maschinery` -i "D:/SoundLibs/NativeInstruments" -o "D:/DrumKits/Maschinery" -g`
