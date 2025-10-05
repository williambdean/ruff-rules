# Ruff Rules

These are the official [Ruff documentation](https://docs.astral.sh/ruff/rules/) saved as a CSV and JSON file.

## The Flat Files

Each file contains a list of all the Ruff linting rules, with the following columns:

*   **Code:** The rule's identifier code (e.g. `RUF001`).
*   **Name:** The name of the rule.
*   **Message:** A brief description of what the rule checks for.
*   **Details:** Additional details or autofix availability for the rule.
*   **ParentGroup**: The parent category of the rule. (e.g. `RUF` for Ruff rules)

## Access the CSV

Use the raw link to access the CSV file directly. That is: 

```terminal
curl https://raw.githubusercontent.com/williambdean/ruff-rules/refs/heads/main/ruff_rules.csv
```

## Scraping Script

The `scrape_rules.py` script scrapes the rules from the official Ruff documentation.

### How to Use the Script

Run the script with its dependencies using [uv](https://pypi.org/project/uv/):

```terminal
# Run with Makefile
make

# Run script directly
uv run scrape_rules.py
```

