import os
import pandas as pd


def save_report(results: list, output_path: str) -> None:
    """
    Saves screening results into a CSV file.
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.DataFrame(results)

    df.to_csv(output_path, index=False)

    print(f"\nReport saved successfully at: {output_path}")


def print_top_candidates(results: list, top_n: int = 10) -> None:
    """
    Prints top ranked candidates in terminal.
    """

    if not results:
        print("No results found.")
        return

    df = pd.DataFrame(results)

    columns_to_show = [
        "candidate_name",
        "final_score",
        "decision",
        "experience_years",
        "matched_skills",
        "missing_skills"
    ]

    print(f"\nTop {top_n} Ranked Candidates:")
    print(df[columns_to_show].head(top_n))