#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import re

BASE_URL = "http://espn.go.com/nba/"

def scrape_nba_teams():
	url = BASE_URL + "teams"  # REMEMBER that the url will change once you click on a team, will have to remove the s 
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
	for team_link in soup.find_all('a', href = re.compile("http://espn.go.com/nba/team/_/name/*")):
		print team_link
		print team_link['href']
		print team_link.text

if __name__ == "__main__":
	scrape_nba_teams()