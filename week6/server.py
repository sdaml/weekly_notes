from flask import Flask
import pickle

app = Flask(__name__)
with open('housing_model.pkl', 'r') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return app.send_static_file('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)