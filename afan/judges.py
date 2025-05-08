import dspy


class EntitiesMatch(dspy.Signature):
    """Determine if the predicted entity is semantically equal to at least one 
    of the gold entities."""

    golds: list[str] = dspy.InputField()
    pred: str = dspy.InputField()

    match: bool = dspy.OutputField()


judge_says_match = dspy.Predict(EntitiesMatch)
