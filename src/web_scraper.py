import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class WebScraper:
    def __init__(self):
        pass

    def scrape_news_articles(self, url):
        logging.info(f'Scraping news articles from {url}')
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('article')  # Adjust based on website structure
            return [article.text for article in articles]
        except requests.RequestException as e:
            logging.error(f'An error occurred while scraping news articles: {e}')
            return []

    def fetch_data_from_api(self, api_url):
        logging.info(f'Fetching data from API: {api_url}')
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f'An error occurred while fetching data from API: {e}')
            return None

    def scrape_html_tables(self, url):
        logging.info(f'Scraping HTML tables from {url}')
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            tables = soup.find_all('table')
            return [[cell.text for cell in row.find_all(['td', 'th'])] for table in tables for row in table.find_all('tr')]
        except requests.RequestException as e:
            logging.error(f'An error occurred while scraping HTML tables: {e}')
            return []

