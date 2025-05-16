import dspy


class EntitiesMatchFewShot(dspy.Signature):
    """Determine if the predicted entity is similar
      in meaning to at least one of the gold entities.


    ######################
    -Examples-
    ######################
    Example 1:

    [[ ## golds ## ]]
    ["Offshore drilling safety regulations"]

    [[ ## pred ## ]]
    'Environmental safety regulations and advocates for responsible drilling practices'

    [[ ## match ## ]]
    True

    [[ ## completed ## ]]
    ######################
    Example 2:

    [[ ## golds ## ]]
    [Community protest, the local press]

    [[ ## pred ## ]]
    'The local community and concerned citizens who actively protested against the plant.'

    [[ ## match ## ]]
    True

    [[ ## completed ## ]]
    ######################
    Example 3:

    [[ ## golds ## ]]
    [California lawsuit]

    [[ ## pred ## ]]
    'California and the coalition of states fighting for environmental protection.'

    [[ ## match ## ]]
    True

    [[ ## completed ## ]]
    ######################
    Example 4:

    [[ ## golds ## ]]
    [Julian Castro's Climate Plan]

    [[ ## pred ## ]]
    'Julian Castro'

    [[ ## match ## ]]
    True
    [[ ## completed ## ]]

    ######################
    Example 5:

    [[ ## golds ## ]]
    [Green New Deal]

    [[ ## pred ## ]]
    'Rep. Alexandria Ocasio-Cortez'

    [[ ## match ## ]]
    False

    [[ ## completed ## ]]

    ######################
    Example 6:

    [[ ## golds ## ]]
    [Political leaders]

    [[ ## pred ## ]]
    'Justin Trudeau'

    [[ ## match ## ]]
    False

    [[ ## completed ## ]]

    ######################
    Example 7:

    [[ ## golds ## ]]
    [some ordinary Americans, climate action]

    [[ ## pred ## ]]
    'Peter Kalmus, as a climate scientist and advocate for personal action against climate change'

    [[ ## match ## ]]
    False

    [[ ## completed ## ]]

    """

    golds: list[str] = dspy.InputField()
    pred: str = dspy.InputField()

    match: bool = dspy.OutputField()


class EntitiesMatch(dspy.Signature):
    """Determine if the predicted entity is semantically equal to at least one
    of the gold entities"""

    golds: list[str] = dspy.InputField()
    pred: str = dspy.InputField()

    match: bool = dspy.OutputField()
