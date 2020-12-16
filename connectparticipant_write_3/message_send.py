#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectparticipant/send-message.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # content-type : The type of the content. Supported types are text/plain.
    # content : The content of the message.
    # connection-token : The authentication token associated with the connection.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connectparticipant", "send-message", "content-type", "content", "connection-token", add_option_dict)
