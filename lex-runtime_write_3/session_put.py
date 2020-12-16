#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/put-session.html
if __name__ == '__main__':
    """
	delete-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/delete-session.html
	get-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/get-session.html
    """

    parameter_display_string = """
    # bot-name : The name of the bot that contains the session data.
    # bot-alias : The alias in use for the bot that contains the session data.
    # user-id : The ID of the client application user. Amazon Lex uses this to identify a userâs conversation with your bot.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lex-runtime", "put-session", "bot-name", "bot-alias", "user-id", add_option_dict)
