#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-retention-policy.html
if __name__ == '__main__':
    """
	put-retention-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-retention-policy.html
    """

    parameter_display_string = """
    # log-group-name : The name of the log group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("logs", "delete-retention-policy", "log-group-name", add_option_dict)





