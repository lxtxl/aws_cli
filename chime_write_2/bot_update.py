#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-bot.html
if __name__ == '__main__':
    """
	create-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-bot.html
	get-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-bot.html
	list-bots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-bots.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # bot-id : The bot ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "update-bot", "account-id", "bot-id", add_option_dict)
