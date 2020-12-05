#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-flow-logs.html
if __name__ == '__main__':
    """
	create-flow-logs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-flow-logs.html
	describe-flow-logs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-flow-logs.html
    """

    parameter_display_string = """
    # flow-log-ids : One or more flow log IDs.
Constraint: Maximum of 1000 flow log IDs.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-flow-logs", "flow-log-ids", add_option_dict)





