#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot-alias.html
if __name__ == '__main__':
    """
	get-bot-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-alias.html
	put-bot-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot-alias.html
    """

    parameter_display_string = """
    # name : The name of the alias to delete. The name is case sensitive.
    # bot-name : The name of the bot that the alias points to.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lex-models", "delete-bot-alias", "name", "bot-name", add_option_dict)
