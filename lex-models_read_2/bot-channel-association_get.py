#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-channel-associations.html
if __name__ == '__main__':
    """
	delete-bot-channel-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot-channel-association.html
	get-bot-channel-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-channel-association.html
    """

    parameter_display_string = """
    # bot-name : The name of the Amazon Lex bot in the association.
    # bot-alias : An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
    """

    execute_two_parameter("lex-models", "get-bot-channel-associations", "bot-name", "bot-alias", parameter_display_string)