Housing Webapp
===

This is a super simple Flask app that loads a pre trained model and responds
to requests at an endpoint with how much it thinks a house should cost.

## Usage

1. Run `housing_regression.py` to create a model. It will save the model as a pickle
called `housing_model.pkl`.

2. Run `server.py` and navigate to `localhost:5000`

3. Run `housing_regression.py --force` and wait like 15 minutes as we try to 
brute force optimize our model (we haven't talked about why this is actually a false
positive result, but hey, maybe next semester)

4. Restart `server.py` and it will load the new model.

