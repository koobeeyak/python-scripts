#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import re, time

BASE_URL = "http://espn.go.com/nba/"

def generate_team_abbrev_team_name_dict():
	url = BASE_URL + "teams"  # REMEMBER that the url for a specific team will be http://espn.go.com/nba/team/_/name/
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	team_dict = {}
	for team_link in soup.find_all('a', href = re.compile(BASE_URL + "team/_/name/*")):
		find_abbrev = re.match(r"^.*\/name\/(.*)\/.*$",team_link['href'])
		team_abbrev = find_abbrev.group(1)
		team_dict[team_abbrev] = team_link.text # e.g. {'gs':'Golden State Warriors'}
	return team_dict

def prompt_user_for_team():
	d = generate_team_abbrev_team_name_dict()
	print "\nWhich team would you like to see?\n"
	time.sleep(1)
	for p,v in d.iteritems():
		print "Enter \'%s\' for %s." % (p,v) 
	chosen_team = raw_input("> ").lower()
	while True:
		if chosen_team in d.keys():
			break
		else:
			print "Please enter the abbreviation of a team above."
			chosen_team = raw_input("> ").lower()
	return BASE_URL + "teams/stats?team=" + chosen_team # link to team's page, e.g. http://espn.go.com/nba/teams/stats?team=sa

def scrape_team(chosen_team):           # TODO: -is this scraping postseason or regular season performance?
	response = requests.get(chosen_team)#       -add team name, player id to the list of stats
	soup = BeautifulSoup(response.text, "html.parser")
	players = []
	for player in soup.find_all(class_ = re.compile("player-[0-9]")): # avoid 'player-info' class--that's for top performers (redundant)
		individual_player = []
		for stat in player:
			individual_player.append(stat.text)
		players.append(individual_player)
	return players

if __name__ == "__main__":
	chosen_team = prompt_user_for_team()
	players = scrape_team(chosen_team)
	print players