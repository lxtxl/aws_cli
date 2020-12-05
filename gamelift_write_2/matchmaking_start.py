#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/start-matchmaking.html
if __name__ == '__main__':
    """
	describe-matchmaking : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-matchmaking.html
	stop-matchmaking : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/stop-matchmaking.html
    """

    parameter_display_string = """
    # configuration-name : Name of the matchmaking configuration to use for this request. Matchmaking configurations must exist in the same Region as this request. You can use either the configuration name or ARN value.
    # players : Information on each player to be matched. This information must include a player ID, and may contain player attributes and latency data to be used in the matchmaking process. After a successful match, Player objects contain the name of the team the player is assigned to.
(structure)

Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
PlayerId -> (string)

A unique identifier for a player

PlayerAttributes -> (map)

A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: "PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}} .
key -> (string)
value -> (structure)

Values for use in  Player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each AttributeValue object can use only one of the available properties.
S -> (string)

For single string values. Maximum string length is 100 characters.

N -> (double)

For number values, expressed as double.

SL -> (list)

For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
(string)

SDM -> (map)

For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.
key -> (string)
value -> (double)



Team -> (string)

Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.

LatencyInMs -> (map)

Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.
If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.
key -> (string)
value -> (integer)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "start-matchmaking", "configuration-name", "players", add_option_dict)
