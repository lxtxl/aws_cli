#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot-alias.html
if __name__ == '__main__':
    """
	delete-bot-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot-alias.html
	get-bot-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-alias.html
    """

    parameter_display_string = """
    # name : The name of the alias. The name is not case sensitive.
    # bot-version : The version of the bot.
    # bot-name : The name of the bot.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lex-models", "put-bot-alias", "name", "bot-version", "bot-name", add_option_dict)
