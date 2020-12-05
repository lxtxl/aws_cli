#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-alias.html
if __name__ == '__main__':
    """
	delete-bot-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot-alias.html
	put-bot-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot-alias.html
    """

    parameter_display_string = """
    # name : The name of the bot alias. The name is case sensitive.
    # bot-name : The name of the bot.
    """

    execute_two_parameter("lex-models", "get-bot-alias", "name", "bot-name", parameter_display_string)