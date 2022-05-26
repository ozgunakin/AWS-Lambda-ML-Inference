from main import lambda_handler
import json

#LOCAL TEST SCENARIO
# Opening JSON file
f = open('data.json')
sample_event = json.load(f)


if __name__ == "__main__":
    print(lambda_handler(sample_event, context=None))