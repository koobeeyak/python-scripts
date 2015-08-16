#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import re, time

BASE_URL = "http://espn.go.com/nba/"

def generate_team_abbrev_team_name_dict():
	url = BASE_URL + "teams"  # REMEMBER that the url for a specific team will be http://espn.go.com/nba/team/_/name/
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
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
	# TODO: can I make this more user friendly by isolating team name abbreviation from link using regex
	# and having user type abbreviation instead of full name?
	# 	find_abbrev = re.match(r"^.*\/name\/(.*)\/.*$",team_link['href'])
	#	team_abbrev = find_abbrev.group(1)
	print "Which team would you like to see?"
	time.sleep(2)
	for p,v in d.iteritems():
		print "%s" % (p) 
	chosen_team = raw_input("> ")
	while True:
		if chosen_team in d.keys():
			break
		else:
			print "Please enter the exact name of a team above." # TODO: fix this by autocapitalizing first letters and removing whitespace
			chosen_team = raw_input("> ")
	return d[chosen_team] # this is the link to the team's page

if __name__ == "__main__":
	print prompt_user_for_team()