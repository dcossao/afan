import dspy


class ZeroShotPredictor(dspy.Module):
    def __init__(self, signature):
        super().__init__()

        self.predict = dspy.Predict(signature)

    def forward(self, text):
        self.predict(text=text)
