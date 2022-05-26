import pickle
import pandas as pd

def load_and_test(data):

    model = pickle.load(open("models/finalized_fl80_model.sav", "rb"))
    prediction = model.predict(pd.DataFrame(dict(data)["data"])).tolist()

    return {"prediction": prediction}

def lambda_handler(event, context):
    try:
        return load_and_test(event)
    except Exception as e:
        raise