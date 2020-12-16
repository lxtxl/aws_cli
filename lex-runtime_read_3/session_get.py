#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/get-session.html
if __name__ == '__main__':
    """
	delete-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/delete-session.html
	put-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-runtime/put-session.html
    """

    parameter_display_string = """
    # bot-name : The name of the bot that contains the session data.
    # bot-alias : The alias in use for the bot that contains the session data.
    """

    execute_two_parameter("lex-runtime", "get-session", "bot-name", "bot-alias", parameter_display_string)