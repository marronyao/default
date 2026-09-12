# Random Number Generator

A small Python command-line tool for producing cryptographically secure random
integers. Values are unbiased and include both ends of the supplied range.

## Requirements

Python 3.10 or later. No third-party packages are required.

## Usage

Generate one integer from 1 through 100:

```bash
python3 random_number_generator.py 1 100
```

Generate five integers from -10 through 10:

```bash
python3 random_number_generator.py -10 10 --count 5
```

Use `--help` to view all command-line options.

## Run in Codex Cloud

Open the repository's terminal in Codex Cloud, then run the command from the
repository root:

```bash
cd /workspace/Default
python3 random_number_generator.py 1 100
```

Replace `1` and `100` with the smallest and largest allowed values. To generate
several values, pass `--count`:

```bash
python3 random_number_generator.py -10 10 --count 5
```

To see the available arguments at any time, run:

```bash
python3 random_number_generator.py --help
```
