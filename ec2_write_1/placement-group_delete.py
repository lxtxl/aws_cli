#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-placement-group.html
if __name__ == '__main__':
    """
	create-placement-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-placement-group.html
	describe-placement-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-placement-groups.html
    """

    parameter_display_string = """
    # group-name : The name of the placement group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-placement-group", "group-name", add_option_dict)





