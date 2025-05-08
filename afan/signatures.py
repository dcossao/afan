import dspy


class BasicHeroSignature(dspy.Signature):

    __doc__ = """Does the text suggest that some entity could alleviate 
    the problem?"""  # IF so, extract it?

    text = dspy.InputField()
    entity = dspy.OutputField(desc="Often between 1-5 words")


## TODO:
# # if the text suggests that some entity could alleviate the problem, extract it.
# Otherwise say "not applicable"
