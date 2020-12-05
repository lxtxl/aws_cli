#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot-version.html
if __name__ == '__main__':
    """
	create-bot-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-bot-version.html
	get-bot-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-versions.html
    """

    parameter_display_string = """
    # name : The name of the bot.
    # bot-version : The version of the bot to delete. You cannot delete the $LATEST version of the bot. To delete the $LATEST version, use the  DeleteBot operation.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lex-models", "delete-bot-version", "name", "bot-version", add_option_dict)
