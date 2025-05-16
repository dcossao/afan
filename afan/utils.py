from typing import Callable

import pandas as pd


def predict(df: pd.DataFrame, predictor: Callable, entity: str):
    """
    Apply a predictor function to a DataFrame's text column and extract entity predictions.
    This function takes a DataFrame containing text data, applies a prediction function
    to each text entry, and extracts the specified entity type from the predictions.
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing a 'text' column to make predictions on
    predictor : Callable
        Function that takes text input and returns an object with entity attributes
    entity : str
        Name of the entity attribute to extract from the predictor's output
    Returns
    -------
    pd.DataFrame
        Copy of input DataFrame with an additional 'predicted_entity' column containing
        the extracted entity predictions
    Example usage:
    """

    df_copy = df.copy()

    df_copy["predicted_entity"] = df_copy.text.apply(
        lambda text: getattr(predictor(text=text), entity)
    )

    return df_copy


def judge(df: pd.DataFrame, judge_match: Callable) -> pd.DataFrame:

    df["judge_match"] = df.apply(
        lambda row: judge_match(golds=row.entities, pred=row.predicted_entity).match,
        axis=1,
    )

    accuracy = df["judge_match"].sum() / df.shape[0] * 100

    print(f"Accuracy: {accuracy:.2f}%")

    return df
