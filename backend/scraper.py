import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all article titles (replace 'article-title' with the actual class or tag)
        titles = soup.find_all(class_='article-title')  # Example class name
        
        # Extract and print the text of each title
        for title in titles:
            print(title.get_text(strip=True))
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace with the URL you want to scrape
    url = 'https://laurenyip.com'  # Replace with the actual URL
    scrape_articles(url)
