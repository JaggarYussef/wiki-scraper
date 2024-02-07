#main.py
from src.wiki_scraper import Scraper

scraper = Scraper()
# print(scraper.refresh_cookie())

#Get Countries and respective leaers
listOfCountries = scraper.get_countries()
for country in listOfCountries:
    scraper.get_leaders(country)

#Fill in wiki_excerpt prop
scraper.get_first_paragraph()

#Write Data
filepath = "leaders_data.json"
scraper.to_json_file(filepath)