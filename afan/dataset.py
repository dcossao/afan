"""Scripts to load and preprocess datasets."""

import os

import dspy
import pandas as pd


def load_and_preprocess_dataset(
    dataset_name: str, data_dir: str, columns: list[str] = None
) -> pd.DataFrame:
    """
    - Loads the dataset from the specified directory
    - Formats the 'entities' column as a list of entities

    Args:
        dataset_name (str): The name of the dataset to load.
        data_dir (str): The directory where the dataset is located.

    Returns:
        pd.DataFrame: The preprocessed dataset as a pandas DataFrame
    """
    df = load_tsv(dataset_name, data_dir)
    df = format_entities_as_list(df)

    if columns is not None:
        return df[columns].copy()
    return df[["ID", "text", "entities"]].copy()


def load_tsv(dataset_name: str, data_dir: str) -> pd.DataFrame:
    """Load a dataset from the specified directory.

    Args:
        dataset_name (str): The name of the dataset to load.
        data_dir (str): The directory where the dataset is located.

    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame
    """
    # Construct the file path
    file_path = os.path.join(data_dir, f"{dataset_name}.tsv")

    # Load the dataset
    df = pd.read_csv(
        file_path,
        sep="\t",
    )

    return df.copy()


def format_entities_as_list(df: pd.DataFrame) -> pd.DataFrame:
    """Returns a list of entities from the semicolon-separated string in the
    'entities' column.
    Args:
        df (pd.DataFrame): The DataFrame containing the 'entities' column.
    Returns:
        pd.DataFrame: The DataFrame with the 'entities' column processed

    """

    assert "entities" in df.columns, "DataFrame must contain 'entities' column"
    assert "text" in df.columns, "DataFrame must contain 'text' column"

    df["entities"] = (
        df["entities"].str.split(";").apply(lambda x: [item.strip() for item in x])
    )

    return df


def make_examples(df: pd.DataFrame) -> list[dspy.Example]:
    """Turns a dataframe with columns 'text' and 'entities'
    into a list of dspy Examples to be used for optimizing"""

    return [
        dspy.Example(text=row["text"], entities=row["entities"]).with_inputs("text")
        for _, row in df.iterrows()
    ]


def save_tsv(
    df: pd.DataFrame,
    data_dir: str,
    name: str,
    columns: list[str] = None,
) -> None:
    """
    Saves dataframe as tsv.

    Careful saving 'entities' column: format could cause problems"""

    if columns is None:
        columns = ["ID", "predicted_entity", "judge_match"]

    file_name = f"""../data/{data_dir}/{name}.tsv"""

    df[columns].to_csv(file_name, sep="\t", index=False)
