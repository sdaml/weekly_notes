from flask import Flask, request, render_template
import pickle
import json

app = Flask(__name__)

model = None
with open('housing_model.pkl', 'r') as f:
    model = pickle.load(f)

metadata = {}
with open('model.meta.json', 'r') as f:
    metadata = json.load(f)


@app.route('/')
def index():
    return render_template('index.html', metadata=metadata)


@app.route('/metadata')
def get_labels():
    return json.dumps(metadata), 200

@app.route('/predict')
def predict_house():
    required_labels = metadata['labels']
    score = metadata['score']
    vector = request.args.getlist('values[]')
    vector = [int(x) for x in vector]
    prediction = model.predict(vector)
    
    if prediction < 50000:
        return "These values clearly aren't correct, this house is worth %.2f" % prediction
    else:
        return "This house is should be worth around $%.2f" % prediction
    
   
if __name__ == "__main__":
    app.run(debug=True)