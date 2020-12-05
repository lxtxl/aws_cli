#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/delete-fleet.html
if __name__ == '__main__':
    """
	create-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/create-fleet.html
	list-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-fleets.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("worklink", "delete-fleet", "fleet-arn", add_option_dict)





