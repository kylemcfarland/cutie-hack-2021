# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 17:00:05 2021
An random insult generator
@author: Kyle McFarland
"""
import random

adjectives = ['cheese-lipped', 'hallow brained', 'mouse-brained', 'stinky breathed',
              'stinky', 'sticky-fingered', 'unwashed', 'unbrushed', 'sour-smelling',
              'rotten', 'twinkle-toed', 'poopy', 'buttfaced', 'greasy']
nouns = ['weasel', 'fool', 'baffoon', 'tiddywinkle', 'numbskull', 'melon', 'cutie',
         'boob', 'sponge', 'hacker', 'tit', 'carbuncle', 'dingleberry', 'virgin',
         'nerd']

generate = input("Are you ready to get roasted? Y/N ")

if len(generate) == 1: 
    while generate.lower() == "y":
        x = random.randrange(0, len(adjectives))
        y = random.randrange(0, len(nouns))
        print("You " + adjectives[x] + " " + nouns[y])
        generate = input("Still hungry for roast beef? ")
else:
    generate = input("Invalid, please type Y or N you buffoon. ")
    while generate.lower() == "y":
        x = random.randrange(0, len(adjectives))
        y = random.randrange(0, len(nouns))
        print("You " + adjectives[x] + " " + nouns[y])
        generate = input("Still hungry for roast beef? ")
   
    
print("You're weak, but you have beautiful eyes. The nearest tissue station can be found at the next Anime Expo.")
