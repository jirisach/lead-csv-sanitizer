# Contributing

Thank you for your interest in contributing to **Lead CSV Sanitizer**.

## Development Setup

Clone the repository:

```
git clone https://github.com/jirisach/lead-csv-sanitizer.git
cd lead-csv-sanitizer
```

Create a virtual environment:

```
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

Install dependencies:

```
python -m pip install --upgrade pip
python -m pip install -e .
```

Run tests:

```
pytest
```

## Guidelines

Please follow these principles when contributing:

* Keep the tool deterministic
* Avoid external API dependencies
* Ensure data privacy (no external data transmission)
* Add tests for new features
* Keep the CLI interface simple

## Reporting Issues

If you find a bug or have a feature request, please open an issue.

## Pull Requests

Pull requests are welcome. Please make sure tests pass before submitting.
