# /// script
# requires-python = ">=3.13"
# dependencies = ["pandas", "requests", "lxml"]
# ///


from io import StringIO
import requests
import pandas as pd

url = "https://docs.astral.sh/ruff/rules/"
result_file = "ruff_rules.csv"


def derive_parent_group(df: pd.DataFrame) -> pd.DataFrame:
    """Derive the Parent_Group column from the Code column."""
    return df.assign(Parent_Group=lambda df: df["Code"].str.extract(r"([A-Z_]+)")[0])


def scrape_rules() -> pd.DataFrame:
    """Scrape the rules from the ruff documentation page and save to a CSV file."""
    response = requests.get(url)
    response.raise_for_status()

    html_content = response.text
    tables = pd.read_html(StringIO(html_content))

    return pd.concat(tables, ignore_index=True)


def scrape_process_and_save_rules() -> None:
    """Scrape the rules and save to a CSV file."""
    (
        scrape_rules()
        .rename(columns={"Unnamed: 3": "Details"})
        .pipe(derive_parent_group)
        .to_csv(
            result_file,
            index=False,
        )
    )


if __name__ == "__main__":
    scrape_process_and_save_rules()
