#wiki_scraper.py 

    # def get_first_paragraph(self, wiki_url: str):
    #     response = requests.get(wiki_url).text
    #     print(response)
    #     if response.status_code == 200:
    #         soup = BeautifulSoup(response.content, 'html.parser')
    #         infobox_text = soup.find('div', class_='infobox-below')
    #         return infobox_text
    #     else:
    #         print("Failed to retrieve page:", response.status_code)
    #         return None
                  
from bs4 import BeautifulSoup
import requests
import json

import re

def fix_special_chars(name):
    special_chars = {
        r'\u00e7': 'ç',
        r'\u00e8': 'è',
        r'\u00e9': 'é',
        r'\u00ea': 'ê',
        r'\u00eb': 'ë',

    }
    
    for pattern, replacement in special_chars.items():
        name = re.sub(pattern, replacement, name)
    
    return name

print("fix" +  fix_special_chars("Fran\u00e7ois Hollande"))

class Scraper:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.cookie = self.refresh_cookie()

    def refresh_cookie(self):
        try:
            cookie = requests.get(self.base_url + self.cookies_endpoint).cookies
            return cookie
        except Exception as ex:
            print('Error refreshing cookie:', str(ex))
            # return None

    def get_countries(self):
        try:
            response = requests.get(self.base_url + self.country_endpoint, cookies=self.cookie)
            if response.status_code == 200:
                countries = response.json()
                return countries
            else:
                print("Failed to retrieve countries:", response.status_code)
                # return None
        except Exception as ex:
            print('Error retrieving countries:', str(ex))
            # return None

    def get_leaders(self, country: str):
        leadersList= []
        try:
            response = requests.get(f"{self.base_url}{self.leaders_endpoint}?country={country}", cookies=self.cookie)
            if response.status_code == 200: 
                leaders = response.json()
                for leader in leaders: 
                    cleanFirstName = fix_special_chars(leader["first_name"])
                    cleanLastName= fix_special_chars(leader["last_name"])
                    leadersList.append({"name": cleanFirstName+ " " +  cleanLastName, "wiki_url": leader["wikipedia_url"], "wiki_excerpt": ""})

                self.leaders_data[country] = leadersList
            else:
                print(f"Failed to retrieve leaders for {country}:", response.status_code)
        except Exception as ex:
            print(f'Error retrieving leaders for {country}:', str(ex))

    def get_first_paragraph(self):
        for country, leaders in self.leaders_data.items():
            for leader in leaders:
                leader['wiki_excerpt'] = "This is a dummy excerpt for " + leader['name'] + "."


    def to_json_file(self, filepath: str):
        try:
            with open(filepath, 'w') as f:
                json.dump(self.leaders_data, f, indent=4)
            print("Data saved to", filepath)
        except Exception as ex:
            print('Error saving data to JSON file:', str(ex))
