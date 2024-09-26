from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from scraping import scrape_articles


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/scrape', methods=['GET'])
def scrape():
    url = 'https://laurenyip.com'  # Replace with the actual URL
    titles = scrape_articles(url)
    return jsonify(titles)

if __name__ == "__main__":
    app.run(debug=True)
