#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot-channel-association.html
if __name__ == '__main__':
    """
	get-bot-channel-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-channel-association.html
	get-bot-channel-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-channel-associations.html
    """

    parameter_display_string = """
    # name : The name of the association. The name is case sensitive.
    # bot-name : The name of the Amazon Lex bot.
    # bot-alias : An alias that points to the specific version of the Amazon Lex bot to which this association is being made.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lex-models", "delete-bot-channel-association", "name", "bot-name", "bot-alias", add_option_dict)
