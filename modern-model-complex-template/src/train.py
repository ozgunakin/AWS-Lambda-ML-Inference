import pickle
import pandas as pd

class Classifier:
    def __init__(self):
        pass

    def load_and_test(self,data):

        model = pickle.load(open("models/finalized_fl80_model.sav", "rb"))
        prediction = model.predict(pd.DataFrame(dict(data)["data"])).tolist()

        return {"prediction": prediction}

