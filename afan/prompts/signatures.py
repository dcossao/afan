import dspy


class NarrativeArcSignature(dspy.Signature):

    __doc__ = """Identity narrative arc. Stick to the text"""

    text = dspy.InputField()
    conflict = dspy.OutputField(desc="be concise")
    hero = dspy.OutputField(desc="Not necessarily a person")
    victim = dspy.OutputField(desc="Not necessarily a person")
    villain = dspy.OutputField(desc="Not necessarily a person")


class BasicHeroSignature(dspy.Signature):

    __doc__ = """Does the text suggest that some entity could alleviate 
    a problem?"""

    text = dspy.InputField()
    entity = dspy.OutputField(desc="Often between 1-5 words")
