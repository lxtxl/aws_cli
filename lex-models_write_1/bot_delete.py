#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot.html
if __name__ == '__main__':
    """
	get-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot.html
	get-bots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bots.html
	put-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot.html
    """

    parameter_display_string = """
    # name : The name of the bot. The name is case sensitive.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lex-models", "delete-bot", "name", add_option_dict)





