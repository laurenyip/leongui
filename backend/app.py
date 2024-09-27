from flask import Flask, jsonify
from scraper import scrape_articles

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = 'https://laurenyip.com'  # Replace with the actual URL you want to scrape
    articles = scrape_articles(url)
    return jsonify(articles)  # Return the scraped articles as JSON

if __name__ == "__main__":
    app.run(debug=True)
