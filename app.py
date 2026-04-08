from flask import Flask, render_template, request
from data_loader import load_data

app = Flask(__name__)

@app.route('/')
def index():
    postcode = request.args.get('postcode', 'L40TH').strip()
    
    restaurants = load_data(postcode)
    
    return render_template('index.html', restaurants=restaurants, postcode=postcode)

if __name__ == "__main__":
    app.run(debug=True)