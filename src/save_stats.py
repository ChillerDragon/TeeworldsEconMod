#!/usr/bin/env python3
from chiller_essential import *
from kills import *
import os.path


def HasStats(name):
    if os.path.isfile("stats/" + name + ".acc"):
        return True
    return False

def SaveStats(name):
    from player import GetPlayerByName
    player = GetPlayerByName(name)
    if not player:
        say("[stats] failed to load player '" + name + "'")
        return False
    if HasStats(name):
        #say("[stats] found stats --> loading and appending")
        load_player = LoadStats(name)
        if not load_player:
            say("[stats] error loading stats for player '" + name + "'")
            return False
        player = player + load_player
    sf = open("stats/" + name + ".acc", "w")
    sf.write(str(player.kills) + "\n")
    sf.write(str(player.deaths) + "\n")
    sf.write(str(player.flag_grabs) + "\n")
    sf.write(str(player.flag_caps_red) + "\n")
    sf.write(str(player.flag_caps_blue) + "\n")
    sf.write(str(player.flag_time) + "\n")
    sf.close()
    return True

def LoadStats(name):
    from player import Player
    if not HasStats(name): 
        return None
    sf = open("stats/" + name + ".acc", "r")
    player = Player(name)
    player.kills = int(sf.readline())
    player.deaths = int(sf.readline())
    player.flag_grabs = int(sf.readline())
    player.flag_caps_red = int(sf.readline())
    player.flag_caps_blue = int(sf.readline())
    player.flag_time = float(sf.readline())
    sf.close()
    return player