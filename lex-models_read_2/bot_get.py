#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot.html
if __name__ == '__main__':
    """
	delete-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot.html
	get-bots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bots.html
	put-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot.html
    """

    parameter_display_string = """
    # name : The name of the bot. The name is case sensitive.
    # version-or-alias : The version or alias of the bot.
    """

    execute_two_parameter("lex-models", "get-bot", "name", "version-or-alias", parameter_display_string)