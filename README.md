# Wikipedia Scraper

## Description

This project is a Python application designed to scrape data from Wikipedia regarding the political leaders of various countries. It leverages an external API to obtain a list of countries and their past political leaders, then extracts and sanitizes their short bios from Wikipedia. The scraped data is then saved to a JSON file for further processing.

## Requirements

- Python 3.x
- BeautifulSoup
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JaggarYussef/wiki-scraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd wikipedia-scraper
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the `main.py` script to start the scraping process:
   ```bash
   python main.py
   ```
2. The script will call the API to retrieve a list of countries and their leaders, scrape the Wikipedia pages for the leaders' bios, and save the data to a JSON file named `leaders_data.json` in the project directory.

## Project Structure

- `main.py`: The main script that orchestrates the scraping process.
- `src/`: Directory containing the source code for the Wikipedia scraper.
  - `wiki_scraper.py`: Module containing the `Scraper` class responsible for scraping Wikipedia data.
- `requirements.txt`: File listing the project dependencies.
- `leaders_data.json`: Output JSON file containing the scraped data.
