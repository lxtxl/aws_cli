#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/remove-permission.html
if __name__ == '__main__':
    """
	put-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-permission.html
    """

    parameter_display_string = """
    # statement-id : The statement ID corresponding to the account that is no longer allowed to put events to the default event bus.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("events", "remove-permission", "statement-id", add_option_dict)





