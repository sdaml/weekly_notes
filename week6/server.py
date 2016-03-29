from flask import Flask
import pickle

app = Flask(__name__)
model = pickle.load("housing_model.pkl")

@app.route('/')
def index():
    return "hello world"
    
if __name__ == "__main__":
    app.run(debug=True)