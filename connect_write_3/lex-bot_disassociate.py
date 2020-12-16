#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-lex-bot.html
if __name__ == '__main__':
    """
	associate-lex-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-lex-bot.html
	list-lex-bots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-lex-bots.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # bot-name : The name of the Amazon Lex bot. Maximum character limit of 50.
    # lex-region : The Region in which the Amazon Lex bot has been created.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "disassociate-lex-bot", "instance-id", "bot-name", "lex-region", add_option_dict)
