#!/usr/bin/python

import time, random

POS = {
	'PG':'Point Guard',
	'SG':'Shooting Guard',
	'SF':'Small Forward',
	'PF':'Power Forward',
	'C':'Center',
	}

class Player(object):

	def __init__(self, name, position, college):
		self.name = name
		self.position = position
		self.college = college

	def __repr__(self):
		return "Your name is %s and you're a %s from %s." % (self.name, POS[self.position], self.college)

class Game(object):

	def __init__(self):
		pass

	def start(self):
		print "What will be your player's name?"
		name = raw_input("> ")
		print "What will be your player's position?"
		for p, v in POS.iteritems():
			print "Enter %s for %s " % (p, v)
		position = raw_input("> ").upper()
		while position not in POS.keys(): #Should this be a while True loop?
			print "Type one of the above."
			position = raw_input("> ").upper()
		print "Where did your player go to college?"
		college = raw_input("> ")
		player = Player(name, position, college)
		print "OK..."
		time.sleep(1)
		print "So:"
		time.sleep(1)
		print player


if __name__ == "__main__":
	game = Game()
	game.start()
