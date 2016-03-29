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
    print request.args
    return 200
    
   
if __name__ == "__main__":
    app.run(debug=True)