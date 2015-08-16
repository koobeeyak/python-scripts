#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import re, time

BASE_URL = "http://espn.go.com/nba/"

def scrape_nba_teams():
	url = BASE_URL + "teams"  # REMEMBER that the url for a specific team will be http://espn.go.com/nba/team/_/name/
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
	return soup

def generate_team_abbrev_team_name_dict():
	soup = scrape_nba_teams()
	team_dict = {}
	for team_link in soup.find_all('a', href = re.compile(BASE_URL + "team/_/name/*")):
		print team_link
		print team_link['href']
		print team_link.text
		find_abbrev = re.match(r"^.*\/name\/(.*)\/.*$",team_link['href'])
		team_abbrev = find_abbrev.group(1)
		print team_abbrev
		team_dict[team_link.text] = team_link['href']
	return team_dict

def prompt_user_for_team():
	d = generate_team_abbrev_team_name_dict()
	print "Enter the abbreviation for the team you would like to see stats for."
	time.sleep(2)
	for p,v in d.iteritems():
		print "Enter %s for %s." % (p,v)
	chosen_team = raw_input("> ")
	while True:
		if chosen_team in d.keys():
			break
		else:
			print "Enter one of the abbreviations above."
			chosen_team = raw_input("> ").lower()
	return d[chosen_team]

if __name__ == "__main__":
	print prompt_user_for_team()