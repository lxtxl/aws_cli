#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/add-region.html
if __name__ == '__main__':
    """
	describe-regions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-regions.html
	remove-region : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/remove-region.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory to which you want to add Region replication.
    # region-name : The name of the Region where you want to add domain controllers for replication. For example, us-east-1 .
    # vpc-settings : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ds", "add-region", "directory-id", "region-name", "vpc-settings", add_option_dict)
