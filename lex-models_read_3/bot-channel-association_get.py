#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-channel-association.html
if __name__ == '__main__':
    """
	delete-bot-channel-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot-channel-association.html
	get-bot-channel-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-channel-associations.html
    """

    parameter_display_string = """
    # name : The name of the association between the bot and the channel. The name is case sensitive.
    # bot-name : The name of the Amazon Lex bot.
    """

    execute_two_parameter("lex-models", "get-bot-channel-association", "name", "bot-name", parameter_display_string)