#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-command.html
if __name__ == '__main__':
    """
	list-commands : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-commands.html
	send-command : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/send-command.html
    """

    parameter_display_string = """
    # command-id : The ID of the command you want to cancel.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "cancel-command", "command-id", add_option_dict)





