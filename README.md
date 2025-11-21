# Python Flet Project

This is a basic Python Flet application managed with `uv`.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) installed.

## Installation

1. Clone the repository.
2. Sync dependencies:

```bash
uv sync
```

### Install from requirements.txt

If you have a `requirements.txt` file:

```bash
uv pip install -r requirements.txt
```

## Running the App

To run the application:

```bash
uv run src/main.py
```

## Managing Dependencies

### Add a package

```bash
uv add <package_name>
```

### Remove a package

```bash
uv remove <package_name>
```

### Export requirements.txt

```bash
uv export --format requirements-txt --output-file requirements.txt
```