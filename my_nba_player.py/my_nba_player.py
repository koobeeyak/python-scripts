#!/usr/bin/python

import time, random

POS = { # Abbreviations much more practical. Use dict to print player info and check correct input when creating player.
	'PG':'Point Guard',
	'SG':'Shooting Guard',
	'SF':'Small Forward',
	'PF':'Power Forward',
	'C':'Center',
	}

class Player(object):
	"""
	Our NBA Player.
	"""

	def __init__(self, name, position, college):
		self.name = name
		self.position = position
		self.college = college

	def __repr__(self):
		return "Your name is %s and you're a %s from %s." % (self.name, POS[self.position], self.college)

class Engine(object):
	"""
	How our game will work.
	"""

	def __init__(self):
		pass

	def start(self):
		"""
		Prompt for Player creation.
		"""
		print "What will be your player's name?"
		name = raw_input("> ")
		print "What will be your player's position?"
		for p, v in POS.iteritems():
			print "Enter %s for %s " % (p, v)
		position = raw_input("> ").upper()
		while True:
			if position in POS.keys():
				break
			else:
				print "Enter one of the above position abbreviations."
				position = raw_input("> ").upper()
		print "Where did your player go to college?"
		college = raw_input("> ")
		player = Player(name, position, college)
		print "OK..."
		time.sleep(1)
		print "So:"
		time.sleep(1)
		print player
		return player

if __name__ == "__main__":
	engine = Engine()
	player = engine.start()
