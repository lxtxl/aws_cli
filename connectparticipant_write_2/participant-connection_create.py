#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectparticipant/create-participant-connection.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # type : Type of connection information required.
(string)
    # participant-token : Participant Token as obtained from StartChatContact API response.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("connectparticipant", "create-participant-connection", "type", "participant-token", add_option_dict)
