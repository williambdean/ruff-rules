# Ruff Rules

These are the official [Ruff documentation](https://docs.astral.sh/ruff/rules/) saved as a CSV and JSON file.

> [!TIP]
>
> You can also use `ruff rule --output-format json --all` to get the rules in
> JSON format which might be more up-to-date.

## The Flat Files

Each file contains a list of all the Ruff linting rules, with the following columns:

*   **Code:** The rule's identifier code (e.g. `RUF001`).
*   **Name:** The name of the rule.
*   **Message:** A brief description of what the rule checks for.
*   **Details:** Additional details or autofix availability for the rule.
*   **ParentGroup**: The parent category of the rule. (e.g. `RUF` for Ruff rules)

## Access the Files

Use the raw link github to access the file directly. For example, to download the CSV file:

```terminal
curl -s https://raw.githubusercontent.com/williambdean/ruff-rules/refs/heads/main/ruff_rules.csv
```

Or access the JSON file:

```terminal
curl -s https://raw.githubusercontent.com/williambdean/ruff-rules/refs/heads/main/ruff_rules.json
```

### Example: Filter Rules by Parent Group

Use [jq](https://jqlang.org/) to filter the JSON file by parent group. For example, to get all rules in the `RUF` parent group:

```terminal
curl -s https://raw.githubusercontent.com/williambdean/ruff-rules/refs/heads/main/ruff_rules.json | jq 'map(select(.ParentGroup == "RUF"))'
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

