#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-events-configuration.html
if __name__ == '__main__':
    """
	delete-events-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-events-configuration.html
	put-events-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-events-configuration.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # bot-id : The bot ID.
    """

    execute_two_parameter("chime", "get-events-configuration", "account-id", "bot-id", parameter_display_string)