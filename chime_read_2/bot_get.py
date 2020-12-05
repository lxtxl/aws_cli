#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-bot.html
if __name__ == '__main__':
    """
	create-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-bot.html
	list-bots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-bots.html
	update-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-bot.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # bot-id : The bot ID.
    """

    execute_two_parameter("chime", "get-bot", "account-id", "bot-id", parameter_display_string)