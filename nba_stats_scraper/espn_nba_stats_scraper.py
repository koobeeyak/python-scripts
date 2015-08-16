#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import re

BASE_URL = "http://espn.go.com/nba/"

def scrape_nba_teams():
	url = BASE_URL + "teams"  # REMEMBER that the url for a specific team will be http://espn.go.com/nba/team/_/name/
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
	return soup

def prompt_user_for_team():
	soup = scrape_nba_teams()
	
	for team_link in soup.find_all('a', href = re.compile(BASE_URL + "team/_/name/*")):
		print team_link
		print team_link['href']
		print team_link.text
		find_abbrev = re.match(r"^.*\/name\/(.*)\/.*$",team_link['href'])
		team_abbrev = find_abbrev.group(1)
		print team_abbrev

if __name__ == "__main__":
	prompt_user_for_team()