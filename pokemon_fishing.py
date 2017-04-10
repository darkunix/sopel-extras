##################################################################################################
# coding=utf-8
# Author: Hercules -- itsheracules@gmail.com -- irc://irc.lunarirc.net/#innuendo
# Description: fish.py for sopel IRC bot, it is a game based on the creatures from the Pokémon   
# series. To trigger the plugin, type ".fish" in the channel. 									 
##################################################################################################
# Copyright 2017 -- Hercules <itsheracules@gmail.com>
##################################################################################################
# The MIT License <https://opensource.org/licenses/MIT>
##################################################################################################
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
# to whom the Software is furnished to do so, subject to the following conditions:
##################################################################################################
# The above copyright notice and this permission notice shall be included in all copies 		 
# or substantial portions of the Software.
##################################################################################################
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 			 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 		 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 			 
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 			 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 			 
# USE OR OTHER DEALINGS IN THE SOFTWARE.
##################################################################################################

from __future__ import unicode_literals, absolute_import, print_function, division
from sopel.module import commands
from sopel.module import rate
from random import choice

@commands("fish")
def fish(bot, trigger):
	fishes = choice(['Magikarp', 'Corphish', 'Crawdaunt', 'Feebas', 'Milotic', 'Goldeen', 'Seaking'])
	if fishes == 'Magikarp':
		bot.say(trigger.nick + ' threw the fishing rod in water and... ')
		bot.say('and there are waves generating in water...')
		bot.say('It seems like a Gyarados')
		bot.say('Awh! It was just a Magikarp')
	if fishes == 'Corphish':
		bot.say(trigger.nick + ' threw the fishing rod in water and... ')
		bot.say('and there are waves generating in water...')
		bot.say('It looks like a crabby Pokémon')
		bot.say('It is a Corphish!')
	if fishes == 'Crawdaunt':
		bot.say(trigger.nick + ' threw the fishing rod in water and... ')
		bot.say('and there are waves generating in water...')
		bot.say('Whoa it looks like a huge Crabby Pokémon')
		bot.say('Guess what! It is a Crawdaunt')
	if fishes == 'Feebas':
		bot.say(trigger.nick + ' threw the fishing rod in water and... ')
		bot.say('and there are waves generating in water...')
		bot.say("cannot say what Pokémon is this now")
		bot.say('after looking into PokéDex, the Pokémon is Feebas!')
	if fishes == 'Milotic':
		bot.say(trigger.nick + ' threw the fishing rod in water and... ')
		bot.say('and there are waves generating in water...')
		bot.say('Wow! this is a Beautiful Pokémon')
		bot.say('You know what this called? Its Milotic')
	if fishes == 'Goldeen':
		bot.say(trigger.nick + ' threw the fishing rod in water and... ')
		bot.say('and there are waves generating in water...')
		bot.say("Beware of its horn!! later don't say I didn't told you!")
		bot.say('It is a Goldeeeen!')
	if fishes == 'Seaking':
		bot.say(trigger.nick + ' threw the fishing rod in water and... ')
		bot.say('and there are waves generating in water...')
		bot.say('The hint lies in the "king of sea!"')
		bot.say('You guessed it right, its Seaking!')
